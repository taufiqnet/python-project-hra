from __future__ import unicode_literals

from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _

from django.utils.html import mark_safe

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Employee(models.Model):
    emp_no = models.IntegerField(_('employee number'), primary_key=True)
    birth_date = models.DateField(_('birthday'), blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField(_('hire date'), blank=True, null=True)
    created = models.DateTimeField(_('created'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)

    image = models.ImageField(upload_to='employee_images', blank=True, default='employee_images/profile.jpg')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employees'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("core:employee-detail", args=[self.emp_no])

    def get_update_url(self):
        return reverse("core:employee-update", args=[self.emp_no])

    def get_delete_url(self):
        return reverse("core:employee-delete", args=[self.emp_no])

    # Admin Panel Image
    def image_tag(self):
        return mark_safe('<img src="%s" width="50px" height="50px" />' % (self.image.url))
        image_tag.short_description = 'Image'