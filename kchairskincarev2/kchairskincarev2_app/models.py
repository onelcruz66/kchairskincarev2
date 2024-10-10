from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class HourSelected(models.TextChoices):
    NINE = '9:00', _('9:00')
    TEN = '10:00', _('10:00')
    ELEVEN = '11:00', _('11:00')
    TWELVE = '12:00', _('12:00')
    ONE = '1:00', _('1:00')
    TWO = '2:00', _('2:00')
    THREE = '3:00', _('3:00')
    FOUR = '4:00', _('4:00')
    FIVE = '5:00', _('5:00')

class ServiceType(models.TextChoices):
    HAIRSTYLING = 'Hair Styling', _('Hair Styling')
    FACEMASK = 'Face Mask', _('Face Mask')
    SHAVING = 'Shaving', _('Shaving')
    BEARDTRIMMING = 'Beard Trimming', _('Beard Trimming')
    HAIRWASH = 'Hair Wash', _('Hair Wash')

class BarberName(models.TextChoices):
    KAMJI = 'Kamji', _('Kamji')
    STEPHEN = 'Stephen', _('Stephen')
    HELEN = 'Helen', _('Helen')

class AppointmentRequest(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    phone_number = models.CharField(max_length=50, blank=False, default='')
    date_requested = models.CharField(max_length=50, blank=False, default='')
    time_requested = models.CharField(max_length=50, choices=HourSelected.choices, default='')
    service_type = models.CharField(max_length=50, choices=ServiceType.choices, default='')
    barber_name = models.CharField(max_length=50, choices=BarberName.choices, default='')