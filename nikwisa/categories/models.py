from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """Main category for different domains like weddings, gyms, etc."""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  # Image field for categories

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Subcategories under a main category."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategories/', blank=True, null=True)  # Image field for subcategories

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

