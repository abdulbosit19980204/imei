from rest_framework.serializers import ModelSerializer
from api.models import CustomUser, Bolim, Boshqarma, Device, Imei, SimCard, Unvon


class BoshqarmaSerializer(ModelSerializer):
    class Meta:
        model = Boshqarma
        fields = ['id', 'name']


class BolimSerializer(ModelSerializer):
    class Meta:
        model = Bolim
        fields = ['id', 'name']


class UnvonSerializer(ModelSerializer):
    class Meta:
        model = Unvon
        fields = ['id', 'name']


class CustomUserSerializer(ModelSerializer):
    ishjoylari = BoshqarmaSerializer(many=True, read_only=True)
    bolim = BolimSerializer(read_only=True)
    boshqarma = BoshqarmaSerializer(many=False, read_only=True)
    unvon = UnvonSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'jton', 'first_name', 'last_name', 'father_name', 'phone_number', 'boshqarma',
                  'boshqarma',
                  'bolim',
                  'unvon',
                  'ishjoylari']
        depth = 1

    def create(self, validated_data):
        username = validated_data['phone_number']
        password = validated_data['jton']
        ishjoylari_data = validated_data.pop('ishjoylari', None)
        # Foydalanuvchi obyektini yaratamiz
        user = CustomUser.objects.create(**validated_data)
        user.username = username
        # user.is_active = False
        user.set_password(password)  # Parolni xesh qilish
        user.save()
        # Many-to-Many maydonni sozlaymiz (agar u mavjud bo'lsa)
        if ishjoylari_data:
            user.ishjoylari.set(ishjoylari_data)

        # Foydalanuvchini qaytaramiz
        return user
