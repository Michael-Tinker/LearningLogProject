from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #all user defined topic, text, and date_added
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        #with a str method we can define what to return when someone calls a print statement
        return self.text #+ '-' + str(self.date_added)
            #text is user defined as an attribute (just a word we came up with)
        #if we print(Topic) it would print the text of that topic

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural =  'entries'

    def __str__(self):
        #with a str method we can define what to return when someone calls a print statement
        return f"{self.text[:50]}..."
        #will return the first 50 characters 
        #without this string method you won't be able to see the details