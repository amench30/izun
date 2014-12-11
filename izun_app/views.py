from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("izun/index.html", context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("izun/about.html", context_dict, context)

def contact(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("izun/contact.html", context_dict, context)

def blog(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("izun/blog.html", context_dict, context)

def forms(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response("izun/forms.html", context_dict, context)
