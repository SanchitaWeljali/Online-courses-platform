from django.db import models
from django.utils import timezone

class Category(models.Model):
    #fields for attributes for category models
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    
#one to many relationship between category & course

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #if category gets deleted courses are deleted
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title