from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bem-vindo ao meu primeiro projeto Django!")