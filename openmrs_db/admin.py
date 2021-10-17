from django.contrib import admin

from .models import Concept, EncounterType, Obs, Patient, Person, PersonName, Users, Visit
#from .models import Liquibasechangelog

admin.site.register(Concept)
admin.site.register(EncounterType)
admin.site.register(Obs)
admin.site.register(Patient)
admin.site.register(Person)
admin.site.register(Visit)
admin.site.register(Users)

# this is only to see what openmrs liquibase migrations have been done
#admin.site.register(Liquibasechangelog)

