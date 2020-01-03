from django.db import models
from datetime import datetime

class Document(models.Model):
	about = models.TextField()
	file = models.FileField(upload_to='user_docs')
	date_posted = models.CharField(max_length=70 ,default=datetime.now().strftime("%d %B %Y %I:%M%p"))
