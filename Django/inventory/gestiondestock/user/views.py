from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from user.forms import CreateUserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'user/register.html', context )
