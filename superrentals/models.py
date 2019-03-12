import uuid

from django.db import models


class Rental(models.Model):
    CATEGORIES = (
        ('Condo', 'Condo'),
        ('Townhouse', 'Townhouse'),
        ('Apartment', 'Apartment'),
        ('Estate', 'Estate'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORIES)
    image = models.URLField()
    bedrooms = models.PositiveSmallIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
