from django.db import models

# Create your models here.

class fan(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class trainee(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class coach(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name= models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class ShopItem(models.Model):
	CATEGORY =(
		('BasketBall','BasketBall'),
		('FootBall','FootBall'),
		)
	name= models.CharField(max_length=200, null=True)
	price= models.FloatField(null=True)
	category= models.CharField(max_length=200, choices= CATEGORY, null=True)
	description= models.CharField(max_length=200, null=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	tags= models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class OrderShop(models.Model):
	STATUS =(
		('Pending', 'Pending'),
		('Out for delivery','Out for delivery'),
		('Delivered', 'Delivered'),
		)
	fan = models.ForeignKey(fan, null=True, on_delete=models.SET_NULL, blank=True)
	trainee = models.ForeignKey(trainee, null=True, on_delete=models.SET_NULL, blank=True)
	coach = models.ForeignKey(coach, null=True, on_delete=models.SET_NULL, blank=True)
	shop_item= models.ForeignKey(ShopItem, null=True, on_delete=models.SET_NULL)

	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, choices=STATUS, null=True)


class ticket(models.Model):
	CATEGORY =(
		('BasketBall','BasketBall'),
		('FootBall','FootBall'),
		)
	name= models.CharField(max_length=200, null=True)
	price= models.FloatField(null=True)
	category= models.CharField(max_length=200, choices= CATEGORY, null=True)
	descirption= models.CharField(max_length=200, null=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class OrderTicket(models.Model):
	STATUS =(
		('Pending', 'Pending'),
		('Paid','Paid'),
		)
	fan = models.ForeignKey(fan, null=True, on_delete=models.SET_NULL, blank=True)
	trainee = models.ForeignKey(trainee, null=True, on_delete=models.SET_NULL, blank=True)
	coach = models.ForeignKey(coach, null=True, on_delete=models.SET_NULL, blank=True)
	order_ticket= models.ForeignKey(ticket, null=True, on_delete=models.SET_NULL)
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, choices=STATUS, null=True)

	
