import re
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})    

def meetingdetail(request, id):
    meetingdetail=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meetingdetail' : meetingdetail})