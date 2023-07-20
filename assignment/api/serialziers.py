from rest_framework import serializers
from CRUD.models import student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = '__all__'

    # def get_dob(self, obj):
    #     return obj.dob.strftime('%d-%m-%Y')