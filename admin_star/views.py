from django.shortcuts import render, redirect
from admin_star.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views
# Create your views here.


def index(request):
  context = {
    'parent': 'dashboard'
  }
  return render(request, 'pages/index.html', context)

def buttons(request):
  context = {
    'parent': 'ui-elements',
    'segment': 'buttons'
  }
  return render(request, 'pages/ui-features/buttons.html', context)

def dropdowns(request):
  context = {
    'parent': 'ui-elements',
    'segment': 'dropdowns'
  }
  return render(request, 'pages/ui-features/dropdowns.html', context)

def typography(request):
  context = {
    'parent': 'ui-elements',
    'segment': 'typography'
  }
  return render(request, 'pages/ui-features/typography.html', context)

def basic_elements(request):
  context = {
    'parent': 'form-elements',
    'segment': 'basic-elements'
  }
  return render(request, 'pages/forms/basic_elements.html', context)

def chartjs(request):
  context = {
    'parent': 'charts',
    'segment': 'chartjs'
  }
  return render(request, 'pages/charts/chartjs.html', context)

def basic_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'basic-table'
  }
  return render(request, 'pages/tables/basic-table.html', context)

def md_icons(request):
  context = {
    'parent': 'icons',
    'segment': 'md-icons'
  }
  return render(request, 'pages/icons/mdi.html', context)


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')