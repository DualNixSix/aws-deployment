# exec(open("./setup_data.py").read())

from move_app.models import Move
from pokemon_app.models import Pokemon

# Create moves
psychic = Move.objects.create(name="Psychic")
flamethrower = Move.objects.create(name="Flamethrower")
thunderbolt = Move.objects.create(name="Thunderbolt")
vine_whip = Move.objects.create(name="Vine Whip")
water_gun = Move.objects.create(name="Water Gun")

# Create Pokémon
charizard = Pokemon.objects.create(
    name="Charizard",
    level=25,
    date_encountered="2007-04-07",
    captured=True
)

pikachu = Pokemon.objects.create(
    name="Pikachu",
    level=18,
    date_encountered="2008-06-12",
    captured=True
)

bulbasaur = Pokemon.objects.create(
    name="Bulbasaur",
    level=12,
    date_encountered="2009-03-22",
    captured=False
)

squirtle = Pokemon.objects.create(
    name="Squirtle",
    level=15,
    date_encountered="2010-09-01",
    captured=True
)

alakazam = Pokemon.objects.create(
    name="Alakazam",
    level=30,
    date_encountered="2006-11-19",
    captured=True
)

# Assign moves
charizard.moves.add(flamethrower)
pikachu.moves.add(thunderbolt)
bulbasaur.moves.add(vine_whip)
squirtle.moves.add(water_gun)
alakazam.moves.add(psychic)
