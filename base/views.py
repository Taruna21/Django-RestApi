from django.shortcuts import render , redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from . models import Advocate ,Company
from .serializers import AdvocateSerializer , CompanySerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class EndpointsView(APIView):
    def get(self, request):
        data = ['/advocates', 'advocates/:username']
        return Response(data)

class AdvocateListView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query))        
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    def post(self, request):
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

class AdvocateDetailsView(APIView):
    def get(self, request, username):
        try:
            advocate = Advocate.objects.get(username=username)
            serializer = AdvocateSerializer(advocate, many=False)
            return Response(serializer.data)
        except Advocate.DoesNotExist:
            return Response({"error": "Advocate not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data) 

    def delete(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.delete()
        return Response('user was deleted')

class CompanyListView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
