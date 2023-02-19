from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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


class CashierForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            cashier = Cashier.objects.create(user=user)
            cashier.save()
        return user
        widgets = {
            'password': forms.PasswordInput(),
        }


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


class StaffLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Cashier
        fields = ['username', 'password']
