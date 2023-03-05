from django.shortcuts import render
from .forms import ActivityForm,LeaveRequestForm
# Create your views here.

def user_profile (request): 
    pass

def user_profile_setting(request):
    pass 

def home (request):
    pass

def new_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LeaveRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render('/NewRequest/')

    # if a GET (or any other method) we'll create a blank form
    else:
        context = LeaveRequestForm()

    return render(request, 'NewRequest.html', {'form': context})

def my_requests (request):
    pass

def new_activity (request):
    pass

def my_activities (request):
    pass
