from rest_framework.serializers import ModelSerializer
from . models import * 

class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'