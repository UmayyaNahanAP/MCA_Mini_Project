from django.shortcuts import render, redirect
from officer.forms import VegetablePermissionForm

def vegetable_permission_view(request):
    if request.POST:
        form = VegetablePermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vayal_user:home')  # Redirect to a success page or another relevant view
    form = VegetablePermissionForm()
    return render(request, 'vayal_user/vegetable/index.html', {'form': form})
