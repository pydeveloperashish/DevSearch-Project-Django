from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # we can either create a list and mention the fields 
        # we want to allow, or just write __all__ to allow all fields.
        # fields = '__all__'
        fields = ['title', 'description', 'featured_image', 'demo_link', 
                  'source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        # self.fields['title'].widget.attrs.update({'class': 'input', 
        #                                           'placeholder': 'Add Title'})
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f"Add {name}"})
            
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
    labels = {
        'value': 'Place your Vote',
        'body': 'Add a Comment with your Vote'
    }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})