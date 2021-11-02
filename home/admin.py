from django.contrib import admin
from .models import front_order
from .models import back_order
from .models import fullstack_order







admin.site.register (front_order)
admin.site.register (back_order)
admin.site.register (fullstack_order)