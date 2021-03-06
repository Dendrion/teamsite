from django.db import models
from django.contrib.auth.models import User
import os.path
from django.conf import settings

class Base(models.Model):
    #TODO: i think we don't need this field to be nullable, they always must be filled.
    created_by = models.ForeignKey(User, related_name = '%(class)s_relate', blank = True, null = True)
    created_at = models.DateField(auto_now_add = True, blank = True, null = True)
    modified_by = models.ForeignKey(User, related_name = '%(class)s_related', blank = True, null = True)
    modified_at = models.DateField(auto_now = True, blank = True, null = True)
	
    class Meta:
        abstract = True

class Image(Base):    
    title = models.CharField(max_length=60)
    url = models.ImageField(upload_to= u'%s/img' % settings.MEDIA_ROOT, blank = True, null = True)

class Employee(Base):
    name = models.CharField(max_length=30)
    #address = models.CharField(max_length=50)
    skype = models.CharField(max_length=20, blank = True, null = True)
    jabber = models.CharField(max_length=20, blank = True, null = True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField(blank = True, null = True)
    position_in_team = models.CharField(max_length=60, blank = True, null = True)
    education = models.CharField(max_length=60)
    skills = models.CharField(max_length=60, blank = True, null = True)
    info = models.TextField()
    user = models.OneToOneField(User, related_name = 'employee', blank = True, null = True)
    img = models.OneToOneField(Image, related_name = 'employee', blank = True, null = True)
    
    def __unicode__(self):
         return u'Employee %s' % self.name

class Projects(Base):
    name = models.CharField(max_length=30)
    url_address = models.URLField()
    info = models.TextField()
    date_start = models.DateField()
    client = models.CharField(max_length=30, blank = True, null = True)
    authors = models.ManyToManyField(Employee, related_name = 'projects')
    screenshots = models.ManyToManyField(Image, related_name = 'projects')

    def __unicode__(self):
        return u'Project %s' % self.name

class Article(Base):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now = True)
    text = models.TextField()
    author = models.ForeignKey(Employee, related_name = 'article', blank = True, null = True)
    #TODO: rename this to 'images' (should be plural) and related name to 'artiles' (should be plural too)
    img = models.ManyToManyField(Image, related_name = 'article', blank = True, null = True)

"""    
class Price(Base):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
"""    
    
