from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    #import that it inherents from the model form so that we don't recreate all the fields
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
