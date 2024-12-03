from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    d = {
        'f': 1,
        'g': 2
    }
    return JsonResponse(d)
