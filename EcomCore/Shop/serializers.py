from rest_framework import serializers
from .models import Product, Room, Concept

class ProductSerializer(serializers.ModelSerializer):
    room = serializers.CharField() 
    concept = serializers.CharField() 

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'room', 'concept', 'image']
        

    def create(self, validated_data):
        room_name = validated_data.pop('room', None)
        concept_name = validated_data.pop('concept', None)

        
        room, _ = Room.objects.get_or_create(name=room_name) if room_name else (None, None)
        concept, _ = Concept.objects.get_or_create(name=concept_name) if concept_name else (None, None)

        
        return Product.objects.create(room=room, concept=concept, **validated_data)
