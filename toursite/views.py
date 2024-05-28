from .models import Tour
from .forms import TourFilterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'toursite/index.html')

def tour_page(request):
    tours = Tour.objects.all()
    form = TourFilterForm(request.GET)
    
    if form.is_valid():
        from_city = form.cleaned_data.get('from_city')
        to_city = form.cleaned_data.get('to_city')
        num_days = form.cleaned_data.get('num_days')
        sort_by_cost = form.cleaned_data.get('sort_by_cost')
        
        if from_city:
            tours = tours.filter(transport__departure_city=from_city)
        if to_city:
            tours = tours.filter(transport__arrival_city=to_city)
        if num_days:
            tours = tours.filter(num_days=num_days)
        
        if sort_by_cost == 'asc':
            tours = tours.order_by('cost')
        elif sort_by_cost == 'desc':
            tours = tours.order_by('-cost')
    
    context = {
        'tours': tours,
        'form': form
    }
    return render(request, 'toursite/tourpage.html', context)

def tour_details(request, slug):
    needed_tour = get_object_or_404(Tour, slug=slug)
    return render(request, 'toursite/tourdetail.html', {
        "tour": needed_tour
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
  
  
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'toursite/register.html', {'form': form, 'title':'register here'})
  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

def Login(request):
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            if user.is_authenticated:  # Check if the user is authenticated
                return redirect('user_profile')  # Redirect to user profile page
            else:
                return redirect('index')  # If somehow not authenticated, redirect to index
        else:
            messages.info(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'toursite/login.html', {'form': form, 'title': 'Log in'})


from .models import TourOrder
from .forms import TourOrderForm
def tour_order(request, slug):
    tour = Tour.objects.get(slug=slug)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        num_people = request.POST.get('num_people')
        if start_date and num_people:
            order = TourOrder.objects.create(
                tour=tour,
                start_date=start_date,
                num_people=num_people,
                user=request.user,
                status='NEW',
                final_cost=tour.cost * int(num_people)
            )
            order.save()
            return redirect('success')  # Redirect to success page after successful order
    else:
        form = TourOrderForm()
    return render(request, 'toursite/tourorder.html', {'form': form, 'tour': tour})


def success(request):
    return render(request, 'toursite/success.html')


from .models import Hotel
from .forms import HotelFilterForm
from .models import Transpont

def hotel_page(request):
    hotel = Hotel.objects.all()
    form = HotelFilterForm(request.GET)



    transport_slug = request.GET.get('transport_slug')
    if transport_slug:
        request.session['selected_transport'] = transport_slug
    
    selected_transport = request.session.get('selected_transport')
    needed_transport = Transpont.objects.get(slug=selected_transport)
    hotel = hotel.filter(city=needed_transport.arrival_city)
    if form.is_valid():
        sort_by = form.cleaned_data.get('sort_by')
        
        if sort_by == 'p_asc':
            hotel = hotel.order_by('cost')
        elif sort_by == 'p_desc':
            hotel = hotel.order_by('-cost')
        elif sort_by == 'r_asc':
            hotel = hotel.order_by('rating')
        elif sort_by == 'r_desc':
            hotel = hotel.order_by('-rating')
    
    context = {
        'hotels': hotel,
        'form': form, 
        "transport": needed_transport
    }
    return render(request, 'toursite/hotelpage.html', context)


def hotel_details(request, slug):
    needed_hotel = get_object_or_404(Hotel, slug=slug)
    return render(request, 'toursite/hoteldetail.html', {
        "hotel": needed_hotel
    })


from .models import Transpont
from .forms import TranspontFilterForm
def transport_page(request):
    transport = Transpont.objects.all()
    form = TranspontFilterForm(request.GET)
    
    if form.is_valid():
        from_city = form.cleaned_data.get('from_city')
        to_city = form.cleaned_data.get('to_city')
        sort_by_cost = form.cleaned_data.get('sort_by_cost')
        sort_by_trans = form.cleaned_data.get('sort_by_trans')
        if from_city:
            transport = transport.filter(transport__departure_city=from_city)
        if to_city:
            transport = transport.filter(transport__arrival_city=to_city)
        
        if sort_by_cost == 'asc':
            transport = transport.order_by('cost')
        elif sort_by_cost == 'desc':
            transport = transport.order_by('-cost')

        if sort_by_trans:
            transport = transport.filter(transport_type=sort_by_trans)
    
    context = {
        'transports': transport,
        'form': form
    }
    return render(request, 'toursite/transportpage.html', context)



from .models import Excursion
from .forms import ExcursionFilterForm
def excursion_page(request):
    excursion = Excursion.objects.all()
    form = ExcursionFilterForm(request.GET)

    selected_transport = request.session.get('selected_transport')
    needed_transport = Transpont.objects.get(slug=selected_transport)
    excursion = excursion.filter(city=needed_transport.arrival_city)

    hotel_slug = request.GET.get('hotel_slug')
    if hotel_slug:
        request.session['selected_hotel'] = hotel_slug
    selected_hotel = request.session.get('selected_hotel')
    needed_hotel = Hotel.objects.get(slug=selected_hotel)

    selected_excursion_list = request.session.get('selected_excursion_list', [])
    excursion_slug = request.GET.get('excursion_slug')
    if excursion_slug:
        selected_excursion_list.append(excursion_slug)
        request.session['selected_excursion_list'] = selected_excursion_list
        
    needed_excursions = Excursion.objects.filter(slug__in=selected_excursion_list)
    print(needed_excursions)
    if form.is_valid():
        sort_by_cost = form.cleaned_data.get('sort_by')
        if sort_by_cost == 'asc':
            excursion = excursion.order_by('cost')
        elif sort_by_cost == 'desc':
            excursion = excursion.order_by('-cost')
    context = {
        'excursions': excursion,
        'form': form, 
        'transport': needed_transport,
        'hotel': needed_hotel,
        'user_excursion': needed_excursions
    }
    return render(request, 'toursite/excursionpage.html', context)

def excursion_details(request, slug):
    needed_excursion = get_object_or_404(Excursion, slug=slug)
    return render(request, 'toursite/excursiondetail.html', {
        "excursion": needed_excursion
    })

from .models import Order
from .forms import OrderForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    if not request.user.is_authenticated:
         return redirect('login')
    selected_transport = request.session.get('selected_transport')
    needed_transport = Transpont.objects.get(slug=selected_transport)
    selected_hotel = request.session.get('selected_hotel')
    needed_hotel = Hotel.objects.get(slug=selected_hotel)
    selected_excursion_list = request.session.get('selected_excursion_list', [])
    excursion_slug = request.GET.get('excursion_slug')
    if excursion_slug:
        selected_excursion_list.append(excursion_slug)
        request.session['selected_excursion_list'] = selected_excursion_list
        
    needed_excursions = Excursion.objects.filter(slug__in=selected_excursion_list)
    excursion_cost = sum(exc.cost for exc in needed_excursions)

    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        num_people = int(request.POST.get('num_people'))

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        total_days = (end_date - start_date).days

        if start_date and end_date and num_people:
            final_cost = ((needed_hotel.cost * total_days) + needed_transport.cost + excursion_cost) * num_people

            order = Order.objects.create(
                hotel=needed_hotel,
                transport=needed_transport,
                start_date=start_date,
                end_date=end_date,
                num_people=num_people,
                user=request.user,
                status='NEW',
                final_cost=final_cost
            )
            request.session.clear()
            order.excursions.set(needed_excursions)

            return redirect('success') 
    else:
        form = OrderForm()

    return render(request, 'toursite/order.html', {'form': form, 'transport': needed_transport, 'hotel': needed_hotel, 'excursions': needed_excursions, "excursion_cost": excursion_cost})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout

@login_required
def user_profile(request):
    user = request.user
    tour_orders = TourOrder.objects.filter(user=user)
    orders = Order.objects.filter(user=user)
    return render(request, 'toursite/user_profile.html', {'user': user, 'tour_orders': tour_orders, 'orders': orders})


def logout_user(request):
    logout(request)
    return redirect('index')


from django.shortcuts import render, redirect
from .models import Order, TourOrder

@login_required
def orders_view(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')
        if order_id and status:
            if Order.objects.filter(id=order_id).exists():  
                order = Order.objects.get(id=order_id)
            else:
                order = TourOrder.objects.get(id=order_id)
            order.status = status
            order.save()
            return redirect('orders')
    
    orders = Order.objects.all()
    tour_orders = TourOrder.objects.all()
    return render(request, 'toursite/orders.html', {'orders': orders, 'tour_orders': tour_orders})

@login_required
def all_services_view(request):
    transports = Transpont.objects.all()
    tours = Tour.objects.all()
    hotels = Hotel.objects.all()
    excursions = Excursion.objects.all()
    
    return render(request, 'toursite/all_services.html', {'transports': transports, 'tours': tours, 'hotels': hotels, 'excursions': excursions})


@login_required
def delete_transport_view(request, transport_id):
    transport = get_object_or_404(Transpont, id=transport_id)
    transport.delete()
    return redirect('all_services')

@login_required
def delete_hotel_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    hotel.delete()
    return redirect('all_services')

@login_required
def delete_excursion_view(request, excursion_id):
    excursion = get_object_or_404(Excursion, id=excursion_id)
    excursion.delete()
    return redirect('all_services')

@login_required
def delete_tour_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    tour.delete()
    return redirect('all_services')


# views.py

from django.shortcuts import render, redirect
from .forms import TransportForm

def add_transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_services')  
    else:
        form = TransportForm()
    return render(request, 'toursite/add_transport.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import HotelForm

def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        form = HotelForm()
    return render(request, 'toursite/add_hotel.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import ExcursionForm

def add_excursion(request):
    if request.method == 'POST':
        form = ExcursionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        form = ExcursionForm()
    return render(request, 'toursite/add_excursion.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import TourForm

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        form = TourForm()
    return render(request, 'toursite/add_tour.html', {'form': form})



from rest_framework import viewsets
from .models import City, Transpont, Hotel, Excursion, Tour, TourOrder, Order, Question
from .serializers import CitySerializer, TranspontSerializer, HotelSerializer, ExcursionSerializer, TourSerializer, TourOrderSerializer, OrderSerializer, QuestionSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class TranspontViewSet(viewsets.ModelViewSet):
    queryset = Transpont.objects.all()
    serializer_class = TranspontSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourOrderViewSet(viewsets.ModelViewSet):
    queryset = TourOrder.objects.all()
    serializer_class = TourOrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

from django.shortcuts import render
import requests

def data_table(request):
    orders_response = requests.get('http://localhost:8000/api/orders/')
    hotels_response = requests.get('http://localhost:8000/api/hotels/')
    excursions_response = requests.get('http://localhost:8000/api/excursions/')
    transport_response = requests.get('http://localhost:8000/api/transponts/')
    
    if orders_response.status_code != 200 or hotels_response.status_code != 200 or excursions_response.status_code != 200:
        return render(request, 'error.html', {'error_message': 'Failed to fetch data from API.'})

    orders = orders_response.json()
    hotels = hotels_response.json()
    excursions = excursions_response.json()
    transports = transport_response.json()

    hotel_dict = {hotel['id']: hotel for hotel in hotels}
    excursion_dict = {excursion['id']: excursion for excursion in excursions}
    transport_dict = {transport['id']: transport for transport in transports}

    for order in orders:
        order['hotel_name'] = hotel_dict[order['hotel']]['hotel_name'] if order['hotel'] in hotel_dict else None
        order['transport_type'] = transport_dict[order['transport']]['transport_type'] if order['transport'] in transport_dict else None
        order['excursion_names'] = [excursion_dict[excursion_id]['excursion_name'] for excursion_id in order['excursions'] if excursion_id in excursion_dict]

    return render(request, 'toursite/data_table.html', {'orders': orders})
