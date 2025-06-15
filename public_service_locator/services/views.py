from django.shortcuts import render
from django.contrib.auth import authenticate, login

# basic login/registration
def register(request):
  if request.method == 'POST':
    role = request.POST['role'] # the roles are: 'general', 'provider', 'admin'
    user = UserFactory().create_user(role, request.POST['username'], request.POST['password'])
    login(request, user)
