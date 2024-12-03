from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Boshqarma(BaseModel, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bolim(BaseModel, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Unvon(BaseModel, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomUser(BaseModel, User, models.Model):
    father_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    jton = models.CharField(max_length=8)
    boshqarma = models.ForeignKey(Boshqarma, on_delete=models.SET_NULL, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)
    unvon = models.ForeignKey(Unvon, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name


class Device(BaseModel, models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return self.name


class Imei(BaseModel, models.Model):
    imei = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.imei


class SimCard(BaseModel, models.Model):
    number = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
