from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note  # specify the model to be serialized
        fields = [
            "id",
            "body",
            "updated",
            "created",
        ]  # specify the fields to be serialized
