from asyncio import ReadTransport
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uritemplate import partial
from urllib3 import Retry
from .models import company, employees, invoices
from .serializers import employeesSerializer, companySerializer, invoicesSerializer

class employeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many=True)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request):
        serialzer = employeesSerializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)

class employeeListSingle(APIView):
    
    def get(self, request, id):
        try:
            employees1 = employees.objects.get(id = id)
        except:
            return Response({"error":"employee does not exist"})
        serializer = employeesSerializer(employees1)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request, id):
        # pass
        try:
            employees1 = employees.objects.get(id = id)
        except:
            return Response({"error":"employee does not exist"})
        serialzer = employeesSerializer(employees1, data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)

class companyList(APIView):
    
    def get(self, request):
        company1 = company.objects.all()
        serializer = companySerializer(company1, many=True)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request):
        serialzer = companySerializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)

class companyListSingle(APIView):
    
    def get(self, request, id):
        try:
            company1 = company.objects.get(id = id)
        except:
            return Response({"error":"company does not exist"})
        serializer = companySerializer(company1)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request, id):
        # pass
        try:
            company1 = company.objects.get(id = id)
        except:
            serialzer = companySerializer(company1, data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)

class invoicesList(APIView):
    
    def get(self, request):
        invoices1 = invoices.objects.all()
        serializer = invoicesSerializer(invoices1, many=True)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request):
        # pass
        # corner case : user 1 access only

        payload = request.data
        list1 = payload['product'].split(',')
        total = len(list1)
        payload['total'] = total
        serialzer = invoicesSerializer(data = payload)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)\

class invoicesListSingle(APIView):
    
    def get(self, request, id):
        try:
            invoices1 = invoices.objects.get(id = id)
        except:
            return Response({"error":"invoice does not exist"})
        #invoices1 = invoices.objects.all()
        serializer = invoicesSerializer(invoices1)
        return Response(serializer.data)
        # return HttpResponse("hi there")

    def post(self,request, id):
        # pass
        # company1 = company.objects.get(id = id)
        # serialzer = companySerializer(company1, data = request.data)
        User = employees.objects.get(id = 1)
        company = User.company

        try:
            invoices1 = invoices.objects.get(id = id)
        except:
            return Response({"error":"invoice does not exist"})

        if invoices1.seller != company and invoices1.buyer != company:
            return Response({"error":"user not authenticated"})

        payload = request.data

        if 'seller' in payload:
            return Response({"error":"user not authenticated for updating this field"})

        if 'total' in payload:
            return Response({"error":"user not authenticated for updating total cost"})

        if 'product' in payload:
            list1 = payload['product'].split(',')
            new_total = len(list1)
            payload['total'] = new_total

        serialzer = invoicesSerializer(invoices1, data = payload, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)