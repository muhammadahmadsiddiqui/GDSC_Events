from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='event_pictures', null=True, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20,default='(000) 000-0000')
    
    def __str__(self):
        return self.name + ', ' + self.email + ', ' + self.phone
