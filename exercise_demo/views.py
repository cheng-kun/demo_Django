from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    res = {}
    if 'q' in request.GET:
        res['res'] = "\"sucess['" + request.GET['q']+"']\""
    return render(request, 'search_form.html', res)

def api_demo(request):
    res = {}
    if 'q' in request.GET:
        res['res'] = request.GET['q']
    return HttpResponse(res['res'])
    # return JsonResponse({"result":0,"msg":"success"})