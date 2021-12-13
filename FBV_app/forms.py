from django import forms
from FBV_app.models import User

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('name','email','mob_number','image')
        labels={'mob_number':'Mobile','image':'Upload_Image'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mob_number':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

    