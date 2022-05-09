from django import forms
# from django.contrib.auth import get_user_model
from .models import Lead
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            'description',
            'phone_number',
            'email',
            
        )

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        return data

    def clean(self):
        pass
        # first_name = self.cleaned_data["first_name"]
        # last_name = self.cleaned_data["last_name"]
        # if first_name + last_name != "Joe Soap":
        #     raise ValidationError("Your name is not Joe Soap")


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class NewUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1' , 'password2']

        def __init__(self , *args,**kwargs):

            super(NewUserCreationForm,self).__init__(*args , **kwargs)

            for name , field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})
