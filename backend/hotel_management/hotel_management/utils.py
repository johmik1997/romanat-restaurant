# populate_initial_data.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_management.settings")
django.setup()

from accounts.models import Role, Permission, RolePermission, User

# ==========================
# PERMISSIONS DATA
# ==========================

permissions_data = [
    {"id": 1, "name": "manage_rooms", "description": "Can add and edit rooms"},
    {"id": 2, "name": "view_rooms", "description": "Can view rooms"},
    {"id": 4, "name": "manage_reservations", "description": "Can approve/update reservations"},
    {"id": 5, "name": "create_reservation", "description": "Can create reservations"},
    {"id": 6, "name": "view_reservations", "description": "Can view own / all reservations"},
    {"id": 7, "name": "process_payment", "description": "Payment handling"},
    {"id": 8, "name": "check_in_guests", "description": "Receptionist use"},
    {"id": 9, "name": "check_out_guests", "description": "Receptionist use"},
    {"id": 10, "name": "manage_roles", "description": "Can Create/update roles"},
    {"id": 11, "name": "manage_users", "description": "Can create/update/delete staff"},
]

# ==========================
# ROLES AND PERMISSIONS
# ==========================

roles_permissions = {
    "Admin": [1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
    "Manager": [1, 2, 4, 5, 6, 7],
    "Receptionist": [2, 5, 6, 8, 9],
    "Customer": [2, 5, 6],
}

def seed_data():
    print("\n📌 Creating Permissions...")
    for perm in permissions_data:
        p, created = Permission.objects.get_or_create(
            name=perm["name"],
            defaults={"description": perm["description"]}
        )
        print(f"   ✓ {p.name} ({'created' if created else 'exists'})")

    print("\n📌 Creating Roles and assigning permissions...")
    for role_name, perm_ids in roles_permissions.items():
        role, created = Role.objects.get_or_create(name=role_name)
        print(f"   ➤ Role: {role.name}")

        # Reset old permissions (safe re-run)
        RolePermission.objects.filter(role=role).delete()

        for perm_id in perm_ids:
            perm = Permission.objects.get(name=permissions_data[perm_id - 1]["name"])
            RolePermission.objects.create(role=role, permission=perm)
            print(f"      ✓ Assigned: {perm.name}")

    print("\n👑 Creating Admin User (romanat)...")

    admin_role = Role.objects.get(name="Admin")

    ADMIN_USERNAME = "romanat"
    ADMIN_PASSWORD = "ChangeThisPassword123"   # ⬅️ CHANGE THIS
    ADMIN_EMAIL = "admin@example.com"

    admin_user, created = User.objects.get_or_create(
        username=ADMIN_USERNAME,
        defaults={
            "email": ADMIN_EMAIL,
            "role": admin_role,
            "is_staff": True,
            "is_superuser": True,
        }
    )

    if created:
        admin_user.set_password(ADMIN_PASSWORD)
        admin_user.save()
        print(f"   ✓ Admin user '{ADMIN_USERNAME}' created!")
    else:
        print(f"   ✓ Admin user '{ADMIN_USERNAME}' already exists (skipping).")

    print("\n🎉 All initial data loaded successfully!")

if __name__ == "__main__":
    seed_data()

