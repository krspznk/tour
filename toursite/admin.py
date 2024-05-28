from django.contrib import admin
from .models import City, Hotel, Transpont, Excursion, Order, TourOrder, Tour, Question


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'city_id', 'rating')

class TranspontAdmin(admin.ModelAdmin):
    list_display = ('departure_city', 'arrival_city', 'transport_type', 'cost')

class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('excursion_name', 'city_id', 'cost')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('start_date','user', 'status')

class TourOrderAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'tour', 'user', 'status')

class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'num_days', 'cost', 'slug')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'reply_status')

# Register your models with the custom admin classes
admin.site.register(City, CityAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Transpont, TranspontAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(TourOrder, TourOrderAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Question, QuestionAdmin)
