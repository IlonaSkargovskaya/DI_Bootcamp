from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy 
from django.contrib import messages
from django.shortcuts import get_object_or_404


def homepage(request):

    context = {
        'title' : 'HOME | TORQUAY'
    }

    return render(request, 'home.html', context)
