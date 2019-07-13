from django.urls import path, include
from api.views import sentiment_analysis, ad_only, fetch_pages, add_pages, flip_page_selection, register, login, facebook_login

urlpatterns = [
    path('sentiment_analysis/', sentiment_analysis.as_view(), name="sentiment_analysis"),
    path('ad_only/', ad_only.as_view(), name="ad_only"),
    path('fetch_pages/', fetch_pages.as_view(), name="fetch_pages"),
    path('add_pages/', add_pages.as_view(), name="add_pages"),
    path('flip_page_selection/', flip_page_selection.as_view(), name="flip_page_selection"),
    path('register', register.as_view(), name="register"),
    path('login', login.as_view(), name="login"),    
    path('facebook_login', facebook_login.as_view(), name="facebook_login"),
]
