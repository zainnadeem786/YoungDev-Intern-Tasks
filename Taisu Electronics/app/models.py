from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title
    
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=0)
    


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Details for {self.product.name}"