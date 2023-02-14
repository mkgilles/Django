from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Customer, Product, Sale, Cashier
from django import forms
from .models import Cart


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'boarding_pass', 'email']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'product', 'quantity', 'total_price']


class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['first_name', 'last_name', 'username', 'password']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity', 'product', 'price']
        widgets = {
            'product': forms.TextInput(attrs={'readonly': True}),
            'price': forms.NumberInput(attrs={'readonly': True}),
        }


class CashierLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Cashier
        fields = ['username', 'password']
