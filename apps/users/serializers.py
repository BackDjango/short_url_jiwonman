from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers

AuthUser = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["password", "email", "name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = AuthUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data.get("name"),
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

    def login(self, request):
        user = self.validated_data
        login(request, user)


class EmptySerializer(serializers.Serializer):
    pass  # For endpoints that do not require input
