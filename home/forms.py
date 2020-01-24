from django import forms

class ContactForm(forms.Form):
    """ 
    Form for contact page 
    """
    
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 5,
            },
        ),
    )
    class Meta:
        fields = [
            'name',
            'email',
            'message',
        ]