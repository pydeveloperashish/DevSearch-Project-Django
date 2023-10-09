
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

  
@receiver(post_save, sender = Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Saved")
    print("Instance: %s" % instance)
    print("Created: %s" % created)
    
    
@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, **kwargs):
    print("Deleted User...")
    print("Instance: %s" % instance)


# Automatically create a profile when a new user is created...
@receiver(post_save, sender = User)
def createProfile(sender, instance, created, **kwargs):
    print("New Profile created")
    if created:
        user = instance
        profile = Profile.objects.create(user = user, 
                                         username = user.username,
                                         name = user.first_name, 
                                         email = user.email)
    
    
# post_save.connect(profileUpdated, sender = Profile)
# post_delete.connect(deleteUser, sender = Profile)