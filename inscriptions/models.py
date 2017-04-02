from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from bib.models import Book
from places.models import Place
from images.models import Image


class Reference(models.Model):
    book = models.ForeignKey(Book, blank=True, null=True)
    page = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.book


class Person(models.Model):
    name = models.CharField(blank=True, max_length=255)
    titel_grad_beruf = models.CharField(blank=True, max_length=255)
    gnd_id = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


class Inschrift(models.Model):
    gattung = models.ManyToManyField(SkosConcept, blank=True, related_name="gattung")
    traeger = models.ManyToManyField(SkosConcept, blank=True, related_name="traeger")
    schrift_hoch_min = models.IntegerField(blank=True, null=True)
    schrift_hoch_max = models.IntegerField(blank=True, null=True)
    schrift_breit_min = models.IntegerField(blank=True, null=True)
    schrift_breit_max = models.IntegerField(blank=True, null=True)
    majuskel_min = models.IntegerField(blank=True, null=True)
    majuskel_max = models.IntegerField(blank=True, null=True)
    minuskel_min = models.IntegerField(blank=True, null=True)
    minuskel_max = models.IntegerField(blank=True, null=True)
    mittellaenge_min = models.IntegerField(blank=True, null=True)
    mittellaenge_max = models.IntegerField(blank=True, null=True)
    oberlaenge_min = models.IntegerField(blank=True, null=True)
    oberlaenge_max = models.IntegerField(blank=True, null=True)
    farbtraeger = models.CharField(blank=True, max_length=255)
    farbschrift = models.CharField(blank=True, max_length=255)
    erhaltungszustand = models.CharField(blank=True, max_length=255)
    transkription = models.TextField(blank=True)
    transkription_normalized = models.TextField(blank=True)
    kennname = models.ManyToManyField(Person, blank=True, related_name="kennname")
    kuenstler = models.ManyToManyField(Person, blank=True, related_name="kuenstler")
    resch_kopial_signatur = models.CharField(blank=True, max_length=255)
    resch_kopial_text = models.TextField(blank=True)
    andere_kopial_signatur = models.CharField(blank=True, max_length=255)
    anderer_kopial_text = models.TextField(blank=True)
    notizen = models.TextField(blank=True)
    bemerkungen = models.TextField(blank=True)
    quellen = models.ManyToManyField(Reference, blank=True)
    quellen_unstruktieriert = models.TextField(blank=True)
    created = models.DateTimeField(null=True, blank=True)
    status = models.NullBooleanField()
    schlagworte = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schlagworte"
    )
    restaurierungsphasen = models.CharField(blank=True, max_length=255)
    allgemeine_beschreibung = models.TextField(blank=True)
    schriftbeschreibung = models.TextField(blank=True)
    schriftklassifikation = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schriftklassifikation")
    legacy_id = models.IntegerField(blank=True, null=True)
    museale_inv_nummer = models.CharField(blank=True, max_length=255)
    aufnahmedatum = models.DateField(null=True, blank=True)
    datierung_inschrift_written = models.CharField(blank=True, max_length=255, null=True)
    datierung_inschrift = models.DateField(null=True, blank=True)
    genauer_standort = models.ForeignKey(
        Place, blank=True, null=True, related_name="genauer_standort"
    )
    alter_standort = models.CharField(blank=True, max_length=255, null=True)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return "{}".format(self.legacy_id)

    def get_absolute_url(self):
        return reverse('inschriften:inschrift_detail', kwargs={'pk': self.id})
