from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'vayal_user/home/index.html')

