from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #all user defined topic, text, and date_added


    def __str__(self):
        #with a str method we can define what to return when someone calls a print statement
        return self.text
            #text is user defined as an attribute (just a word we came up with)
        #if we print(Topic) it would print the text of that topic

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #with a str method we can define what to return when someone calls a print statement
        return f"{self.text[:50]}..."
        #will return the first 50 characters 
        #without this string method you won't be able to see the details