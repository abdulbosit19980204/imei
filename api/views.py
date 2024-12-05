from django.http import JsonResponse
from django.shortcuts import render
from api.models import CustomUser


# from rest_framework
def index(request):
    user = CustomUser.objects.filter(user=request.user).first()  # Fetch the user instance
    if not user:
        return JsonResponse({'error': 'User not found'}, status=404)

    # Serialize user data
    user_data = {
        "id": user.id,
        "bolim": user.bolim.name,
        "unvonim": user.unvon.name,
        "username": user.user.username,  # Assuming CustomUser has a `username` field
        "ishjoylari": list(user.ishjoylari.values("id", "name"))  # Adjust field names as per your model
    }
    return JsonResponse(user_data)


def send_message(request):
    data = request
    print(data)
    # send_sms()
