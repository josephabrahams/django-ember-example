from django.contrib import admin

from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'city', 'category',
                    'bedrooms', 'created_at', 'updated_at')
    # prepopulated_fields = {'id': ('title',)}
    # readonly_fields = ('created_at', 'updated_at')
    # readonly_fields = ('slug', 'created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # object already exists
            return ('slug', 'created_at', 'updated_at')
        else:
            return ()

    def slug(self, obj):
        return obj.id

    # def get_readonly_fields(self, request, obj=None):
    #     if obj: #This is the case when obj is already created i.e. it's an edit
    #         return ['players']
    #     else:
    #         return []


admin.site.register(Rental, RentalAdmin)
