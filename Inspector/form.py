from django import forms
from .models import Fir

class FirForm(forms.ModelForm):
    class Meta:
        model = Fir
        fields = ('Name', 'Address','City','State','Pincode','Addhar','Img','Firdescription','Date','Time')
        
        # widgets = {
        #     'Name': forms.TextInput(attrs={'class':'form-control form-group'})
        # }