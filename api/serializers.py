from rest_framework.serializers import ModelSerializer
from api.models import CustomUser, Bolim, Boshqarma, Unvon, ArizaModel, ClientData


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

    def update(self, instance, validated_data):
        # Validated_data dagi barcha maydonlarni yangilash
        for field, value in validated_data.items():
            if field == 'ishjoylari':  # Many-to-Many maydonlar uchun maxsus ishlov
                instance.ishjoylari.set(value)
            elif field == 'jton':  # Parolni sozlash uchun maxsus ishlov
                instance.set_password(value)
            else:
                setattr(instance, field, value)  # Fieldni dinamik ravishda yangilash

        # O'zgarishlarni saqlash
        instance.save()
        return instance


class ArizaOwnerSerializer(ModelSerializer):
    class Meta:
        model = ClientData
        fields = ['id', 'first_name', 'last_name', 'father_name', 'phone_number', 'jshir', 'phone_number']


class ArizaModelSerializer(ModelSerializer):
    owner = ArizaOwnerSerializer(read_only=True)

    class Meta:
        model = ArizaModel
        fields = ['id', 'author', 'status', 'imei', 'last_simcard', 'model', 'color', 'created_at', 'updated_at',
                  'owner', ]

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.id
        clientdata = {}

        clientdata['jshir'] = validated_data['jshir']
        clientdata['phone_number'] = validated_data['phone_number']
        clientdata['first_name'] = validated_data['fish']
        validated_data['owner'] = ClientData.objects.create(**clientdata)
        ariza = ArizaModel.objects.create(**validated_data)
        return ariza

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
