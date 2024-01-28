from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    # Name = serializers.CharField(max_length=10)

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_Name(self, name):
        if len(name) <= 3:
            raise serializers.ValidationError("Please Name Characters More Than Three ")
        return name
