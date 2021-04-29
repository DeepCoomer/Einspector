from django.contrib import admin
from Inspector.models import Fir
from Inspector.models import Contact
from Inspector.models import StatusDetails

# Register your models here.
admin.site.register(Fir),
admin.site.register(Contact)
admin.site.register(StatusDetails)