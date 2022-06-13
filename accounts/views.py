from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import CreateView

from accounts.forms import PatientSignupForm, DoctorSignupForm, BlogForm, CategoryForm
from accounts.models import User, Patient, Doctor, Blog, Category


def register(request):
    return render(request, 'register.html')


def doctorview_profile(request):
    context = {
        'user': request.user

    }
    return render(request, 'doctorhomepage.html', context)


def patientview_profile(request):
    context = {
        'user': request.user

    }
    return render(request, 'patienthomepage.html', context)


def patient_register(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('patientview_profile')
    else:
        form = PatientSignupForm()

    return render(request, 'patient_register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('doctorview_profile')
    else:
        form = DoctorSignupForm()

    return render(request, 'doctor_register.html', {'form': form})


def category(request):
    context = {}
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            slug = form.cleaned_data.get("slug")
            cat = Category.objects.create(
                name=name,
                slug=slug

            )
            cat.save()
    else:
        form = CategoryForm()
    context['form'] = form

    return render(request, 'category.html', context)


def blog(request):
    context = {}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            summary = form.cleaned_data.get("summary")
            content = form.cleaned_data.get("content")
            categ = form.cleaned_data.get("categ")
            draft = form.cleaned_data.get("draft")

            obj = Blog.objects.create(
                title=title,
                image=image,
                summary=summary, content=content, categ=categ, draft=draft

            )
            obj.save()
    else:
        form = BlogForm()
    context['form'] = form
    return render(request, "sample.html", context)


def post_view(request):
    obj1 = Blog.objects.all()

    return render(request, 'viewpost.html', {'obj1': obj1})


def home(request, c_slug=None):
    c_page = None
    obj1 = None
    if c_slug != None:

        c_page = get_object_or_404(Category, slug=c_slug)
        obj1 = Blog.objects.filter(categ=c_page, draft=False)
    else:
        obj1 = Blog.objects.all().filter(draft=False)
    abc = Category.objects.all()

    return render(request, 'postlisting.html', {'obj1': obj1, 'ct': abc})
