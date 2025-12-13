# hotel_management/utils/populate_initial_data.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_management.settings")
django.setup()

# ✅ IMPORT MODELS AFTER setup
from accounts.models import Role, Permission, RolePermission, User
from rooms.models import RoomType

# ==========================
# Permissions
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
# Roles → Permissions
# ==========================
roles_permissions = {
    "Admin": [1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
    "Manager": [1, 2, 4, 5, 6, 7,10,11],
    "Receptionist": [2, 5, 6, 8, 9],
    "Customer": [2, 5, 6,7],
}

# ==========================
# Room Types
# ==========================
room_types_data = [
    {"name": "Single"},
    {"name": "Family"},
    {"name": "Twin"},
]


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
        role, _ = Role.objects.get_or_create(name=role_name)
        print(f"   ➤ Role: {role.name}")

        RolePermission.objects.filter(role=role).delete()

        for perm_id in perm_ids:
            perm_dict = next((p for p in permissions_data if p["id"] == perm_id), None)
            if not perm_dict:
                continue

            perm = Permission.objects.get(name=perm_dict["name"])
            RolePermission.objects.create(role=role, permission=perm)
            print(f"      ✓ Assigned: {perm.name}")

    # ✅ ROOM TYPES (CORRECT PLACE)
    print("\n🏨 Creating Room Types...")
    for rt in room_types_data:
        room_type, created = RoomType.objects.get_or_create(name=rt["name"])
        print(f"   ✓ {room_type.name} ({'created' if created else 'exists'})")

    print("\n👑 Creating Admin User (romanat)...")
    admin_role = Role.objects.get(name="Admin")

    admin_user, created = User.objects.get_or_create(
        username="romanat",
        defaults={
            "email": "admin@example.com",
            "role": admin_role,
            "is_staff": True,
            "is_superuser": True,
        }
    )

    if created:
        admin_user.set_password("password")
        admin_user.save()
        print("   ✓ Admin user created!")
    else:
        print("   ✓ Admin user already exists (skipping).")

    print("\n🎉 All initial data loaded successfully!")


if __name__ == "__main__":
    seed_data()
