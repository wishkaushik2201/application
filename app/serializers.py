from rest_framework import serializers
from .models import demodb

class demo_rest(serializers.ModelSerializer):
    class Meta:
        model=demodb
        fields='__all__'