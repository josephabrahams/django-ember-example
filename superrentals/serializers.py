from rest_framework import serializers

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = (
            'title',
            'owner',
            'city',
            'category',
            'image',
            'bedrooms',
            'description',
        )
