from django import forms
from .models import blog,feedback

class blog_form(forms.ModelForm):

    class Meta:
        model = blog
        fields = "__all__"

class feedback_form(forms.ModelForm):

    class Meta:
        model = feedback
        fields = "__all__"


