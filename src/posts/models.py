from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class post(models.Model):
	user							= models.ForeignKey(User, on_delete=models.CASCADE)
	title							= models.CharField(max_length=120,unique=True)
	content							= models.TextField()
	publish_date					= models.DateField(default='2018-5-13')
	timestamp						= models.DateTimeField(auto_now_add=True)
	Updated							= models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return  self.title[:50]

	class Meta:
		verbose_name 				= 'Blog Post'
		verbose_name_plural 		= 'Blog Posts'
		ordering					= ['-publish_date','-pk'] #primary key
		