from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Inschrift, Person, Reference


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class InschriftForm(forms.ModelForm):

    class Meta:
        model = Inschrift
        exclude = [
            'schlagworte',
        ]
        widgets = {
            'gattung': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=gattung'),
            'traeger': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=traeger'),
            'traeger_material': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=traegermaterial'),
            'schrift_anbringung': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=schriftanbringung'),
            'schlagworte': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=schlagworte'),
            'schriftklassifikation': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=schriftklassifikation'),
            'dating': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=Dating'),
            'reference': autocomplete.ModelSelect2Multiple(
                url='burials:book-autocomplete'),
            'kennname': autocomplete.ModelSelect2Multiple(
                url='inschriften-ac:person-ac'),
            'kuenstler': autocomplete.ModelSelect2Multiple(
                url='inschriften-ac:person-ac'),
            'images': autocomplete.ModelSelect2Multiple(
                url='images-ac:image-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(InschriftForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
