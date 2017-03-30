
# coding: utf-8

# In[1]:

import csv


# In[2]:

def split_numbers(numbers):
    numbers = numbers.replace(" ", "")
    numbers = numbers.split("-")
    numbers = [s for s in numbers if s.isdigit()]
    return numbers


# In[3]:

split_numbers("48-55")


# In[4]:

file = "legacy_data/main.csv"


# In[5]:

with open(file, encoding='utf-8') as csvfile:
    data = [x for x in csv.reader(csvfile, delimiter=',') if not x[2].startswith("0000", 0, 4)]


# In[14]:

for x in data[1:]:
    temp_ins, _ = Inschrift.objects.get_or_create(legacy_id=x[0])
    for y in x[9].split(";"):
        temp_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title="gattung")
        temp_scheme.save()
        temp_concept, _ = SkosConcept.objects.get_or_create(pref_label=y)
        temp_concept.save()
        temp_concept.scheme.add(temp_scheme)
        temp_ins.gattung.add(temp_concept)
    for y in x[10].split(";"):
        temp_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title="traeger")
        temp_scheme.save()
        temp_concept, _ = SkosConcept.objects.get_or_create(pref_label=y)
        temp_concept.save()
        temp_concept.scheme.add(temp_scheme)
        temp_ins.traeger.add(temp_concept)
    for y in x[38].split(";"):
        temp_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title="schlagworte")
        temp_scheme.save()
        temp_concept, _ = SkosConcept.objects.get_or_create(pref_label=y)
        temp_concept.save()
        temp_concept.scheme.add(temp_scheme)
        temp_ins.schlagworte.add(temp_concept)
    for y in x[42].split(";"):
        temp_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title="schriftklassifikation")
        temp_scheme.save()
        temp_concept, _ = SkosConcept.objects.get_or_create(pref_label=y)
        temp_concept.save()
        temp_concept.scheme.add(temp_scheme)
        temp_ins.schlagworte.add(temp_concept)
        
    temp_ins.farbtraeger = x[17]
    temp_ins.farbschrift = x[18]
    temp_ins.erhaltungszustand = x[19]
    temp_ins.transkription = x[20]
    temp_ins.transkription_normalized = x[35]
    temp_ins.resch_kopial_signatur = x[24]
    temp_ins.resch_kopial_text = x[25]
    temp_ins.andere_kopial_signatur = x[26]
    temp_ins.anderer_kopial_text = x[27]
    temp_ins.notizen = x[28]
    temp_ins.bemerkungen = x[29]
    temp_ins.quellen_unstruktieriert = x[30]
    temp_ins.restaurierungsphasen = x[39]
    temp_ins.allgemeine_beschreibung = x[40]
    temp_ins.schriftbeschreibung = x[41]
    temp_ins.museale_inv_nummer = x[1]
    temp_ins.datierung_inschrift_written = x[3]
    try:
        temp_ins.aufnahmedatum = x[2]
    except:
        print(x[2])
    try:
        temp_ins.created = x[31]
    except:
        print(x[31])
    if len(split_numbers(x[11])) == 2:
        temp_ins.schrift_hoch_min = split_numbers(x[11])[0]
        temp_ins.schrift_hoch_max = split_numbers(x[11])[1]
    elif len(split_numbers(x[11])) == 1:
        temp_ins.schrift_hoch_min = split_numbers(x[11])[0]
        temp_ins.schrift_hoch_max = split_numbers(x[11])[0]
    else:
        pass
    if len(split_numbers(x[12])) == 2:
        temp_ins.schrift_breit_min = split_numbers(x[12])[0]
        temp_ins.schrift_breit_max = split_numbers(x[12])[1]
    elif len(split_numbers(x[12])) == 1:
        temp_ins.schrift_breit_min = split_numbers(x[12])[0]
        temp_ins.schrift_breit_max = split_numbers(x[12])[0]
    else:
        pass
    if len(split_numbers(x[13])) == 2:
        temp_ins.majuskel_min = split_numbers(x[13])[0]
        temp_ins.majuskel_max = split_numbers(x[13])[1]
    elif len(split_numbers(x[13])) == 1:
        temp_ins.majuskel_min = split_numbers(x[13])[0]
        temp_ins.majuskel_max = split_numbers(x[13])[0]
    else:
        pass
    if len(split_numbers(x[14])) == 2:
        temp_ins.minuskel_min = split_numbers(x[14])[0]
        temp_ins.minuskel_max = split_numbers(x[14])[1]
    elif len(split_numbers(x[14])) == 1:
        temp_ins.minuskel_min = split_numbers(x[14])[0]
        temp_ins.minuskel_max = split_numbers(x[14])[0]
    else:
        pass
    if len(split_numbers(x[15])) == 2:
        temp_ins.mittellaenge_min = split_numbers(x[15])[0]
        temp_ins.mittellaenge_max = split_numbers(x[15])[1]
    elif len(split_numbers(x[15])) == 1:
        temp_ins.mittellaenge_min = split_numbers(x[15])[0]
        temp_ins.mittellaenge_max = split_numbers(x[15])[0]
    else:
        pass
    if len(split_numbers(x[16])) == 2:
        temp_ins.oberlaenge_min = split_numbers(x[16])[0]
        temp_ins.oberlaenge_max = split_numbers(x[16])[1]
    elif len(split_numbers(x[16])) == 1:
        temp_ins.oberlaenge_min = split_numbers(x[16])[0]
        temp_ins.oberlaenge_max = split_numbers(x[16])[0]
    else:
        pass
    temp_ins.save()


# In[26]:

#for x in Inschrift.objects.all():
 #   x.delete()


# In[ ]:



