from django import forms


class LolForm(forms.Form):
    '''A very complicated form.'''
    lol = forms.CharField(widget=forms.Textarea)


class FaqForm(forms.Form):
    q = forms.CharField()
