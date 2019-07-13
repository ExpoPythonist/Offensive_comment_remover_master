# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):
    name = models.CharField(unique=True, max_length=250)
    email = models.CharField(unique=True, max_length=50)
    password = models.TextField()
    chk_facebook = models.BooleanField(default=False)
    chk_pages = models.BooleanField(default=False)
    chk_creditcard = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'user'



class Fbuser(models.Model):
    uid = models.IntegerField()
    access_token = models.TextField()
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Uid: " + str(self.uid)

    class Meta:
        managed = False
        db_table = 'fbuser'


class Page(models.Model):
    uid = models.IntegerField()
    page_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    image = models.TextField(blank=True, null=True)
    access_token = models.TextField()
    ad_only = models.BooleanField(default=False)
    sentiment_analysis = models.BooleanField(default=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return "UId: " + str(self.uid) + " -> " + self.name

    class Meta:
        managed = False
        db_table = 'page'

class AppDetails(models.Model):
    keyname = models.CharField(max_length=500)
    value = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'app_details'

class CommentLog(models.Model):
    page_id = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comment_log'