from rest_framework import serializers
from .models import Airport, Deal

class DealSerializer(serializers.Serializer):
    class Meta:
        model = Deal
        fields = ['created', 'departure_airport', 'arrival_airport', 'miles', 'start_date', 'end_date']

    '''
    created = serializers.DateTimeField(auto_now_add=True)
    departure_airport serializers.ForeignKey(Airport, on_delete=(models.CASCADE), related_name='departure_airport')
    arrival_airport = serializers.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    miles = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        return Deal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.departure_airport validated_data.get('departure_airport', instance.departure_airport)
        instance.arrival_airport = validated_data.get('arrival_airport', instance.arrival_airport)
        instance.miles = validated_data.get('miles', instance.miles)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)

        instance.save()

        return instance
    '''

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['created', 'name']
    
    '''
    If inheriting from serializers.Serializer

    created = serializers.DateTimeField(auto_now_add=True)
    name = serializers.CharField(max_length=6)

    def create(self, validated_data):
        return Airport.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.name = validated_data.get('name', instance.name)
    '''