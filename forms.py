from django import forms

FIELD_BOOL = ('or')

class SearchForm(forms.Form):
    book_code = forms.CharField()
    chapter = forms.IntegerField(required=False)
    mode = forms.CharField(required=False)
    question_name = forms.CharField(required=False)
    question_name_exclude = forms.CharField(required=False)
    question_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'field'}))
    question_field_exclude = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'field'}))
    answer_bool = forms.BooleanField(required=False)
    answer_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'field'}))
    solution_bool = forms.BooleanField(required=False)
    solution_field = forms.CharField(required=False,  widget=forms.Textarea(attrs={'class':'field'}))
