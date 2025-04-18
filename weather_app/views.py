# views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

API_KEY = "78738b80ee5bd2008874e5ff7b95878b"

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def weather(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city = data.get('city')

            if not city:
                return JsonResponse({"error": "City is required"}, status=400)

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code != 200:
                return JsonResponse({"error": "City not found"}, status=404)

            weather_data = response.json()
            result = {
                "temperature": weather_data["main"]["temp"],
                "description": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"],
                "pressure": weather_data["main"]["pressure"],
                "wind": weather_data["wind"]["speed"]
            }

            return JsonResponse(result)
        except Exception as e:
             return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "POST request required"}, status=405)
