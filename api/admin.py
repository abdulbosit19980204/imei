from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Boshqarma, Imei, SimCard, CustomUser, Device, Unvon, Bolim


class BoshqarmaAdmin(admin.ModelAdmin):
    class Meta:
        model = Boshqarma
        fields = '__all__'


class ImeiAdmin(admin.ModelAdmin):
    class Meta:
        model = Imei
        fields = '__all__'


class SimCardAdmin(admin.ModelAdmin):
    class Meta:
        model = SimCard
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    class Meta:
        model = CustomUser
        fields = '__all__'


class DeviceAdmin(admin.ModelAdmin):
    class Meta:
        model = Device
        fields = '__all__'


class UnvonAdmin(admin.ModelAdmin):
    class Meta:
        model = Unvon
        fields = '__all__'


class BolimAdmin(admin.ModelAdmin):
    class Meta:
        model = Bolim
        fields = '__all__'


admin.site.register(Boshqarma, BoshqarmaAdmin)
admin.site.register(Imei, ImeiAdmin)
admin.site.register(SimCard, SimCardAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Unvon, UnvonAdmin)
admin.site.register(Bolim, BolimAdmin)
