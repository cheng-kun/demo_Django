from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    context = {}
    if 'q' in request.GET:
        context['res'] = "\"sucess['" + request.GET['q']+"']\""
    return render(request, 'search_form.html', context)