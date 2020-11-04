from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.predict import predict

# your views, in C# - controler
# views in c# - templates in django


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context))


def accept_view(request):
    # request must be post
    result = predict(request.data)
    template = loader.get_template('accept.html')
    context = {
        'result': result,
    }
    return HttpResponse(template.render(context))
