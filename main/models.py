from django.db import models

# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('apparel', 'Apparel'),
        ('accessories', 'Accessories'),
        ('collectibles', 'Collectibles'),
        ('sneakers', 'Sneakers'),
    ]
    
    # Required Attributes
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    # Extras
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    