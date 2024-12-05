from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('yoqolgan', "Yo'qoldi"),
    ('ogirlatilgan', "O'girlatilgan"),
    ('unitilgan', 'Unitib Qoldirilgan'),
    ('topilgan', 'Topilgan'),
]


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


class PrimaryData(BaseModel, models.Model):
    phone = models.CharField(max_length=255)
    jton = models.CharField(max_length=9)

    def __str__(self):
        return self.phone


class UserProfile(BaseModel):
    userPrimaryData = models.OneToOneField(PrimaryData, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255)

    def __str__(self):
        return self.fullName


class CustomUser(BaseModel, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boshqarma = models.ForeignKey(Boshqarma, on_delete=models.SET_NULL, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)
    unvon = models.ForeignKey(Unvon, on_delete=models.SET_NULL, null=True)
    userPrimaryData = models.ForeignKey(PrimaryData, on_delete=models.SET_NULL, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, unique=True)
    jton = models.CharField(max_length=8, unique=True)
    ishjoylari = models.ManyToManyField(Boshqarma, related_name='ishjoylari', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Device(BaseModel, models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    info = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='yoqolgan',
    )

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


class ClientData(BaseModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    jshir = models.CharField(max_length=30)
    shakl1 = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
