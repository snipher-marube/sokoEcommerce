from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Account



class BaseFeedback(models.Model):
    type = models.CharField(choices=settings.FEEDBACK_CHOICES, max_length=100,
                            verbose_name=_('Type'))
    message = models.TextField(verbose_name=_('Message'))
    time = models.DateTimeField(auto_now_add=True, verbose_name=_('Time'))

    class Meta:
        abstract = True
        ordering = ['-time']

    def __unicode__(self):
        return self.message


class Feedback(BaseFeedback):
    user = models.ForeignKey(Account, verbose_name=_('User'), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('admin:view-feedback', args=[self.id])


class AnonymousFeedback(BaseFeedback):
    user = models.ForeignKey(Account, verbose_name=_('User'), null=True,
                             blank=True, default=None, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('admin:view-anon-feedback', args=[self.id])
