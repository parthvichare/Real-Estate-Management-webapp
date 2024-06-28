from django.db import models
from django.utils import timezone
import numpy as np
from django.db import models

class Post(models.Model):
    property_id = models.CharField(max_length=8, default='UNKNOWN', null=False)
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100,null=True)
    beds = models.IntegerField(null=True)
    floor = models.CharField(max_length=20, default='')
    furnishing = models.CharField(max_length=10, default='')
    super_areas = models.CharField(max_length=100, default='',null=False)
    area_sqft = models.CharField(max_length=100, default='',null=False)
    # amenities=models.TextField(null=False)
    # NearbyLocality=models.TextField()
    Image_url=models.CharField(max_length=100,default='',null=False)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name or f"Property {self.property_id}"