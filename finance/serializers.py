from rest_framework.serializers import ModelSerializer
from .models import *

class TreasurySerializer(ModelSerializer):
    class Meta:
        model = Treasury
        fields = '__all__'
