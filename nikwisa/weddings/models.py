

from django.db import models
from django.utils.text import slugify
from categories.models import SubCategory



class Wedding(models.Model):
    """Products under wedding-related categories."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, related_name="weddings", on_delete=models.CASCADE)
    overview = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    photos = models.JSONField(default=list)  # Array of image URLs
    services = models.JSONField(default=list)  # Array of service objects

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

