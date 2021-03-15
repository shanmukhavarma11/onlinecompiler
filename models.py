from django.db import models

class Database1(models.Model):
	code=models.TextField()
	input1=models.TextField()
	def __str__(self):
		return self.code
