from django.db import models
from vocabs.models import SkosConcept
from bib.models import Book


class References(models.Model):
    book = models.ForeignKey(Book, blank=True, null=True)
    page = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=255)


class Person(models.Model):
    name = models.CharField(blank=True, max_length=255)
    titel_grad_beruf = models.CharField(blank=True, max_length=255)


class Inschrift(models.Model):
    gattung = models.ManyToManyField(SkosConcept, blank=True, related_name="gattung")
    traeger = models.ManyToManyField(SkosConcept, blank=True, related_name="traeger")
    schrift_hoch_min = models.IntegerField(blank=True, null=True)
    schrift_hoch_max = models.IntegerField(blank=True, null=True)
    schrift_breit_min = models.IntegerField(blank=True, null=True)
    schrift_breit_max = models.IntegerField(blank=True, null=True)
    majuskel_min = models.IntegerField(blank=True, null=True)
    majuskel_max = models.IntegerField(blank=True, null=True)
    mittellaenge = models.IntegerField(blank=True, null=True)
    oberlaenge = models.IntegerField(blank=True, null=True)
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
    quellen = models.ManyToManyField(References, blank=True)
    created = models.DateTimeField(null=True)
    status = models.NullBooleanField()
    schlagworte = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schlagworte"
    )
    restaurierungsphasen = models.CharField(blank=True, max_length=255)
    allgemeine_beschreibung = models.TextField(blank=True)
    schriftbeschreibung = models.TextField(blank=True)
    schriftklassifikation = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schriftklassifikation")
