from django.contrib import admin

from api.models import Boshqarma, CustomUser, Unvon, Bolim, ClientData, ArizaModel, \
    JinoyatIshiModel


class BoshqarmaAdmin(admin.ModelAdmin):
    class Meta:
        model = Boshqarma
        fields = '__all__'


# class CustomUserAdmin(UserAdmin):
#     class Meta:
#         model = CustomUser
#         # fields = '__all__'


class UnvonAdmin(admin.ModelAdmin):
    class Meta:
        model = Unvon
        fields = '__all__'


class BolimAdmin(admin.ModelAdmin):
    class Meta:
        model = Bolim
        fields = '__all__'


admin.site.register(Boshqarma, BoshqarmaAdmin)
admin.site.register(Bolim, BolimAdmin)
admin.site.register(Unvon, UnvonAdmin)
admin.site.register(CustomUser)
# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(ClientData)
admin.site.register(ArizaModel)
admin.site.register(JinoyatIshiModel)
