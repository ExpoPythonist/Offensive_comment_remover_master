from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from modules.models import User, Fbuser, Page, AppDetails, CommentLog
from modules.facebook.graphapi import api
import datetime


class dashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        uid = request.GET.get('uid', None)
        page_id = request.GET.get('page_id', None)

        response = {}
        
        response["uid"] = uid

        # Check if signup complete
        userObj = User.objects.get(id=uid)
        if not userObj.chk_facebook:
            # redirect to fbsignup page
            red_link = "/fbsignup/?uid=" + str(uid)
            return redirect(red_link)
        
        if not userObj.chk_pages:
            # redirect to select pages page
            red_link = "/pageselect/?uid=" + str(uid)
            return redirect(red_link)

        # Fetch pages and details
        pageObjs = Page.objects.filter(uid=uid).order_by("name")

        self.fetch_pages(uid)

        pageObjsel = Page.objects.filter(uid=uid, selected=1).order_by("name")

        if not pageObjsel:
            red_link = "/pageselect?uid=" + str(uid)
            return redirect(red_link)

        if not page_id:            
            red_link = "/dashboard/?uid=" + str(uid) + "&&page_id=" + pageObjsel[0].page_id
            return redirect(red_link)
                
        
        pages = []
        curpage = {}
        for pageObj in pageObjs:
            page = {
                "page_id": pageObj.page_id,
                "name": pageObj.name,
                "image": pageObj.image,
                "access_token": pageObj.access_token,
                "ad_only": pageObj.ad_only,
                "sentiment_analysis": pageObj.sentiment_analysis,
                "selected": pageObj.selected
            }
            pages.append(page)

            if pageObj.page_id == page_id:
                curpage = page
        
        response["pages"] = pages
        response["curpage"] = curpage

        # Setting count of deleted comments
        comment_count = CommentLog.objects.filter(page_id=page_id).count()

        response["comment_count"] = comment_count

        # This week comment
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        weekcount = CommentLog.objects.filter(page_id=page_id, date_time__range=[start_week, end_week]).count()

        response["weekcount"] = weekcount

        # Fetch all comments filtered
        commentLogObjs = CommentLog.objects.filter(page_id=page_id)
        comments = []
        for commentLogObj in commentLogObjs:
            comment = {
                "date": commentLogObj.date_time,
                "comment": commentLogObj.comment
            }
            comments.append(comment)
        
        response["comments"] = comments

        return render(request, 'dashboard.html', response)
    
    def fetch_pages(self, uid):
        # Fetch pages
        user_id_frm_get = uid
        client_id = AppDetails.objects.get(keyname='client_id').value
        client_secret = AppDetails.objects.get(keyname='client_secret').value

        user_token = Fbuser.objects.get(uid=user_id_frm_get).access_token

        # Get fb exchange token
        apiObj = api()
        apiObj.set_access_token(user_token)
        apiObj.set_version("v3.3")
        params = {}
        
        params["grant_type"] = "fb_exchange_token"
        params["client_id"] = client_id
        params["client_secret"] = client_secret
        params["fb_exchange_token"] = user_token

        data = apiObj.get(link="oauth/access_token", params=params)

        # User token never ending
        user_access_token = data["access_token"]

        # Settings new access token
        apiObj.set_access_token(user_access_token)

        data = apiObj.get(link="me")

        # Setting user id
        user_id = data["id"]

        # Fetching pages
        data = apiObj.get(link=str(user_id) + "/accounts")
        
        # Fetching pages
        pages = []
        for datum in data["data"]:
            page_name = datum["name"]
            page_id = datum["id"]
            page_access_token = datum["access_token"]

            # Fetching page image
            apiObj.set_access_token(page_access_token)
            params = {'redirect':'0'}
            page_image_data = apiObj.get(link=str(page_id) + "/picture", params=params)            
            page_image = page_image_data["data"]["url"]

            try:
                Page(uid=int(user_id_frm_get), page_id=page_id, name=page_name, image=page_image, access_token=page_access_token, sentiment_analysis=False).save()
            except Exception as e:
                print(str(e))

class login(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

class signup(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')

class fbsignup(TemplateView):
    def get(self, request, *args, **kwargs):
        response = {}
        client_id = AppDetails.objects.get(keyname="client_id").value
        client_secret = AppDetails.objects.get(keyname="client_secret").value

        response["client_id"] = client_id
        response["uid"] = request.GET.get("uid")

        return render(request, 'signup1.html', response)

class settings(TemplateView):
    def get(self, request, *args, **kwargs):
        uid = request.GET.get('uid', None)
        response = {}
        response["uid"] = uid

        userObj = User.objects.get(id=uid)
        fbObj = Fbuser.objects.get(uid=uid)

        response["email"] = userObj.email
        response["name"] = userObj.name
        response["image"] = fbObj.image

        return render(request, 'settings.html', response)        

class pageselect(TemplateView):
    def get(self, request, *args, **kwargs):
        uid=request.GET.get('uid')

        response = {}

        response["uid"] = uid

        # Update pageselect
        userObj = User.objects.get(id=uid)
        userObj.chk_pages = True
        userObj.save()

        # Fetch pages
        dashObj = dashboard()
        dashObj.fetch_pages(uid)

        pageObjs = Page.objects.filter(uid=uid).order_by("name")

        pages = []
        
        for pageObj in pageObjs:
            page = {
                "page_id": pageObj.page_id,
                "name": pageObj.name,
                "image": pageObj.image,
                "access_token": pageObj.access_token,
                "ad_only": pageObj.ad_only,
                "sentiment_analysis": pageObj.sentiment_analysis,
                "selected": pageObj.selected
            }
            pages.append(page)
        
        response["pages"] = pages

        return render(request, 'page-select.html', response)