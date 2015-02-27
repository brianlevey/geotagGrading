from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, event_id):
    return HttpResponse("You're looking at question %s." % event_id)
