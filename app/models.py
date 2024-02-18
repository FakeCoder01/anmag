from django.db import models
from shortuuid.django_fields import ShortUUIDField
import random
# Create your models here.


class AnonUser(models.Model):
    id = ShortUUIDField(
        length=5,
        max_length=5,
        primary_key=True
    )
    name = models.CharField(max_length=32)
    pin = models.PositiveSmallIntegerField(default=random.randint(1000, 9999))

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user = models.ForeignKey(AnonUser, related_name="messages", on_delete=models.CASCADE)
    msg = models.CharField(max_length=200)
    extra = models.CharField(max_length=100, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.msg