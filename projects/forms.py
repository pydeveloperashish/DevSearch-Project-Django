from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # we can either create a list and mention the fields 
        # we want to allow, or just write __all__ to allow all fields.
        # fields = '__all__'
        fields = ['title', 'description', 'demo_link', 
                  'source_link', 'tags']