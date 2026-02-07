from rest_framework.views import APIView, Response #<-- Utilize to handle API behavior
from requests_oauthlib import OAuth1 # Authenticates a user with public and secret keys
from dotenv import load_dotenv # Allows us to interact with .env files
import requests # Pythons user friendly way to make requests to API's
import os # os will make it possible to grab key value pairs from .env

load_dotenv()

# Create your views here.
class PokeballImg(APIView):

    def get(self, request, ball):
        # Grab the url parameter of ball
        print(ball)
        auth = OAuth1(os.environ['NOUN_KEY'], os.environ['NOUN_SECRET_KEY'])
        print(os.environ['NOUN_KEY'], os.environ['NOUN_SECRET_KEY'])
        # pass in both the public and secret key from the Noun Project
        endpoint = f"https://api.thenounproject.com/v2/icon?query={ball}"
        response = requests.get(endpoint, auth=auth)
        print(response.status_code)
        # Send API request to the Noun_project
        responseJSON = response.json()
        return Response( {"thumbnail":responseJSON['icons'][0]['thumbnail_url']})