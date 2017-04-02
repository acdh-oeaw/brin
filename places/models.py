from django.db import models


class AlternativeName(models.Model):
    name = models.CharField(max_length=250, blank=True, help_text="Alternative Name")

    def __str__(self):
        return self.name


class Place(models.Model):
    PLACE_TYPES = (
        ("part of building", "part of building"),
        ("building", "building"),
        ("district", "district"),
        ("city", "city"),
        ("country", "country")
    )

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalized name"
    )
    alternative_name = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names"
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID"
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True, help_text="A location this place is part of."
    )
    place_type = models.CharField(choices=PLACE_TYPES, null=True, blank=True, max_length=50)

    def __str__(self):
        return "{}".format(self.name)
