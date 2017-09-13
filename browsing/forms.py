from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import *
from inscriptions.models import *


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))


class InschriftFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InschriftFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'legacy_id',
                    'transkription',
                    'transkription_normalized',
                    'resch_kopial_signatur',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Advanced search options',
                    css_id="advanced_search_options"),
                AccordionGroup(
                    'Other search options',
                    css_id="other_search_options"
                ),
                css_id="accordion",
                )
            )