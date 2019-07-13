from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.conf import settings

from modules.models import Page, AppDetails, User, Fbuser
from modules.facebook.graphapi import api

from crontab import CronTab
import getpass
import os
import json
from modules.aesEncryption import aesEncryption


class sentiment_analysis(TemplateView):
    def get(self, request, *args, **kwargs):

        # Fetch sentiment_analysis from request
        page_id = request.GET.get('page_id', None)

        pageObj = Page.objects.get(page_id=page_id)
        pageObj.sentiment_analysis = not pageObj.sentiment_analysis

        self.cronjob(pageObj.sentiment_analysis, page_id)

        pageObj.save()

        response = {"sentiment_analysis": pageObj.sentiment_analysis}

        return JsonResponse(response)

    def cronjob(self, run_sent, page_id):
        if run_sent:
            self.start_cron(page_id)
        else:
            self.stop_cron(page_id)

    def start_cron(self, page_id):
        # Fetch access token
        access_token = Page.objects.get(page_id=page_id).access_token

        # Fetch user
        os_user = getpass.getuser()

        # Initializing cron
        comment_cron = CronTab(user=os_user)

        # Setting python command
        command = "python3 " + os.path.join(settings.BASE_DIR, 'modules',
                                            'comment_manager.py --access_token ' + access_token + ' --page_id ' + str(
                                                page_id))

        job = comment_cron.new(command=command, comment=str(page_id))
        job.minute.every(2)
        comment_cron.write()

    def stop_cron(self, page_id):
        # Fetch user
        os_user = getpass.getuser()

        # Initializing cron
        comment_cron = CronTab(user=os_user)
        for job in comment_cron:
            if job.comment == str(page_id):
                comment_cron.remove(job)
                comment_cron.write()


class ad_only(TemplateView):
    def get(self, request, *args, **kwargs):
        # Fetch page id
        page_id = request.GET.get('page_id', None)

        # Fetch page obj
        pageObj = Page.objects.get(page_id=page_id)
        # Flip ad only
        pageObj.ad_only = not pageObj.ad_only
        pageObj.save()

        response = {"ad_only": pageObj.ad_only}

        return JsonResponse(response)


class fetch_pages(TemplateView):
    def get(self, request, *args, **kwargs):

        user_id_frm_get = request.GET.get('user_id', None)
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

        # Setting response
        response = {}

        # Fetching pages
        pages = []
        for datum in data["data"]:
            page_name = datum["name"]
            page_id = datum["id"]
            page_access_token = datum["access_token"]

            # Fetching page image
            apiObj.set_access_token(page_access_token)
            params = {'redirect': '0'}
            page_image_data = apiObj.get(link=str(page_id) + "/picture", params=params)
            page_image = page_image_data["data"]["url"]

            page_ = {}
            page_["page_id"] = page_id
            page_["page_name"] = page_name
            page_["page_access_token"] = page_access_token
            page_["page_image"] = page_image

            try:
                Page(uid=int(user_id_frm_get), page_id=page_id, name=page_name, image=page_image,
                     access_token=page_access_token, sentiment_analysis=False).save()
                page_["selected"] = False
            except Exception as e:
                page_["selected"] = True
                print(str(e))

            pages.append(page_)

        response["pages"] = pages

        return JsonResponse(response)


class add_pages(TemplateView):
    def get(self, request, *args, **kwargs):
        pages = request.GET.get('page_ids', None)

        pages_list = json.loads(pages)

        for page_id in pages_list:
            print(page_id)
            pageObj = Page.objects.get(page_id=str(page_id))
            if pageObj:
                print(pageObj)
                pageObj.selected = True
                pageObj.sentiment_analysis = True
                sentAn = sentiment_analysis()
                sentAn.cronjob(True, page_id)
                pageObj.save()

        return JsonResponse({"Success": True})


class flip_page_selection(TemplateView):
    def get(self, request, *args, **kwargs):
        page_id = request.GET.get('page_id', None)

        pageObj = Page.objects.get(page_id=page_id)
        pageObj.selected = not pageObj.selected
        pageObj.sentiment_analysis = not pageObj.sentiment_analysis

        pageObj.save()

        sentAn = sentiment_analysis()
        sentAn.cronjob(pageObj.sentiment_analysis, page_id)

        return JsonResponse({"Success": True})


class register(TemplateView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        email = request.GET.get('email')
        passwd = request.GET.get('passwd')

        if name and email and passwd:
            aesObj = aesEncryption()
            encPassword = aesObj.EncodeAES(passwd)
            userObj = User(name=name, email=email, password=encPassword)
            try:
                userObj.save()
                uid = userObj.id
                response = {"success": True, "redirect": "/fbsignup?uid=" + str(uid)}
            except:
                response = {"success": False}
        else:
            response = {"success": False}

        return JsonResponse(response)


class login(TemplateView):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')
        passwd = request.GET.get('passwd')

        login = False
        response = {}

        if email and passwd:
            aesObj = aesEncryption()
            encPassword = aesObj.EncodeAES(passwd)
            try:
                userObj = User.objects.get(email=email, password=encPassword)
                if userObj:
                    login = True
                    response["redirect"] = "/dashboard/?uid=" + str(userObj.id)
            except Exception as e:
                print(e)

        response["login"] = login

        return JsonResponse(response)


class facebook_login(TemplateView):
    def get(self, request, *args, **kwargs):
        response = {}

        uid = request.GET.get('uid', None)
        client_id = AppDetails.objects.get(keyname='client_id').value
        client_secret = AppDetails.objects.get(keyname='client_secret').value

        user_token = request.GET.get("access_token")

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
        image = ""

        # update access token to db
        fbuserObj = Fbuser(uid=uid, access_token=user_access_token, image=image)
        fbuserObj.save()

        # Update fb check
        userObj = User.objects.get(id=uid)
        userObj.chk_facebook = True
        userObj.save()

        response["redirect"] = "/dashboard/?uid=" + str(uid)
        return JsonResponse(response)
