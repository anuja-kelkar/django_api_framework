from django.http import JsonResponse

def app_status(request):
    return JsonResponse({
        'status_code': 200
    }, status=200)