from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 100) #blog title
	category = models.CharField(max_length = 50, blank = True)
	date_time = models.DateTimeField(auto_now_add = True)
	content = models.TextField(blank = True, null = True)

def _unicode_(self):
	return self.title

class Meta: #order by date_time desc
	ordering = ['-date_time']
