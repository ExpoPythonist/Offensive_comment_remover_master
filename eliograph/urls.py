from django.contrib import admin
from django.urls import path, include
from frontend.views import dashboard, login, signup, fbsignup, settings, pageselect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Front end urls
    path('dashboard/', dashboard.as_view(), name="dashboard"),
    path('login/', login.as_view(), name="login"),
    path('signup/', signup.as_view(), name="signup"),
    path('fbsignup/', fbsignup.as_view(), name="fbsignup"),
    path('settings/', settings.as_view(), name="settings"),
    path('pageselect/', pageselect.as_view(), name="pageselect"),
]
