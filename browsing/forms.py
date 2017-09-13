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
                    'plain_word',
                    'right_context',
                    'spelling2',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Lexicon related search options',
                    'lemma__name',
                    'lemma__pos',
                    css_id="lexicon_search_options"),
                AccordionGroup(
                    'Morphology related search options',
                    'pos',
                    'label',
                    'medial_suffix',
                    'final_suffix',
                    'label__label',
                    'label__description',
                    'label__morphonotacticity',
                    css_id="morphology_search_options"
                ),
                AccordionGroup(
                    'Phonology related search options',
                    'rightonset',
                    'rightonset__variable',
                    'rightonset__pre_change',
                    'rightonset__post_change',
                    'rightonset__onset',
                    'rightonset__offset',
                    #cluster-consonant should be added here

                    css_id="phonology_search_options"),
                AccordionGroup(
                    'Phonotactics related search options',
                    'weight',
                    'weight_norm',
                    'cluster__consonant',
                    'cluster__first_consonant__consonant',
                    'cluster__second_consonant__consonant',
                    'cluster__third_consonant__consonant',
                    'cluster__fourth_consonant__consonant',
                    'cluster__size',
                    'cluster__ssp',
                    'cluster__nad_vc',
                    'cluster__nad_c1c2',
                    'cluster__nad_c2c3',
                    'cluster__preferred_cluster',
                    css_id="phonotactics_search_options"),
                AccordionGroup(
                    'Text related search options',
                    'text_source__genre',
                    'text_source__corpus',
                    'text_source__mean_date',
                    'text_source__size',
                    'text_source__dialect',
                    'text_source',
                    'text_source__mean_date__decade',
                    'text_source__mean_date__semicentury',
                    'text_source__mean_date__century',
                    css_id="text_search_options"),
                css_id="accordion",
                )
            )
