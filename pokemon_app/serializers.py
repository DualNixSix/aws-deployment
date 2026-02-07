# # pokemon_app/serializers.py
# from rest_framework import serializers
# from ..pokeball_app.models import Pokemon
# from move_app.serializers import MoveSerializer


# class PokemonSerializer(serializers.ModelSerializer):
#     moves = MoveSerializer(many=True)

#     class Meta:
#         model = Pokemon
#         fields = ('id', 'name', 'level', 'moves') # You can use as many fields as you like from your model