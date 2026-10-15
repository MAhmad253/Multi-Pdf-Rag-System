from rest_framework import serializers
from.models import Collections

class CollectionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields= [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

