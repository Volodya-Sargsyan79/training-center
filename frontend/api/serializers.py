from rest_framework import serializers
from ..models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'date', 'image', 'email', 'user_name')