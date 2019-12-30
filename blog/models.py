from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    #To return title to admin page
    def __str__(self):
        return self.title

    def limit(self):
        return self.body[:100]