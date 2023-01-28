from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from datetime import datetime
from core.models import Employee
from django.urls import reverse_lazy, reverse

# Create your models here.
SICK = 'sick'
CASUAL = 'casual'

LEAVE_TYPE = (
    (SICK, 'Sick Leave'),
    (CASUAL, 'Casual Leave'),
)

DAYS = 20


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_('Start Date'), help_text='leave start date', null=True, blank=False)
    end_date = models.DateField(verbose_name=_('End Date'), help_text='leave end date', null=True, blank=False)
    leave_type = models.CharField(choices=LEAVE_TYPE, max_length=25, default=SICK, null=True, blank=False)
    reason = models.CharField(verbose_name=_('Reason for Leave'), max_length=255,
                              help_text='add valid reason for leave', null=True, blank=True)
    default_days = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'), default=DAYS, null=True,
                                               blank=True)

    status = models.CharField(max_length=12, default='pending')  # pending,approved,rejected,cancelled
    is_approved = models.BooleanField(default=False)  # hide

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('leave')
        verbose_name_plural = _('leaves')
        db_table = 'leave'
        ordering = ['-created']  # recent objects

    def __str__(self):
        return ('{0} - {1}'.format(self.leave_type, self.employee))
