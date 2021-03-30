from django.contrib import admin
#from oc_lettings_site.models import Role, Status, User, Client, Contrat, Event

from .models import Letting
from .models import Address
from .models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
