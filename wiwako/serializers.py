from rest_framework import serializers
from .models import Wiwako
from carousel.models import CarouselItem

class WiwakoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiwako
        fields = '__all__'



class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = ['id', 'title', 'photo', 'wiwako']