from rest_framework import serializers
from .models import Wiwako

class WiwakoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiwako
        fields = '__all__'