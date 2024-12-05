from django.http import JsonResponse
from django.shortcuts import render
# from rest_framework

def index(request):
    d = {
        'f': 1,
        'g': 2
    }

    return JsonResponse(d)


def send_message(request):
    data = request
    print(data)
    # send_sms()
