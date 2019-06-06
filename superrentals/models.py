import itertools

from django.db import models
from django.utils.text import slugify


class Rental(models.Model):
    CATEGORIES = (
        ('Condo', 'Condo'),
        ('Townhouse', 'Townhouse'),
        ('Apartment', 'Apartment'),
        ('Estate', 'Estate'),
    )

    id = models.SlugField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORIES)
    bedrooms = models.PositiveSmallIntegerField()
    image = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Automatically generating unique slugs
    # Based on: https://joseph.is/2EVsTZk
    def save(self, *args, **kwargs):
        if not self.id:
            max_length = Rental._meta.get_field('id').max_length
            slug = slugify(self.title)
            self.id = slug[:max_length]

            for x in itertools.count(1):
                if not Rental.objects.filter(id=self.id).exists():
                    break
                # truncate the original slug minus 1 for the hyphen
                self.id = '{}-{}'.format(
                        slug[:max_length - len(str(x)) - 1], x)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated_at']
