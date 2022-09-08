from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse

def home(request):
    return render(request,'homes.html')

