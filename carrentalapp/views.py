from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarRental, CarReturn
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import CarRentalForm, CarReturnForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from collections import defaultdict
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

def test_view(request):
    return HttpResponse("Django is working!")


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'carrentalapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'carrentalapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    return render(request, 'profile.html') 

# Home Page
def home(request):
    return render(request, 'home.html')

# View to display car log history
@login_required
def car_log_history(request):
    car_rentals = CarRental.objects.all().order_by('car_date')

    # Group car logs by date
    grouped_logs = defaultdict(list)
    for car in car_rentals:
        car_date = car.car_date.strftime('%Y-%m-%d')  # Format date to group by day
        grouped_logs[car_date].append(car)

    # Pass grouped logs to the template
    return render(request, 'car_log_history.html', {'grouped_logs': grouped_logs})

# Custom decorator to check if the user is a staff member
def staff_member_required(function):
    """
    Decorator to ensure the user is a staff member.
    If not, redirects to the home page.
    """
    def wrap(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')  # Redirect to home (or any URL you choose)
        return function(request, *args, **kwargs)
    return wrap
@login_required
@staff_member_required  # This ensures only staff can access this view
def custom_admin(request):
    return render(request, 'custom_admin/base.html')


# View for displaying the car logs (restricted to staff members)
@login_required
@staff_member_required  # This ensures only staff can access this view
def car_log_history(request):
    car_rentals = CarRental.objects.all().order_by('car_date')
    return render(request, 'custom_admin/car_log_history.html', {'car_rentals': car_rentals})

# View for creating a new car log (restricted to staff members)
@login_required
@staff_member_required
def car_log_create(request):
    if request.method == 'POST':
        form = CarRentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_log_history')
    else:
        form = CarRentalForm()
    return render(request, 'custom_admin/car_log_form.html', {'form': form})

# View for editing an existing car log (restricted to staff members)
@login_required
@staff_member_required
def car_log_edit(request, pk):
    car = CarRental.objects.get(pk=pk)
    if not car:
        raise Http404('Car Rental Log not found')
    
    if request.method == 'POST':
        form = CarRentalForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_log_history')
    else:
        form = CarRentalForm(instance=car)
    
    return render(request, 'custom_admin/car_log_form.html', {'form': form})

# View for deleting a car log (restricted to staff members)
@login_required
@staff_member_required
def car_log_delete(request, pk):
    car = CarRental.objects.get(pk=pk)
    if not car:
        raise Http404('Car Rental Log not found')
    
    if request.method == 'POST':
        car.delete()
        return redirect('car_log_history')
    
    return render(request, 'custom_admin/car_log_confirm_delete.html', {'car': car})

@login_required
def rent_car(request):
    if request.method == 'POST':
        form = CarRentalForm(request.POST, request.FILES)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.save()
            return redirect('home')
    else:
        form = CarRentalForm()
    return render(request, 'rent_car.html', {'form': form})

@login_required
def return_car(request):
    if request.method == 'POST':
        form = CarReturnForm(request.POST, request.FILES)
        if form.is_valid():
            rental_id = request.POST['rental_id']
            rental = CarRental.objects.get(id=rental_id, user=request.user)
            car_return = form.save(commit=False)
            car_return.rental = rental
            car_return.save()
            return redirect('home')
    else:
        form = CarReturnForm()
    rentals = CarRental.objects.filter(user=request.user)
    return render(request, 'return_car.html', {'form': form, 'rentals': rentals})
    

