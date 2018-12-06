import datetime

from django.db import models
from django.utils import timezone

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __str__(self):
#    	return self.question_text
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Create your models here.
class Post(models.Model):
	post_title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	image = models.ImageField(upload_to = 'posts')
	body = models.TextField()
	def __str__(self):
		return self.post_title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
