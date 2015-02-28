from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from geoGrading.models import Event


# Create your views here.
def index(request):
    event_list = Event.objects.order_by('event_Id')
    context = {'event_list': event_list}
    return render(request, 'geoGrading/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'geoGrading/detail.html', {'event': event})
