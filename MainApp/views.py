from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')
    
def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics}
    #we have a key and a vlue here
    #whatever you use the key as, the html template needs to refer to that
    #the value is what you use in the view file
    
    return render(request,'MainApp/topics.html', context)
   