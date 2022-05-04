from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    #import that it inherents from the model form so that we don't recreate all the fields
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    #import that it inherents from the model form so that we don't recreate all the fields
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}