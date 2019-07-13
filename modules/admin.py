from django.contrib import admin
from modules.models import User, Fbuser, Page

# Register your models here.
admin.site.register(User)
admin.site.register(Fbuser)
admin.site.register(Page)