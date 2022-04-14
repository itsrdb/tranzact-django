from django.contrib import admin
from . models import employees, company, invoices

admin.site.register(company)
admin.site.register(employees)
admin.site.register(invoices)
# Register your models here.
