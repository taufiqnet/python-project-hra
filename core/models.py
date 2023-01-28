from __future__ import unicode_literals

from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _

from django.utils.html import mark_safe


class Department(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


# sex choices
# according to https://en.wikipedia.org/wiki/ISO/IEC_5218
NOT_KNOWN = "0"
MALE = "1"
FEMALE = "2"
NOT_APPLICABLE = "9"

SEX_CHOICES = (
        (NOT_KNOWN, _("Not Known")),
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (NOT_APPLICABLE, _("Not Applicable")),
    )


FULL_TIME = 'Full-Time'
PART_TIME = 'Part-Time'
CONTRACT = 'Contract'
INTERN = 'Intern'

EMPLOYEETYPE = (
    (FULL_TIME,'Full-Time'),
    (PART_TIME,'Part-Time'),
    (CONTRACT,'Contract'),
    (INTERN,'Intern'),
    )


class Employee(models.Model):
    emp_no = models.IntegerField(_('employee number'), primary_key=True)
    birth_date = models.DateField(_('birthday'), blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    sex = models.CharField(_("Gender"), choices=SEX_CHOICES, max_length=1, default=NOT_KNOWN, blank=True, db_index=True,)
    hire_date = models.DateField(_('hire date'), blank=True, null=True)
    department = models.ForeignKey(Department,verbose_name =_('Department'),on_delete=models.SET_NULL,null=True,default=None)
    employeetype = models.CharField(_('Employee Type'), max_length=15, default=FULL_TIME, choices=EMPLOYEETYPE,
                                    blank=False, null=True)

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
        return "{} {} ({})".format(self.first_name, self.last_name, self.emp_no)

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