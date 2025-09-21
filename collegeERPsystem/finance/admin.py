from django.contrib import admin
from .models import FeeInvoice, FeePlan,Payment
# Register your models here.
admin.site.register(FeePlan)
admin.site.register(FeeInvoice)
admin.site.register(Payment)