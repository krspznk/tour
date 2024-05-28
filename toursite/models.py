from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib.auth.models import User



class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Transpont(models.Model):
    id = models.AutoField(primary_key=True)
    TRANSPORT_CHOICES = [
        ('BUS', 'Автобус'),
        ('TRAIN', 'Поїзд'),
    ]
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures_transpont')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals_transpont')
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    cost = models.IntegerField()
    transport_image = models.CharField(max_length=50, null=True)
    slug = models.SlugField(db_index=True, unique=True, editable=False, default='')  
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерувати slug, тільки якщо він не встановлений
            slug = slugify(f"{self.transport_type}-{self.departure_city}-{self.arrival_city}")
            unique_slug = slug
            counter = 1
            while Transpont.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.departure_city} to {self.arrival_city} - {self.get_transport_type_display()}"
    

    

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    address = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=2000)
    cost = models.IntegerField()
    hotel_image = models.CharField(max_length=50, null=True)
    slug = models.SlugField(db_index=True, unique=True, editable=False, default='') 
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.hotel_name))
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.hotel_name

class Excursion(models.Model):
    id = models.AutoField(primary_key=True)
    excursion_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='excursions')
    description = models.CharField(max_length=2000)
    cost = models.IntegerField()
    excursion_image = models.CharField(max_length=50, null=True)
    slug = models.SlugField(db_index=True, unique=True, editable=False, default='')  
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.excursion_name))
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.excursion_name


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    tour_name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    transport = models.ForeignKey(Transpont, on_delete=models.CASCADE, related_name='tours')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='tours')
    num_days = models.IntegerField()
    excursions = models.ManyToManyField(Excursion, related_name="tours")
    cost = models.IntegerField(default=0) 
    tour_image = models.CharField(max_length=50, null=True)
    slug = models.SlugField(db_index=True, unique=True, editable=False, default='')  # Not editable in admin
    def calculate_cost(self):
        total_cost = self.hotel.cost * self.num_days + self.transport.cost 
        for excursion in self.excursions.all():
            total_cost += excursion.cost
        return total_cost * 0.9
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.tour_name))
        super().save(*args, **kwargs)  # Save the instance first
        self.cost = self.calculate_cost()  # Now calculate the cost
        super().save(*args, **kwargs)  # Save again to update the cost
        self.excursions.set(self.excursions.all()) 

    def __str__(self):
        return self.tour_name


class TourOrder(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('PROCESSED', 'Processed'),
        ('COMPLETED', 'Completed'),
    ]
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_orders')
    start_date = models.DateField()
    num_people = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tour_orders_user', null = True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    final_cost = models.IntegerField()

    def calculate_cost(self):
        return self.tour.cost * self.num_people

    def save(self, *args, **kwargs):
        self.cost = self.calculate_cost()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.tour.tour_name} by {self.user.username}"
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('PROCESSED', 'Processed'),
        ('COMPLETED', 'Completed'),
    ]
    transport = models.ForeignKey(Transpont, on_delete=models.CASCADE, related_name='orders')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='orders')
    excursions = models.ManyToManyField(Excursion, related_name="orders")
    start_date = models.DateField()
    end_date = models.DateField()
    num_people = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_user', null = True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    final_cost = models.IntegerField()
    
    def calculate_cost(self):
        total_days = (self.end_date - self.start_date).days
        total_cost = self.hotel.cost * total_days + self.transport.cost
        for excursion in self.excursions.all():
            total_cost += excursion.cost
        return total_cost 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        self.excursions.set(self.excursions.all())

    def __str__(self):
        return f"Order for {self.transport} and {self.hotel} by {self.user.username}"

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('DONE', 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_user', null = True)
    question_text = models.CharField(max_length=200)
    reply_status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Question from {self.user.username}: {self.question_text}"
