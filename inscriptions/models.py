from django.db import models
from django.urls import reverse
from vocabs.models import SkosConcept
from places.models import Place
from images.models import Image


class Reference(models.Model):
    short_title = models.TextField(
        blank=True, null=True,
        verbose_name="Kurzzitat"
    )
    long_title = models.TextField(
        blank=True, null=True,
        verbose_name="Langzitat"
    )
    page_number = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=255)

    def __str__(self):
        if self.short_title:
            return "{}".format(self.short_title)
        else:
            return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('inschriften:reference_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_reference')

    @classmethod
    def get_createview_url(self):
        return reverse('inschriften:reference_create')

    def get_next(self):
        next = Reference.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Reference.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class Person(models.Model):
    name = models.CharField(
        blank=True, max_length=255,
        verbose_name="Name wie aus Datenimport übernommen",
        help_text="Für internen Gebrauch"
    )
    vor_name = models.CharField(
        blank=True, max_length=255, verbose_name="Vorname"
    )
    nach_name = models.CharField(
        blank=True, max_length=255, verbose_name="Nachname"
    )
    titel_grad_beruf = models.CharField(blank=True, max_length=255)
    gnd_id = models.CharField(
        verbose_name="GND-ID", help_text="Falls es zu dieser Personen einen Eintrag\
        in der GND gibt, bitte diese hier eintragen",
        blank=True, max_length=255
    )

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('inschriften:person_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_persons')

    @classmethod
    def get_createview_url(self):
        return reverse('inschriften:person_create')

    def get_next(self):
        next = Person.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Person.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class Inschrift(models.Model):
    gattung = models.ManyToManyField(
        SkosConcept, blank=True, related_name="gattung",
        verbose_name="Inschriftengattung",
        help_text="Klassifikation der Inschrift nach ihrer Gattung (Grab-, Gedächtnis-,\
        Renovierungsinschrift, Baunachricht, Historische Nachricht, Stiftungsinschrift,\
        Gedenkinschrift, Künstlerinschrift, Datierung etc.)."
        )
    traeger = models.ManyToManyField(
        SkosConcept, blank=True, related_name="traeger",
        verbose_name="Inschriftenträger",
        help_text="Klassifikation des Inschriftenträgers (Grabplatte, Epitaph, Fassade, Türsturz,\
        Altar, Kelch, Tafelmalerei, Medaillon, Grenzstein, Uhr etc.)."
        )
    traeger_material = models.ManyToManyField(
        SkosConcept, blank=True, related_name="traeger_material",
        verbose_name="Material des Inschriftenträgers",
        help_text="Auswahlmöglichkeiten: Holz, Stein, Keramik, Glas, Horn, Elfenbein, Gold, Silber,\
        Blech, Leinwand, Putz, Stoff"
        )
    schrift_anbringung = models.ManyToManyField(
        SkosConcept, blank=True, related_name="anbringung",
        verbose_name="Anbringung der Schrift",
        help_text="Art der Anbringung der Schrift am/im Inschriftenträger\
        (vertieft, erhaben, eingeritzt, ausgelegt, gemalt etc.)."
        )
    hoehe_schrifttraeger = models.IntegerField(
        blank=True, null=True,
        verbose_name="Höhe des Inschriftenträgers",
        help_text="Höhe des Inschriftenträgers, Angabe in Millimetern."
        )
    breite_schrifttraeger = models.IntegerField(
        blank=True, null=True,
        verbose_name="Breite des Inschriftenträgers",
        help_text="Breite des Inschriftenträgers, Angabe in Millimetern."
        )
    schrift_hoch_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Höhe Schriftfeld",
        help_text="Minimale Höhe des Schriftfeldes, Angabe in Millimetern."
        )
    schrift_hoch_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Höhe Schriftfeld",
        help_text="Maximale Höhe des Schriftfeldes, Angabe in Millimetern."
        )
    schrift_breit_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Breite Schriftfeld",
        help_text="Minimale Breite des Schriftfeldes, Angabe in Millimetern."
        )
    schrift_breit_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Breite Schriftfeld",
        help_text="Maximale Breite des Schriftfeldes, Angabe in Millimetern."
        )
    majuskel_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Höhe Majuskel",
        help_text="minimale Höhe eines Großbuchstaben"
        )
    majuskel_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Höhe Majuskel",
        help_text="maximale Höhe eines Großbuchstaben"
        )
    minuskel_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Höhe Minuskel",
        help_text="minimale Höhe eines Kleinbuchstaben"
        )
    minuskel_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Höhe Minuskel",
        help_text="maximale Höhe eines Kleinbuchstaben"
        )
    mittellaenge_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Höhe Mittellänge",
        help_text="minimale Höhe einer Mittellänge (a, c, m, etc.)"
        )
    mittellaenge_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Höhe Mittellänge",
        help_text="maximale Höhe einer Mittellänge (a, c, m, etc.)"
        )
    oberlaenge_min = models.IntegerField(
        blank=True, null=True,
        verbose_name="minimale Höhe Oberlänge",
        help_text="minimale Höhe einer Oberlänge (b, f, l, k, etc.)"
        )
    oberlaenge_max = models.IntegerField(
        blank=True, null=True,
        verbose_name="maximale Höhe Oberlänge",
        help_text="maximale Höhe einer Oberlänge (b, f, l, k, etc.)"
        )
    farbtraeger = models.CharField(
        blank=True, max_length=255,
        verbose_name="Farbe des Inschriftenträgers",
        help_text="Beschaffenheit des Inschriftenträgers, im Fall von Steinen oder Putz eine\
        annähernde Beschreibung der Beschaffenheit der Oberfläche"
        )
    farbschrift = models.CharField(
        blank=True, max_length=255,
        verbose_name="Farbe der Schrift",
        help_text="Bei gemalten Inschriften wird/werden die Farbe/n der Schrift angegeben."
        )
    erhaltungszustand = models.CharField(
        blank=True, max_length=255,
        verbose_name="Erhaltungszustand",
        help_text="Erhaltungszustand der Inschrift und des Inschriftenträgers (sehr gut, gut,\
        befriedigend, schlecht, sehr schlecht)"
        )
    transkription = models.TextField(
        blank=True,
        verbose_name="Transkription",
        help_text="Transkription oder Edition des Textes der Inschrift nach feststehenden\
        Editionsrichtlinien (Auflösung von Abkürzungen, Verwendung von Trennzeichen\
        und Klammern etc.)."
        )
    transkription_normalized = models.TextField(
        blank=True,
        verbose_name="Transkription normalisiert",
        help_text="Normalisierte  Transkription oder Edition des Textes der Inschrift nach\
        feststehenden Editionsrichtlinien (Auflösung von Abkürzungen, Verwendung von\
        Trennzeichen und Klammern etc.)."
        )
    kennname = models.ManyToManyField(
        Person, blank=True, related_name="kennname",
        verbose_name="Kenname(n)",
        help_text="Name/n der in der Inschrift genannten Person/en, Personengruppen\
        (z.B. Klarissen, Kapuziner, Domkapitel) und Orte in normalisierter und ggf. ergänzter\
        Schreibung"
        )
    kuenstler = models.ManyToManyField(
        Person, blank=True, related_name="kuenstler",
        verbose_name="ausführender Künstler",
        help_text="Informationen über den/die ausführenden Künstler,\
        sofern diese/r bekannt ist/sind"
        )
    resch_kopial_signatur = models.CharField(
        blank=True, max_length=255,
        verbose_name="Signatur bei Resch",
        help_text="Signatur in Joseph Reschs 'Monumenta veteris ecclesie Brixinensis' (1765) bzw.\
        im 'Supplementum ad Monumenta Brixinensia' (1775)."
        )
    resch_kopial_text = models.TextField(
        blank=True, verbose_name="Transkription bei Resch",
        help_text="Transkription durch Joseph Resch in den 'Monumenta veteris ecclesie Brixinensis'\
        (1765) bzw. im 'Supplementum ad Monumenta Brixinensia' (1775)."
        )
    andere_kopial_signatur = models.CharField(
        blank=True, max_length=255,
        verbose_name="weitere Signaturen",
        help_text="Gibt kopial überlieferte Signaturen bzw. Standorte wieder."
        )
    anderer_kopial_text = models.TextField(
        blank=True,
        verbose_name="weitere Transkriptionen",
        help_text="Gibt in der kopialen Überlieferung abgebildete Transkriptionen wieder."
        )
    notizen = models.TextField(blank=True,  verbose_name="Notizen")
    bemerkungen = models.TextField(
        blank=True, verbose_name="Bemerkungen",
        help_text="Kommentare zu Inhalt, Textverständnis, graphischen Besonderheiten, Sprache,\
        Formular; biographische oder kunsthistorische Hinweise sowie Verweise auf weiterführende\
        Literatur"
        )
    quellen = models.ManyToManyField(
        Reference, blank=True,
        verbose_name="Quellen und Literatur",
        help_text="Bisherige Nachweise der Inschriften, ggf. mit dem Zusatz ('Abb.'');\
        wichtige Arbeiten, die zum Verständnis des Inschriftenträgers und vor allem zum Inhalt\
        der In­schrift aufklärend und erläuternd beitragen können",
        related_name="has_inscriptions"
        )
    quellen_unstruktieriert = models.TextField(
        blank=True,
        verbose_name="Quellen und Literatur (unstrukturiert)",
        help_text="Bisherige Nachweise der Inschriften, ggf. mit dem Zusatz ('Abb.''); wichtige\
        Arbeiten, die zum Verständnis des Inschriftenträgers und vor allem zum Inhalt der\
        In­schrift aufklärend und erläuternd beitragen können"
        )
    created = models.DateTimeField(
        null=True, blank=True,
        verbose_name="Anlagedatum",
        help_text="Zeitpunkt der Anlegung des Datensatzes"
        )
    status = models.BooleanField(
        null=True,
        verbose_name="Status",
        help_text="Status der Bearbeitung (unfertig, halb fertig, fertig)."
        )
    status_resch = models.BooleanField(
        null=True,
        verbose_name="Status Resch",
        help_text="Status der Resch Transkription."
        )
    schlagworte = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schlagworte",
        verbose_name="Schlagworte",
        help_text="Die Beschlagwortung stellt eine erhebliche Hilfe für die Suche nach Einträgen\
        in der Datenbank dar. Schlagwörter können sowohl Personen- und Ortsnamen als auch Titel\
        und Ämter (Bischof, Diakon, Schulmeister) oder Sachbegriffe sein\
        (Engel, Fresko, Erker, Wirtshaus etc.)."
        )
    restaurierungsphasen = models.CharField(
        blank=True, max_length=255,
        verbose_name="Restaurierungsphasen",
        help_text="Beschreibung früherer Restaurierungen, falls vorhanden kann hier auch auf\
        Restaurierungsberichte verwiesen sein."
        )
    allgemeine_beschreibung = models.TextField(
        blank=True,
        verbose_name="allgemeine Beschreibung",
        help_text="Besonderheiten des Inschriftenträgers nach kunsthistorischen Gesichtspunkten,\
        Blasonierung von Wappen etc. Die Angaben 'links' und 'rechts' beziehen sich auf den\
        Standpunkt des Betrachters, nur im Fall von Wappenbeschreibungen verstehen\
        sich die Angaben den heraldischen Vorgaben entsprechend."
        )
    schriftbeschreibung = models.TextField(
        blank=True,
        verbose_name="Schriftbeschreibung",
        help_text="Hier ist die Schrift genauer beschrieben, d.h. man geht auf Besonderheiten,\
        Unregelmäßigkeiten, größere u. kleinere Buchstaben usw. ein. Mittels alphabetischem\
        Fußnotensystem wird im Transkriptionsfeld auch auf Varianten der Schrift bzw. Buchstaben\
        aufmerksam gemacht (siehe dort den sogenannten 'Variantenapparat')."

        )
    schriftklassifikation = models.ManyToManyField(
        SkosConcept, blank=True, related_name="schriftklassifikation",
        verbose_name="Schriftklassifikation",
        help_text="Art der verwendeten Schrift (Antiqua, Fraktur, Frühhumanistische Kapitalis,\
        Gotico-Antiqua, Gotische Majuskel, Gotische Minuskel, Kapitalis, Romanische Majuskel)."
        )
    legacy_id = models.IntegerField(
        blank=True, null=True, verbose_name="Legacy-ID"
        )
    museale_inv_nummer = models.CharField(
        blank=True, max_length=255,
        verbose_name="museale Inventarnummer",
        help_text="frühere Signaturen oder Inventarnummern von Museen, Archiven und Sammlungen"
        )
    aufnahmedatum = models.DateField(
        null=True, blank=True,
        verbose_name="Aufnahmedatum",
        help_text="Zeitpunkt der Anfertigung der Fotografie(n)"
        )
    datierung_inschrift_written = models.CharField(
        blank=True, max_length=255, null=True,
        verbose_name="Datierung",
        help_text="Exakte oder annähernde Datierung der Inschrift"
        )
    datierung_inschrift = models.DateField(
        null=True, blank=True,
        verbose_name="Datierung (normiert)",
        help_text="Normiertes Datum (YYYY-MM-DD)"
        )
    genauer_standort = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="genauer_standort",
        verbose_name="Standort",
        help_text="Lokalisierung der Inschrift an ihrem Standort zum Zeitpunkt der Aufnahme anhand\
        einer hierarchischen Darstellung (Ort, Fraktion, Weiler/Adresse, genauer Standort).\
        Beispiel: Gemeinde: Brixen, Fraktion: Dombezirk/Altstadt, Weiler/Adresse:\
        Runggadgasse 21, Genauer Standort: Südwand, Erker.",
        on_delete=models.SET_NULL
        )
    alter_standort = models.CharField(
        blank=True, max_length=255, null=True,
        verbose_name="früherer Standort",
        help_text="Frühere Aufstellungs- oder Aufbewahrungsorte, vor allem bei den\
        Brixner Grabmälern mit Bezug auf Joseph Reschs 'Monumenta veteris ecclesie Brixinensis'\
        (1765) und das 'Supplementum ad Monumenta Brixinensia' (1775)."
        )
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return "{}".format(self.legacy_id)

    def get_absolute_url(self):
        return reverse('inschriften:inschrift_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_inscriptions')

    @classmethod
    def get_createview_url(self):
        return reverse('inschriften:inschrift_create')

    def get_next(self):
        next = Inschrift.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Inschrift.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
