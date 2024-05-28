from django import forms
from .models import City
from .models import Transpont, Excursion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

from django import forms
from .models import TourOrder

class TourOrderForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    num_people = forms.IntegerField(min_value=1) 
    
    class Meta:
        model = TourOrder
        fields = ['start_date', 'num_people']


class OrderForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    num_people = forms.IntegerField(min_value=1) 
    class Meta:
        model = TourOrder
        fields = ['start_date', 'end_date', 'num_people']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class TourFilterForm(forms.Form):
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), label='From City', required=False)
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), label='To City', required=False)
    num_days = forms.IntegerField(label='Number of Days', min_value=1, required=False)
    SORT_CHOICES = [
        ('', 'None'),
        ('asc', 'Lowest to Highest'),
        ('desc', 'Highest to Lowest'),
    ]
    sort_by_cost = forms.ChoiceField(choices=SORT_CHOICES, label='Sort by Cost', required=False)


class HotelFilterForm(forms.Form):
    SORT_CHOICES = [
        ('', 'None'),
        ('p_asc', 'Price: Lowest to Highest'),
        ('p_desc', 'Price: Highest to Lowest'),
        ('r_asc', 'Rating: Lowest to Highest'),
        ('r_desc', 'Rating: Highest to Lowest'),
    ]
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, label='Sort by', required=False)


class TranspontFilterForm(forms.Form):
    from_city = forms.ModelChoiceField(queryset=Transpont.objects.all(), label='From City', required=False)
    to_city = forms.ModelChoiceField(queryset=Transpont.objects.all(), label='To City', required=False)
    SORT_TRANS = [
        ('', 'None'),
        ('BUS', 'Автобус'),
        ('TRAIN', 'Поїзд'),
    ]
    sort_by_trans = forms.ChoiceField(choices=SORT_TRANS, label='Sort by Transport', required=False)
    SORT_CHOICES = [
        ('', 'None'),
        ('asc', 'Lowest to Highest'),
        ('desc', 'Highest to Lowest'),
    ]
    sort_by_cost = forms.ChoiceField(choices=SORT_CHOICES, label='Sort by Cost', required=False)


class ExcursionFilterForm(forms.Form):
    SORT_CHOICES = [
        ('', 'None'),
        ('asc', 'Price: Lowest to Highest'),
        ('desc', 'Price: Highest to Lowest'),
    ]
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, label='Sort by', required=False)


# forms.py

from django import forms

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transpont
        fields = ['departure_city', 'arrival_city', 'transport_type', 'cost', 'transport_image']

# forms.py
from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'city', 'address', 'rating', 'description', 'cost', 'hotel_image']

# forms.py
from django import forms
from .models import Excursion

class ExcursionForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = ['excursion_name', 'city', 'description', 'cost', 'excursion_image']

# forms.py
from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['tour_name', 'description', 'transport', 'hotel', 'num_days', 'excursions', 'tour_image']
