












# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import get_user_model

# Logined_User = get_user_model()
# # Create your views here.


# def login_user(request):
#     if request.POST:
#         try:
#             existing_user_name = Logined_User.objects.get(
#                 email=request.POST['username']).get_username()
#         except Logined_User.DoesNotExist:
#             return render(request, 'registration/login.html', {"form": {'errors': ['invalid username']}})
#         logined_user = authenticate(
#             request, username=existing_user_name, password=request.POST['password'])
#         if logined_user is not None:
#             login(request, logined_user)
#             if logined_user.is_officer:
#                 return redirect('officer:home')
#             return redirect('user:home')
#         else:
#             form = AuthenticationForm(request, request.POST)
#             return render(request, 'registration/login.html', {'form': form})

#     form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})
