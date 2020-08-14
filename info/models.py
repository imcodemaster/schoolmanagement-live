from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    salary = models.FloatField()
    age = models.IntegerField()
    phonenumber = models.IntegerField() #without country code
    aadaharid = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
	#slug = models.SlugField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
        	url = ''
        return url


class Notice(models.Model):
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    published = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
    textcontent = models.TextField(null = True, blank = True)

    class Meta:
        ordering = ['-published']


    def __str__(self):
        return self.title
