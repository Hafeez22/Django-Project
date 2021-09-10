from django.contrib import admin
from .models import firstreview, items, models, review

# Register your models here.
admin.site.register(items)
admin.site.register(review)
admin.site.register(firstreview)