from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Full Name'
        }
        
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# Note:- We are creating fields like 'first_name', 'email', so the User Model
# will be having these fields and its data. We have created Signals,
# if any new user is created, their profile will be automatically created.
# So in signals.py file, we have defiend the fields and how to fetch data,
# from User model, in the createProfile function.
        