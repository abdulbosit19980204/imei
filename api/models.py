from django.db import models
from django.contrib.auth.models import User, AbstractUser

STATUS_ARIZA = [
    ('yoqolgan', "Yo'qoldi"),
    ('ogirlatilgan', "O'girlatilgan"),
    ('topilgan', 'Topilgan'),
]
STATUS_JINOYAT = [
    ('ochilgan', "Yangi"),
    ('yopildi', 'Yopilgan'),
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
    bolim = models.ForeignKey(Boshqarma, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Unvon(BaseModel, models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CustomUser(BaseModel, AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    boshqarma = models.ForeignKey(Boshqarma, on_delete=models.SET_NULL, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)
    unvon = models.ForeignKey(Unvon, on_delete=models.SET_NULL, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, unique=True)
    jton = models.CharField(max_length=8, unique=True)
    ishjoylari = models.ManyToManyField(Boshqarma, related_name='ishjoylari', blank=True)

    def __str__(self):
        return self.first_name


class ClientData(BaseModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    jshir = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.father_name}"


class Device(BaseModel, models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Qurilma kim tomonidan kiritilgan
    owner = models.ForeignKey(ClientData, on_delete=models.CASCADE)  # Qurilmaning egasi haqida ma'lumot
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    info = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_ARIZA,
        default='yoqolgan',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Imei(BaseModel, models.Model):
    imei = models.CharField(max_length=255, unique=True)  # IMEI noyob bo‘lishi kerak
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,  # Bitta qurilma o‘chirilsa, bog‘liq IMEI o‘chiriladi
        null=True,
        blank=True,  # IMEI ba'zi qurilmalarda bo‘lmaydi
        related_name='imeis'  # Qurilmaning barcha IMEI ro‘yxatini olish imkoniyati
    )

    def __str__(self):
        return self.imei


class SimCard(BaseModel, models.Model):
    number = models.CharField(max_length=255, unique=True)  # SIM karta raqami noyob bo‘lishi kerak
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,  # Qurilma o‘chirilsa, bog‘liq SIM karta o‘chiriladi
        null=True,
        blank=True,  # SIM karta ba'zi qurilmalarda bo‘lmaydi
        related_name='sim_cards'  # Qurilma bilan bog‘liq barcha SIM kartalar ro‘yxatini olish imkoniyati
    )

    def __str__(self):
        return self.number


class ArizaModel(BaseModel, models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(ClientData, on_delete=models.CASCADE)
    imei = models.CharField(max_length=255)
    last_simcard = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    info = models.TextField()
    shakl1 = models.CharField(max_length=30)
    status = models.CharField(
        max_length=50,
        choices=STATUS_ARIZA,
        default='yoqolgan',
    )

    description = models.TextField()

    def __str__(self):
        return f"{self.owner} {self.imei} {self.model}"


class JinoyatIshiModel(BaseModel, models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fish = models.CharField(max_length=255)
    jshir = models.CharField(max_length=255)
    info = models.TextField()
    phone_number = models.CharField(max_length=13)
    status = models.CharField(
        max_length=50,
        choices=STATUS_JINOYAT,
        default='yopilgan',
    )

    def __str__(self):
        return self.fish
