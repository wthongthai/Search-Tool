# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

#class History(models.Model):
#    id = models.IntegerField()
#    id2 = models.IntegerField(null=True, blank=True)
#    object = models.IntegerField()
#    saved = models.DateTimeField()
#    user = models.IntegerField()
#    class Meta:
#        db_table = 'history'

class Questions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    solution = models.TextField(blank=True)
    keywords = models.CharField(max_length=100L, blank=True)
    author = models.IntegerField()
    textbook = models.IntegerField(null=True, blank=True)
    chapter = models.CharField(max_length=5L, blank=True)
    permissions = models.CharField(max_length=10L)
    level = models.CharField(max_length=1L, blank=True)
    mode = models.CharField(max_length=100L)
    code = models.CharField(max_length=50L, blank=True)
    comment = models.CharField(max_length=125L, blank=True)
    useable = models.CharField(max_length=1L)
    locked = models.CharField(max_length=1L)
    class Meta:
        db_table = 'questions'


class Textbooks(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50L)
    name = models.CharField(max_length=255L)
    edition = models.CharField(max_length=20L, blank=True)
    code = models.CharField(max_length=30L, unique=True, blank=True)
    chapters = models.IntegerField(null=True, blank=True)
    publisher = models.IntegerField(null=True, blank=True)
    gif = models.CharField(max_length=255L, blank=True)
    credit = models.CharField(max_length=255L, blank=True)
    available = models.CharField(max_length=1L, blank=True)
    info = models.CharField(max_length=255L, blank=True)
    short = models.CharField(max_length=50L, blank=True)
    long_author = models.CharField(max_length=255L, blank=True)
    copyright = models.CharField(max_length=40L, blank=True)
    copyright_wa = models.CharField(max_length=40L, blank=True)
    permission = models.CharField(max_length=1L, blank=True)
    publisher_textbook = models.CharField(max_length=1L)
    original_content = models.CharField(max_length=1L)
    labs = models.CharField(max_length=1L)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'textbooks'
                                      