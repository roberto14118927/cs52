from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import DecimalField
from django.utils import timezone
import datetime

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length=250, null=False)