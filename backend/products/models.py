from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField( max_length=50)
	content = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title

