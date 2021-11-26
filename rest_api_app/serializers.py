from rest_framework import serializers
from rest_api_app.models import Dogs, Breed, BREED_CHOICES

BREED_CHOICES = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large")
)


class DogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    age = serializers.IntegerField()
    breed = serializers.CharField(required=True, max_length=100)
    gender = serializers.CharField(required=True, max_length=100)
    color = serializers.CharField(required=True, max_length=100)
    favoritefood = serializers.CharField(required=False, allow_blank=True, max_length=100)
    favoritetoy = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Dogs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance


class BreedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    size = serializers.ChoiceField(choices=BREED_CHOICES)
    friendliness = serializers.IntegerField(required=True, min_value=1, max_value=5)
    trainability = serializers.IntegerField(required=True, min_value=1, max_value=5)
    sheddingamount = serializers.IntegerField(required=True, min_value=1, max_value=5)
    exerciseneeds = serializers.IntegerField(required=True, min_value=1, max_value=5)

    def create(self, validated_data):
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance