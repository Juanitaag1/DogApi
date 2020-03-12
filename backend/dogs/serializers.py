from rest_framework import serializers
from .models import Dog, Breed

class DogSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dog
        fields = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy' )

        # read_only_fields = ('date_created', 'date_modified')


# Breed
class BreedSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    name = serializers.CharField()
    dogs = DogSerializer(many=True, read_only=True)  # This.
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Breed
        fields = ('id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount' ,'exerciseneeds', 'dogs')
