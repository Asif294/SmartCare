from rest_framework import  serializers
from .import models
class AppintmentSerializer(serializers.ModelSerializer):
    time=serializers.StringRelatedField(many=False)
    patient=serializers.StringRelatedField(many=False)
    doctor=serializers.StringRelatedField(many=False)
 
    class Meta:
        model=models.Appintment
        fields='__all__'
