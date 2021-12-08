from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Room(models.Model):
    UID = models.PositiveSmallIntegerField(_("Original ID from website"), default=00000)
    image_link = models.CharField(_("Image Link"), max_length=500)
    title = models.CharField(_("Title of Room"), max_length=300)
    price_per_night = models.CharField(_("Price Per Night(min)"), max_length=25)
    rating = models.CharField(_("Star Rating"), max_length=5)
    link_to_site = models.CharField(_("Link to original Website"), max_length=500)
    std_space = models.CharField(_("Standard Space"), max_length=100, default="")
    max_space = models.CharField(_("Max Space"), max_length=100, default="")
    shower_count = models.CharField(_("Shower Count"), max_length=100, default="")
    bathroom_count = models.CharField(_("Bathroom Count"), max_length=100, default="")
    room_space = models.CharField(_("Room Space"), max_length=100, default="")
    state = models.CharField(_("State"), max_length=155, db_index=True, null=True)
    city = models.CharField(_("City"), max_length=155, db_index=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.link_to_site}"
