from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.template import Context
from core import *

def hello(request):
    return HttpResponse("Hello world")

def test(request):
    t=get_template('memegroups.html')
    print(t)
    html=t.render(Context({}))
    return HttpResponse(t)


def add_memegroup(request):
    
    memegroup_name="floor 4 lol"
    memegroup_id=create_memegroup(memegroup_name)
    return HttpResponse(memegroup_id)
def add_user(request):
    user_id=123
    return HttpResponse(add_user_to_memegroup(user_id, request.get['lol']))

def get_user_memegroups(request):
    user_id=123
    return HttpResponse(get_user_memegroups(user_id))
