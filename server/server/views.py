from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

# Redirecting
def Home(req):
    return redirect('http://localhost:5173/')