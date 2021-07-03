from django.contrib import admin

from .models import Concept, Obs, Patient, Person, PersonName, Visit

admin.site.register(Concept)
admin.site.register(Obs)
admin.site.register(Patient)
admin.site.register(Person)
admin.site.register(Visit)

