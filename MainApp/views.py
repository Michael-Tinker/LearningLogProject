from cmath import log
from django.shortcuts import render, redirect

from MainApp.forms import EntryForm, TopicForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')

    context = {'topics':topics}
    #we have a key and a vlue here
    #whatever you use the key as, the html template needs to refer to that
    #the value is what you use in the view file
    
    return render(request,'MainApp/topics.html', context)

@login_required   
def topic(request, topic_id):
    #topic_id has to be consistent with what's in the urls.py file bc that's whats being passed
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    #- indicates descending order

    context = {'topic':topic,'entries':entries}
    #doesn't matter what you name it but it's consistent with what everyone does in django
    #passes objects from the view to the template
    #whatever variable you're using in the html is the key
    #the value is for the view

    return render(request, 'MainApp/topic.html', context)
    #context is a dictionary object

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #form.save automatically saves the data to the database
            #if you define custom fields that aren't in the model you have to do the objects.insert and querying to be able to save it to the database
            return redirect('MainApp:topics')
            #takes them to the main topics page

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    #topic_id is definedi n the url so it needs to be defined here as well
    topic = Topic.objects.get(id=topic_id)
    #Uppercase T topic because it imports it form .models at the top of this file
    #lower case tpoic is just a variable name
    
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id)


    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #gives us the topic object with all attributes attached
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        #LOAD UP That instance of the entry object
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)
                #use topic.id because the topic object has the topic id)
                #only allowed to do that bc its set up as a foreign key to the topic model
                
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'MainApp/edit_entry.html', context)