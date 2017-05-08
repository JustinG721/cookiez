from django.contrib.auth.models import User
from django import forms

class AddCartForm(forms.Form):
    addcart = forms.IntegerField()
    print("THIS IS THE nice CART nice boy!!" + str(addcart))

'''
class UserForm(forms.modelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
'''