from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False, allow_null=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        username_validation = username and User.objects.filter(username=username).exists()
        email_validation = email and User.objects.filter(email=email).exists()
        if username_validation and email_validation:
            raise serializers.ValidationError({
                'username': ['username already taken.'],
                'email': ['email already registered.']  
            })

        if username_validation:
            raise serializers.ValidationError({'username': ['username already taken.']})

        if email_validation:
            raise serializers.ValidationError({'email': ['email already registered.']})
        
        return data


    def create(self, validated_data: dict):
        if validated_data.get('is_employee') is True:
            validated_data['is_superuser'] = True
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.is_employee = validated_data.get('is_employee', instance.is_employee)
        instance.password = validated_data.get('password', instance.password)
        
        # Se o usuário for um funcionário, ele será um superusuário
        if instance.is_employee:
            instance.is_superuser = True

        instance.save()
        return instance

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token