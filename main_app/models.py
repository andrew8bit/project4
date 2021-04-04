from django.db import models
from django.urls import reverse
from datetime import date
# thank you Django for this user :-)
from django.contrib.auth.models import User

STATUS = (
    ('M', 'Missing Person'),
    ('T', 'Target'),
)

class Bounty(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(
        max_length=250, 
        default='https://static.wikia.nocookie.net/villains/images/6/61/Unknown_Face_Of_The_Collector.jpg/revision/latest?cb=20171207211806'
        )
    last_seen = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50)
    summary = models.CharField(
        max_length=100,
        default=f"Please help find this missing person"
        )
    status = models.CharField(
        max_length=1,
        choices = STATUS,
        default = STATUS[0][0]
    )
    story = models.CharField(max_length=5000)    

    def __str__(self):
        return f" {self.name} was last seen on {self.last_seen}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return f" {self.title} was created by {self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f" A comment by {self.user} in response to {self.post} "