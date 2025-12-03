from rest_framework import serializers
from .models import ContactMessage, User, Role, Permission, RolePermission

from rest_framework import serializers
from django.core.exceptions import ValidationError
from .validators import ComplexityValidator, CharacterRepeatValidator

class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        required=False
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions']


    def create(self, validated_data):
        permissions = validated_data.pop('permissions', [])
        role = Role.objects.create(**validated_data)

        for perm in permissions:
            RolePermission.objects.create(role=role, permission=perm)

        return role

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions', None)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if permissions is not None:
            RolePermission.objects.filter(role=instance).delete()
            for perm in permissions:
                RolePermission.objects.create(role=instance, permission=perm)

        return instance



class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'description']

class RolePermissionSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    permission = serializers.StringRelatedField()

    class Meta:
        model = RolePermission
        fields = ['id', 'role', 'permission']
        
class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        required=False,
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone', 'address', 'date_of_birth', 'role', 'role_id',
            'registered_by', 'temp_password_flag', 'status', 'notes', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}, 'registered_by': {'read_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role_id', None)
        password = validated_data.pop('password', None)
        
        # Set registered_by based on the logged-in user
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['registered_by'] = request.user.username
        else:
            validated_data['registered_by'] = 'Customer'  # default for self-signup

        user = User(**validated_data)

        if role:
            user.role = role

        if password:
            user.set_password(password)

        user.save()
        return user

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'date_of_birth']

    def validate_password(self, value):
        # Validate password complexity
        ComplexityValidator().validate(value)
        CharacterRepeatValidator().validate(value)
        return value

    def create(self, validated_data):
        # Ensure customer role exists
        customer_role, _ = Role.objects.get_or_create(name='Customer')

        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone=validated_data.get('phone'),
            address=validated_data.get('address', ''),
            date_of_birth=validated_data.get('date_of_birth', None),
            role=customer_role,
            registered_by='Customer',  # Always self-registered
            status='Active',
            temp_password_flag=False
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"