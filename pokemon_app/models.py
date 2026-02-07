# models has many different methods we will utilize when creating our Models
from django.db import models
from django.core import validators as v
from .validators import validate_name
from move_app.models import Move
from django.core.exceptions import ValidationError



# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    name = models.CharField(max_length=255, validators=[validate_name])

    level = models.IntegerField(default=1)

    date_encountered = models.DateField(auto_now_add=True)

    captured = models.BooleanField()

    description = models.TextField(default="Unkown", validators=[v.MinLengthValidator(5), v.MaxLengthValidator(150)])

    moves = models.ManyToManyField(Move)

    # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self, new_level):
        self.level = new_level
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self, status):
        self.captured = status
        self.save()

    def clean(self):
        if self.moves.count() > 4:  # Change the maximum number of relationships as needed
            raise ValidationError("A Pokemon can have at most 4 moves.")