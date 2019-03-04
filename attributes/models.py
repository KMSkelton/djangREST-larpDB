from django.db import models

class Attribute(models.Model):
    
    attribute_name = models.CharField(max_length=20)
    attribute_description = models.CharField(max_length=2500)