from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # we can either create a list and mention the fields 
        # we want to allow, or just write __all__ to allow all fields.
        # fields = '__all__'
        fields = ['title', 'description', 'featured_image', 'demo_link', 
                  'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        # self.fields['title'].widget.attrs.update({'class': 'input', 
        #                                           'placeholder': 'Add Title'})
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f"Add {name}"})