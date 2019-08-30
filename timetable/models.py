from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy


class Date(models.Model):
    WEEKDAY = {
        ('1', _('Monday')),
        ('2', _('Tuesday')),
        ('3', _('Wednesday')),
        ('4', _('Thursday')),
        ('5', _('Friday')),
        ('6', _('Saturday')),
        ('7', _('Sunday')),
    }
    date = models.DateField(unique=True, verbose_name=_('Date'))
    weekday = models.CharField(
        max_length=1,
        choices=WEEKDAY,
        verbose_name=_('Day of the week'),
    )
    is_active = models.BooleanField(default=False, verbose_name=_('Working'))
    message = models.TextField(max_length=225, blank=True, null=True, verbose_name=_('Message'))

    class Meta:
        verbose_name = pgettext_lazy('Meta|Date', 'Date')
        verbose_name_plural = pgettext_lazy('Meta|Dates', 'Dates')

    def __str__(self):
        return f"{self.date}"
