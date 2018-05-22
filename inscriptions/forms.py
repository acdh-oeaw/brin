from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Inschrift


class InschriftForm(forms.ModelForm):

    class Meta:
        model = Inschrift
        fields = "__all__"
        widgets = {
            'gattung': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=gattung'),
            'traeger': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=traeger'),
            'schlagworte': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=schlagworte'),
            'schriftklassifikation': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=schriftklassifikation'),
            'dating': autocomplete.ModelSelect2Multiple(
                url='../../vocabs-ac/skos-constraint-ac/?scheme=Dating'),
            'reference': autocomplete.ModelSelect2Multiple(
                url='burials:book-autocomplete'),
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
