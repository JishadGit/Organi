from django.db import models

class register_tb(models.Model):
	NAME = models.CharField(max_length=255)
	EMAIL = models.CharField(max_length=255)
	PHONE = models.CharField(max_length=255)
	PASSWORD = models.CharField(max_length=255)
	ADDRESS = models.CharField(max_length=255,default="0")
	STATUS = models.CharField(max_length=255,default="1")
	IMAGE = models.ImageField(upload_to='user/',blank=True)
	hashpass=models.TextField()



class product(models.Model):
	PRODUCT_NAME = models.CharField(max_length=255)
	PRODUCT_DESCRIPTION = models.CharField(max_length=1000)
	CATEGORY = models.CharField(max_length=255)
	PRICE = models.CharField(max_length=255)
	QUANTITY = models.CharField(max_length=255)
	IMAGE = models.ImageField(upload_to='product/')
	STATUS = models.CharField(max_length=255,default="1")


class cart(models.Model):
	PID = models.ForeignKey(product, on_delete=models.CASCADE)
	UID = models.ForeignKey(register_tb, on_delete=models.CASCADE)
	TOTAL_PRICE = models.CharField(max_length=255)
	STATUS = models.CharField(max_length=255,default="pending")
	QUANTITY = models.CharField(max_length=255)

class shipping_tb(models.Model):
	UID = models.ForeignKey(register_tb, on_delete=models.CASCADE)
	TOTAL_PRICE = models.CharField(max_length=255)
	STATUS = models.CharField(max_length=255,default="pending")
	ADD = models.CharField(max_length=255)
	ADDRESS = models.TextField()


	
class payment_tb(models.Model):
	UID = models.ForeignKey(register_tb, on_delete=models.CASCADE)
	TOTAL_PRICE = models.CharField(max_length=255)
	STATUS = models.CharField(max_length=255,default="pending")
	DATE = models.CharField(max_length=255)
