
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
  
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
    
        subject = "Welcome to DevSearch"
        message = "We are glad you are here..."
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
        
    
# post_save.connect(profileUpdated, sender = Profile)
# post_delete.connect(deleteUser, sender = Profile)

@receiver(post_save, sender = Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()