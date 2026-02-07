# We will import the following to read and return JSON data more efficiently
from rest_framework.views import APIView, Response

# for admin only Puts, Posts, Deletes
from rest_framework.permissions import IsAuthenticated

# We want to bring in our model
from .models import Pokemon

# We will also want to get Move to ensure we can grab those instances from the db
from move_app.models import Move

# We will utilize serializer to turn our QuerySets into a binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json

# Create your views here.
class AllPokemon(APIView):
    # Require a valid token for ALL requests to this view
    permission_classes = [IsAuthenticated]
    # Establish the method that will trigger this behavior
    def get(self, request):
        # Grab all Pokemon existing within our database in a
        # specific order to keep consistency. In this case
        # we will order our data by name in aphabetical order
        pokemon = Pokemon.objects.order_by("name")
        # we can't send back query sets as a valid JSON response
        # so we will utilize Django's built in serialize function
        # to turn our query set into a binary string
        serialized_pokemon = serialize("json", pokemon)
        # Now we can use the python json.loads function to turn
        # our binary string into a workable json format
        json_pokemon = json.loads(serialized_pokemon)
        # currently moves is a list of ints but we want the actual pokemon instances
        for pokemon in json_pokemon:
            # query the database to grab a list of move instances
            move_data = Move.objects.filter(id__in=pokemon["fields"]["moves"])
            # assign it to the original pokemon moves as serialized data
            pokemon["fields"]["moves"] = json.loads(serialize("json", move_data))
        return Response(json_pokemon)
    
# Other way to serialize - breaks frontend
#     # pokemon_app/views.py
# from .serializers import PokemonSerializer

# class AllPokemon(APIView):
#     # Establish the method that will trigger this behavior
#     def get(self, request):
#         # Grab all Pokemon existing within our database in a
#         pokemons = Pokemon.objects.order_by("name")
#         serializer = PokemonSerializer(pokemons, many=True)
#         return Response(serializer.data)
    

    
    
    def post(self, request):
        # Only admins should be able to create new pokemon
        if not request.user.is_staff:
            return Response({"detail": "Only Admin's are allowed to post. Sorry."}, status=403)
        # We can use the kwargs method and pass in request.data (a dict) into the create argument
        new_pokemon = Pokemon.objects.create(**request.data)
        new_pokemon.save()
        new_pokemon.full_clean()
        new_pokemon = json.loads(serialize('json', [new_pokemon]))
        return Response(new_pokemon)
    

class SelectedPokemon(APIView):
    # Require a valid token for ALL requests to this view
    permission_classes = [IsAuthenticated]
    # lets create a class method to grab a pokemon by id or name
    # to avoid repeating this logic on every single request method.
    def get_pokemon(self, id):
        if type(id) == int:
            return Pokemon.objects.get(id = id)
        else:
            return Pokemon.objects.get(name = id.title())
        
    def get(self, request, id):  # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        pokemon = self.get_pokemon(id)
        json_pokemon = serialize('json', [pokemon])
        serialized_pokemon = json.loads(json_pokemon)
        return Response(serialized_pokemon)

    def put(self, request, id):  # <-- ID is our url parameter
        # Only admins should be able to update pokemon
        if not request.user.is_staff:
            return Response({"detail": "Only Admin's are allowed to put. Sorry."}, status=403)
        # we still want to grab a pokemon either by ID or by name
        pokemon = self.get_pokemon(id)
        # Now we have to check the body of our request and check if
        # the following keys are in our request ['level_up', 'captured', 'moves']
        if 'level' in request.data:
            # we will level up a pokemon to the desired level
            pokemon.level_up(request.data['level'])
        if 'captured' in request.data:
            # a pokemons captured status will be set to this value
            pokemon.change_caught_status(request.data['captured'])
        # full clean to check our validations
        pokemon.full_clean()
        # save all changes
        pokemon.save()
        # serialize our updated pokemon and return it as json
        pokemon = json.loads(serialize('json', [pokemon]))
        return Response(pokemon)
    
    def delete(self, request, id):
        # Only admins should be able to delete pokemon
        if not request.user.is_staff:
            return Response({"detail": "Only Admin's are allowed to delete. Sorry."}, status=403)
        # get a pokemon from our database
        pokemon = self.get_pokemon(id)
        # grab the pokemons name before deleting to utilize in the Response message
        pokemon_name = pokemon.name
        # delete instance and database entry
        pokemon.delete()
        # return the name of the pokemon deleted
        return Response(f"{pokemon_name} was deleted")