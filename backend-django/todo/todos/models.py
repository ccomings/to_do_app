from django.db import models

# Create your models here.
class Todo(models.Model):
    date = models.DateTimeField("Due Date")
    text = models.CharField("Description", max_length=300)
    
    def __str__(self):
        return self.text
    def __date__(self):
        return self.date