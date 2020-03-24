from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import LoginForm, RegisterForm, UserProfileForm, UserProfileEdit
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:logout')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form": form, "title": "save"})



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home_app:index')
    return render(request, 'accounts/forms.html', {'form': form, 'title': 'Login'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, email=email, password=password)
        login(request, new_user)
        return redirect('home_app:index')
    return render(request, 'accounts/forms.html', {'form': form, 'title': 'Register'})


def logout_view(request):
    logout(request)
    return redirect('home_app:index')


def user_edit_profile(request):
    data = {'gender': request.user.userprofile.gender,
            'bio': request.user.userprofile.bio,
            'phone_num': request.user.userprofile.phone_num,
            'birth_date': request.user.userprofile.birth_date}
    user_profile_form = UserProfileForm(request.POST or None, instance=request.user, initial=data)

    if request.method == "POST":
        if user_profile_form.is_valid():
            user_profile_form.save(commit=True)

            user_edit_form = UserProfileEdit(data=request.POST, instance=request.user.userprofile)
            user_edit_form.save(commit=True)
            # message = messages.success(request, "Congratulations, your info has been updated...")
            return HttpResponseRedirect(reverse('home_app:index'))

    return render(request, 'accounts/user_edit_profile.html',
                  context={'user_profile_form': user_profile_form, 'title': 'Save'})

