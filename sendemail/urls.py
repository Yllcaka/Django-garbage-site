# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .views import *

urlpatterns = [
    # path('kontakt/', emailView, name='email'),
    path('kontakt/', tripi_me_email, name='email'),
    path('success/', successView, name='success'),
    path('',homepage, name="home"),
    path('internet/',internet,name ="internet"),
    path("telefoni/",telefoni, name="telefoni"),
    path("webdesign/",design,name="design"),
    path("networking",networking,name="networking"),
    path("software/",software,name="software"),
    path("trajnime/",trainime,name="trainime"),
    path("internet_viti/",pdf1,name="internet_viti"),
    path("telefonike_viti/",pdf2,name = "telefonike_viti"),
    path("kontaktim_i_plot",tripi_madh_me_email, name="kontaktim_i_plot"),
    # path("kontakt/",kontakt,name="kontakt")
]