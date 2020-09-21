from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from AppTwo.models import Users, ProjectIdea
from AppTwo.forms import LoginForm, RegisterForm, ContactForm, SignUpForm, ProjectsForm

# Create your views here.


def index(request):
    my_dict = {'home': "Welcome to the home page!"}
    return render(request, 'AppTwo/index.html', my_dict)


def Help(request):
    my_dict = {'contact': "Get in contact!"}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request):
    user_list = Users.objects.all()
    user_dict = {'Activate_Users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)

def sign_up_modelform(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('Error: Invalid Form')

    return render(request, 'AppTwo/sign_up.html', {'form': form})


def submitted_projects(request):
    proj_list = ProjectIdea.objects.all()
    proj_dict = {'projects': proj_list}
    return render(request, 'AppTwo/submitted_projects.html', context=proj_dict)


def project_model_form(request):
    form = ProjectsForm

    if request.method == 'POST':
        form = ProjectsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return submitted_projects(request)
        else:
            print('Invalid Form')

    return render(request, 'AppTwo/project_ideas.html', {'form': form})


# def project_idea_form(request):
#     form = ProjectIdeaForm
#
#     if request.method == 'POST':
#
#         form = ProjectIdeaForm(request.POST)
#
#         if form.is_valid():
#             print('Validation Success')
#             print('First Name: '+form.cleaned_data['First_Name'])
#             print('Last Name: '+form.cleaned_data['Last_Name'])
#             print('Email: '+form.cleaned_data['Email'])
#             print('Project Category: '+form.cleaned_data['Project_Category'])
#             print('Project Name: '+form.cleaned_data['Project_Name'])
#             print('Project Description: '+form.cleaned_data['Proj_Description'])
#
#     return render(request, 'AppTwo/project_ideas.html', {'form': form})


def login_form(request):
    form = LoginForm

    return render(request, 'AppTwo/login.html', {'form': form})


def register_form(request):
    form = RegisterForm

    if request.method == 'POST':

        form = RegisterForm(request.POST)

    return render(request, 'AppTwo/register.html', {'form': form})


def contact_form(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise forms.ValidationError('Error: Invalid inputs, please review the form')

    return render(request, 'AppTwo/contact.html', {'form': form})



