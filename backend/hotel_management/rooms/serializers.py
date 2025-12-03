from rest_framework import serializers
from .models import Review, RoomType, Room
import cloudinary.uploader

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ["id", "name"]


class ReviewSerializer(serializers.ModelSerializer):
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), 
        source='room'  # maps the room_id to the Room foreign key
    )

    class Meta:
        model = Review
        fields = ["id", "room_id", "reviewer_name", "rating", "comment", "created_at"]
        read_only_fields = ["id", "created_at"]

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)

    room_type_id = serializers.PrimaryKeyRelatedField(
        queryset=RoomType.objects.all(),
        source="room_type",
        write_only=True
    )
    reviews = ReviewSerializer(many=True, read_only=True)

    # incoming file uploads
    thumbnail_file = serializers.ImageField(write_only=True, required=False)
    images_files = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Room
        fields = [
            "id", "room_number", "floor",
            "room_type", "room_type_id",

            "title", "subtitle", "description",
            "price",

            "thumbnail", "images",
            "thumbnail_file", "images_files",
            "amenities", "about",
            "reviews",


            "category", "size", "view", "capacity",
            "featured",

            "status", "notes",
        ]

    def create(self, validated_data):
        thumbnail_file = validated_data.pop("thumbnail_file", None)
        images_files = validated_data.pop("images_files", None)

        room = Room.objects.create(**validated_data)

        if thumbnail_file:
            upload = cloudinary.uploader.upload(thumbnail_file)
            room.thumbnail = upload["secure_url"]

        uploaded_images = []
        if images_files:
            for img in images_files:
                upload = cloudinary.uploader.upload(img)
                uploaded_images.append(upload["secure_url"])

        if uploaded_images:
            room.images = uploaded_images

        room.save()
        return room

    def update(self, instance, validated_data):
        thumbnail_file = validated_data.pop("thumbnail_file", None)
        images_files = validated_data.pop("images_files", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if thumbnail_file:
            upload = cloudinary.uploader.upload(thumbnail_file)
            instance.thumbnail = upload["secure_url"]

        if images_files:
            new_images = []
            for img in images_files:
                upload = cloudinary.uploader.upload(img)
                new_images.append(upload["secure_url"])
            instance.images = new_images

        instance.save()
        return instance
