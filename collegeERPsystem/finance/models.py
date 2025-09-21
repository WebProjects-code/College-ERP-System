from django.db import models
from academics.models import Program, Semester
from django.conf import settings
from django.utils import timezone

class FeePlan(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester_no = models.IntegerField()
    base_fee = models.DecimalField(max_digits=12, decimal_places=2)
    misc_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class FeeInvoice(models.Model):
    STATUS_CHOICES = [("pending","pending"),("paid","paid"),("overdue","overdue"),("partial","partial")]
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    generated_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    METHOD_CHOICES = [("khalti","khalti"),("stripe","stripe"),("cash","cash")]
    STATUS_CHOICES = [("initiated","initiated"),("success","success"),("failed","failed"),("refunded","refunded")]
    invoice = models.ForeignKey(FeeInvoice, on_delete=models.CASCADE, related_name="payments")
    method = models.CharField(max_length=32, choices=METHOD_CHOICES)
    txn_id = models.CharField(max_length=256, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="initiated")
    paid_at = models.DateTimeField(null=True, blank=True)
    meta = models.JSONField(null=True, blank=True)

    def mark_success(self, txn_id=None):
        self.status = "success"
        self.txn_id = txn_id or self.txn_id
        self.paid_at = timezone.now()
        self.save()
        # update invoice
        total_paid = sum(p.amount for p in self.invoice.payments.filter(status="success"))
        if total_paid >= self.invoice.amount:
            self.invoice.status = "paid"
        else:
            self.invoice.status = "partial"
        self.invoice.save()
