from django.shortcuts import render, redirect

from MainApp.forms import TopicForm
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
   
def topic(request, topic_id):
    #topic_id has to be consistent with what's in the urls.py file bc that's whats being passed
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    #- indicates descending order

    context = {'topic':topic,'entries':entries}
    #doesn't matter what you name it but it's consistent with what everyone does in django
    #passes objects from the view to the template
    #whatever variable you're using in the html is the key
    #the value is for the view

    return render(request, 'MainApp/topic.html', context)
    #context is a dictionary object

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()
            #form.save automatically saves the data to the database
            #if you define custom fields that aren't in the model you have to do the objects.insert and querying to be able to save it to the database
            return redirect('MainApp:topics')
            #takes them to the main topics page

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)
