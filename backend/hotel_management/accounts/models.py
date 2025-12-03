from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_permissions")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("role", "permission")
    
#     def __str__(self):
#         return f"{self.role.name} → {self.permission.name}"
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # New fields
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    registered_by = models.CharField(
        max_length=20,
        choices=[('Customer', 'Customer'), ('Receptionist', 'Receptionist')],
        default='Customer'
    )
    temp_password_flag = models.BooleanField(default=False)  # True if receptionist generated a temporary password
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended')],
        default='Active'
    )
    notes = models.TextField(blank=True, null=True)  # Optional internal notes

    def __str__(self):
        return self.username


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('reservation', 'Room Reservation'),
        ('inquiry', 'General Inquiry'),
        ('event', 'Event Planning'),
        ('spa', 'Spa Services'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"