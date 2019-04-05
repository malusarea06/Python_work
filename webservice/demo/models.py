from django.db import models

# Create your models here.
class NewUser(models.Model):
	username = models.CharField(max_length=20)
	city = models.CharField(max_length=20)

	class Meta:
		db_table = 'newuser'