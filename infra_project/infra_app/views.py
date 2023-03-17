from django.http import HttpResponse


def index(request):
    return HttpResponse('С ума сойти, неужто получилось!', status=200)


def second_page(request):
    return HttpResponse('А это вторая страница!', status=200)
