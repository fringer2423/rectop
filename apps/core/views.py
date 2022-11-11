from django.http import JsonResponse


def ping(request):
    """Контроллер для проверки сервиса"""
    data = {
        'ping': 'pong!'
    }
    return JsonResponse(data)
