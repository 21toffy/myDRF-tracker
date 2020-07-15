from rest_framework import generics

from rest_framework import viewsets
# from rest_framework.response import response

from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view
# from rest_framework import response
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *



from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser 
from rest_framework import status 
from .models import *
from blog.serializers import BlogSerializer


@api_view(['GET', 'POST'])
def blog_collection(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'title': request.data.get('title'), 'content': request.data.get('content')}
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def report(request):
    if request.method == 'GET':
        report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = {'title': request.data.get('title'), 'content': request.data.get('content')}
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report = serializer.save()
            return Response(ReportSerializer(report).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























