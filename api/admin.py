from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Boshqarma, CustomUser, Unvon, Bolim, ClientData, ArizaModel, \
    JinoyatIshiModel


class BoshqarmaAdmin(admin.ModelAdmin):
    model = Boshqarma
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class CustomUserAdmin(UserAdmin):  # Correct inheritance
    model = CustomUser
    list_display = ('id', 'phone_number', 'jton', 'first_name', 'last_name', 'father_name',)
    list_display_links = ('id', 'phone_number')
    search_fields = ('phone_number', 'jton', 'first_name', 'last_name')
    list_filter = ('ishjoylari',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'father_name', 'phone_number', 'jton')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Work Info', {'fields': ('boshqarma', 'bolim', 'unvon', 'ishjoylari')}),
    )


class UnvonAdmin(admin.ModelAdmin):
    model = Unvon
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class BolimAdmin(admin.ModelAdmin):
    model = Bolim
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class ArizaModelAdmin(admin.ModelAdmin):
    model = ArizaModel
    list_display = (
        'id', 'author', 'status', 'imei', 'last_simcard', 'model', 'color', 'created_at', 'updated_at', 'is_deleted')
    list_display_links = ('id', 'imei')
    list_filter = ('status', 'model', 'color')
    search_fields = ('imei', 'model', 'color')


admin.site.register(Boshqarma, BoshqarmaAdmin)
admin.site.register(Bolim, BolimAdmin)
admin.site.register(Unvon, UnvonAdmin)
# admin.site.register(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(ClientData)
admin.site.register(ArizaModel, ArizaModelAdmin)
admin.site.register(JinoyatIshiModel)
