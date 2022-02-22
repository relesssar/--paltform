from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import catalogmoc
from django.template import loader

def index(request):
    ##return HttpResponse("Hello, world. You're at the polls index.")
    get_moc = catalogmoc.objects.order_by('id')
    template = loader.get_template('catalog_mooc/index.html')
    context = {
        'get_moc': get_moc,
    }
    ##return HttpResponse(template.render(context, request))
    return render(request, 'catalog_mooc/index.html', context)
