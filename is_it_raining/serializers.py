import random
from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal, AnimalImage


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'weather_code'
        )


class AnimalSerializer(serializers.ModelSerializer):
    random_image = serializers.SerializerMethodField()
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'image',
            'images',
            'random_image'
        )

    def get_random_image(self, obj):
        images = obj.images.order_by("?")
        if images:
            image = images.first()
            return image.image.url
        return None


class AnimalImageSerializer(serializers.ModelSerializer):
    model = AnimalImage
    fields = (
        'id',
        'animal',
        'weather'
    )

    def get_weather(self, obj):
        WEATHER_MAP = {
            2: 'Thunderstorm',
            3: 'Drizzle',
            5: 'Rain',
            6: 'Snow',
            7: 'Atmosphere',
            8: 'Clear',
        }

        return WEATHER_MAP.get(obj.weather.weather_code, '')


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = serializers.StringRelatedField(many=False)

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal'
        )
