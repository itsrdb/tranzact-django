from rest_framework import serializers
from . models import employees, company, invoices

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        # fields = ('username','email','company','access')
        fields = '__all__'

class companySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = company
        # fields = ('username','email','company','access')
        fields = '__all__'

class invoicesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = invoices
        # fields = ('username','email','company','access')
        fields = '__all__'