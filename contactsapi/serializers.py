from .models import Contact,Portfolio,Mapper

from rest_framework import serializers

class contactserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

