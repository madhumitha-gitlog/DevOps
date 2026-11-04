from django.db import models
class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   payment_id = models.CharField(max_length=100, null=True, blank=True)
   payment_status = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
