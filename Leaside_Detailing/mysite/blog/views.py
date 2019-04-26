from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Contact
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    my_dict = {'insert_me':"Hello I am from views.py!"}
    return render(request,'blog/index.html',context=my_dict)

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request, template_name="blog:contact",
                            context={"Contact": Contact.objects.all})

def events(request):
    return render(request,'blog/events.html')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            registered = True
            login(request, user)
            return redirect("blog:index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserForm
    return render(request,'blog/register.html',
                            context={"form":form})



def services(request):
    return render(request,'blog/services.html')

def single(request):
    return render(request,'blog/single.html')

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'blog/login.html', {})
