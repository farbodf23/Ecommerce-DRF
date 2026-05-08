from django.contrib import admin
from .models import Profile, Cart, CartItem

# Register your models here.


@admin.register(Profile)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class TodoAdmin(admin.ModelAdmin):
    pass
