from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


User = get_user_model()


class Contract(models.Model):
    
    number = models.CharField(max_length=256, verbose_name="number")
    code = models.CharField(max_length=256, verbose_name="code")
    start_date = models.DateField()
    end_date = models.DateField()
    approved_date = models.DateField()
    currency_id = models.IntegerField()
    partner_id = models.IntegerField()
    partner_address_id = models.IntegerField()   
    notes = models.TextField(null=True)
    dimm_1 = models.IntegerField(blank=True, null=True)
    dimm_2 = models.IntegerField(blank=True, null=True)
    dimm_3 = models.IntegerField(blank=True, null=True)
    dimm_4 = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(null=True)
    self_partner_id = models.IntegerField()
    status_id = models.IntegerField(default=1)
    responsible_id = models.IntegerField()
    repartization_key = models.TextField()
    renewel_type_id = models.IntegerField()
    renewel_end_date = models.DateTimeField()
    penalty_percent_day = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attachment = models.FileField(blank=True, null=True, default='')

    def __str__(self):
        return f'{self.number} {self.start_date} {self.code}'
