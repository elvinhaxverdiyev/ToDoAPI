from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    is_complete = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
