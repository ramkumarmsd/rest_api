from rest_framework import serializers
from .models import datas

class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = datas
        fields = ['id','name','description']