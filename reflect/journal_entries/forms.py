from django.forms import ModelForm
from . models import JournalEntry

class JournalEntryForm(ModelForm):
    class Meta:
        model = JournalEntry
        fields = ('title', 'content', 'tags', 'mood', 'media')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configure widgets and classes for each field
        self.fields['title'].widget.attrs.update({
            'class': 'input',
            'placeholder': 'Enter title'
        })
        
        self.fields['content'].widget.attrs.update({
            'class': 'textarea',
            'placeholder': "What's on your mind?"
        })
        
        self.fields['tags'].widget.attrs.update({
            'class': 'input',
            'placeholder': 'Enter tags (comma-separated)'
        })
        
        self.fields['mood'].widget.attrs.update({
            'class': 'select'
        })
        
        self.fields['media'].widget.attrs.update({
            'class': 'file-input',
            'accept': 'image/*,video/*'  # Specify accepted file types
        })