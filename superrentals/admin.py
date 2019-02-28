from django.contrib import admin

from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'city', 'category',
                    'bedrooms', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Rental, RentalAdmin)
