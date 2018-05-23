from django.contrib import admin

# Register your models here.
from models_.models import Place, Restaurant, Waiter, Publication, Article
# Register your models here.
admin.site.register(Place)
admin.site.register(Waiter)
admin.site.register(Restaurant)
admin.site.register(Publication)
admin.site.register(Article)