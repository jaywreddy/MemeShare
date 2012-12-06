from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def hello(request):
    return HttpResponse("Hello world")

def test(request):
    t=get_template('memegroups.html')
    html=t.render()
    return HttpResponse(html)
