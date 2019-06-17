from django.db import models

class Dollar(models.Model):
    value = models.DecimalField(blank=False, max_digits=6, decimal_places=2)
    delta = models.DecimalField(blank=False, max_digits=6, decimal_places=2)
    value_at = models.DateField(blank=False)
    
    class Meta:
        ordering = ('value_at',)

