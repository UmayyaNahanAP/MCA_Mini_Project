from django.shortcuts import render,redirect
from officer.models import Scheme,Complaint
from vayal_user.models import Vayal_User


def get_as_three_digit(number):
    if number > 99:
        return f'{number}'
    elif number > 9:
        return f'0{number}'
    return f'00{number}'

def index(request):
    scheme_count = get_as_three_digit(Scheme.objects.count())
    vayal_user_count = get_as_three_digit(Vayal_User.objects.count())
    complaint_count = get_as_three_digit(Complaint.objects.count())
    scheme_analytics = {}
    for scheme in Scheme.objects.all():
        if scheme.cast_eligibility in scheme_analytics:
           scheme_analytics[scheme.cast_eligibility] += 1
        else:
            scheme_analytics[scheme.cast_eligibility] = 1
    context = {
        'scheme_count': scheme_count, 
        'vayal_user_count': vayal_user_count, 
        'complaint_count': complaint_count, 
        'scheme_analytics': scheme_analytics,
    }
    return render(request,'officer/home/index.html', context)

def users(request):
    vayal_user= Vayal_User.objects.all().order_by('-id')
    