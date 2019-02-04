from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    res = {}
    if 'q' in request.GET:
        res['res'] = "\"sucess['" + request.GET['q'] + "']\""
    return render(request, 'search_form.html', res)


def api_demo(request):
    res = ""
    if 'input' in request.GET:
        res = request.GET['input']
    result = "sucess:[" + res + "]"
    # return JsonResponse({"response": result})
    response = HttpResponse(json.dumps(result))
    response["Access-Control-Allow-Origin"] = "*"
    return response