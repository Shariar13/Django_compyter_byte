from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import front_order
from .models import back_order
from .models import fullstack_order
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# class profile(ListView):
#     template_name="profile.html"
#     model=post
#     ordering=['-id']

#     def get_queryset(self):
#         query_set=super().get_queryset()
#         return query_set.select_related

#     def get_context_data(self, *args, **kwargs):
#         context = super(profile, self).get_context_data(*args, **kwargs)
#         context['social_media_account_list'] = social_media_account.objects.all()
#         context['profile_picture_list'] = profile_picture.objects.all()
#         context['doctor_list'] = doctor.objects.all()
#         return context

def home(request):
    return render(request, 'index.html')


class front_end(ListView):
    template_name = "front_end.html"
    model = front_order
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related


class back_end(ListView):
    template_name = "back_end.html"
    model = back_order
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related


class fullstack(ListView):
    template_name = "full_stack.html"
    model = fullstack_order
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related


class browse_project(ListView):
    template_name = "browse_project.html"
    model = front_order
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(browse_project, self).get_context_data(*args, **kwargs)
        context['back_order_database'] = back_order.objects.all()
        context['fullstack_order_database'] = fullstack_order.objects.all()
        return context


def front_end_form(request):
    if request.method == 'POST':
        category = request.POST['category']
        username = request.POST['username']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        quantity = request.POST['quantity']
        details = request.POST['details']
        status = request.POST['status']
        front_end_order_form = front_order(category=category, username=username, name=name,
                                           phone=phone, email=email, address=address, quantity=quantity, details=details, status=status)
        front_end_order_form.save()
        messages.success(
            request, 'Your order is successfully submitted.We will contact you soon.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def back_end_form(request):
    if request.method == 'POST':
        category = request.POST['category']
        username = request.POST['username']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        quantity = request.POST['quantity']
        details = request.POST['details']
        status = request.POST['status']
        back_end_order_form = back_order(category=category, username=username, name=name, phone=phone,
                                         email=email, address=address, quantity=quantity, details=details, status=status)
        back_end_order_form.save()
        messages.success(
            request, 'Your order is successfully submitted.We will contact you soon.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def fullstack_form(request):
    if request.method == 'POST':
        category = request.POST['category']
        username = request.POST['username']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        quantity = request.POST['quantity']
        details = request.POST['details']
        status = request.POST['status']
        fullstack_order_form = fullstack_order(category=category, username=username, name=name,
                                               phone=phone, email=email, address=address, quantity=quantity, details=details, status=status)
        fullstack_order_form.save()
        messages.success(
            request, 'Your order is successfully submitted.We will contact you soon.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Account created successfully')
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'index.html')


def signout(request):
    logout(request)
    return redirect("/")
