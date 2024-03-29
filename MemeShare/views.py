from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.template import Context
from core import *
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    return HttpResponse("Hello cloud9")

def test(request):
    t=get_template('memegroups.html')
    html=t.render(Context({}))
    return HttpResponse(html)

def home(request):
    html=get_template('index.html').render(Context({}))
    return HttpResponse(html)
@csrf_exempt
def login(request):
    if (request.POST and 'username' in request.POST):
        user_id=request.POST['username']
    else:
        user_id=''
    html=get_template('memegroups.html').render(Context({}))
    response=HttpResponse(html)
    response.set_cookie('uuid',user_id)
    return response

def route_add_user_to_memegroup(request):
    user_id=request.GET['uuid']
    group_id=request.GET['group_id']
    return HttpResponse(add_user_to_memegroup(user_id, group_id))  

def route_create_memegroup(request):
    uuid=request.COOKIES['uuid'] #cookie
    name=request.GET['name']
    group_id=create_memegroup(name)
    add_user_to_memegroup(uuid, group_id)
    return HttpResponse('True')

def route_get_memegroup_memes(request):
    memegroup_id=request.GET['group_id']
    memes=get_memegroup_memes(memegroup_id)
    return HttpResponse(memes)

def route_get_user_memegroups(request):
    uuid=request.COOKIES['uuid']
    memegroups=get_user_memegroups(uuid)
    return HttpResponse(memegroups)





def add_memegroup(request):    
    memegroup_name="floor 4 lol"
    memegroup_id=create_memegroup(memegroup_name)
    return HttpResponse(memegroup_id)
def add_user(request):
    user_id=123
    return HttpResponse(add_user_to_memegroup(user_id, request.GET['lol']))

def test_get_user_memegroups(request):
    user_id=123
    return HttpResponse(get_user_memegroups(user_id))



