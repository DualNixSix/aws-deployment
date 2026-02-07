from rest_framework.views import APIView, Response

# We will also want to get Move to ensure we can grab those instances from the db
from move_app.models import Move

# We will utilize serializer to turn our QuerySets into
# binary string
from django.core.serializers import serialize

# Json.loads will turn binary strings into JSON data
import json


# Create your views here.
class AllMoves(APIView):
    # specify which request method should trigger this behavior
    def get(self, request):
        # grab a binary string of all Moves in the DB ordered by name
        moves = serialize('json', Move.objects.all().order_by('name'))
        # utilize json.loads to turn moves into JSON Data
        moves = json.loads(moves)
        return Response(moves)
    

class SelectedMove(APIView):

    def get(self, request, name):
        move = serialize('json', [Move.objects.get(name = name.title())])
        move = json.loads(move)[0]
        return Response(move)