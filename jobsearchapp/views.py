from django.shortcuts import render
# -- coding: utf-8 --
# from _future_ import unicode_literals
import re
import csv
import sys
from django.shortcuts import render, HttpResponse, redirect
from importlib import reload
#from .forms import Searchform
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Jobs
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt;
import io
from django.http import HttpResponse
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def Loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            logger.info('login successful')
            return redirect('home')

        else:
            logger.info('invalid credentials')
            return render(request,'login.html')

    else:
        logger.info('user login failed')
        return render(request,'login.html')

def Homeview(request):
    logger.info('login successful')
    return render(request,'home.html')

def ResultsView(request):
    logger.info('search successful showing results')
    dataframe = pd.read_csv('indeed1.csv', index_col=0)
    #df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.bar(dataframe.index, dataframe['Count'])
    ax.set_xticklabels(dataframe.index, rotation=60, horizontalalignment='right')
    ax.set_ylabel('Number of jobs posted')
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('grayscale')
    plt.savefig('Media/visual.png', bbox_inches='tight')




    #plt.show()

    jobs = Jobs.objects.all()
    return render(request,'results.html',{'jobs': jobs})





def SearchView(request):




    return redirect('results')
