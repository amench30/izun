from django.db import models



class Users(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    
    
    def __unicode__(self):
        return self.email
