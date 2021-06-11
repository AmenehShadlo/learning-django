from django import forms
from ticketSales.models import concertModel

class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100,label="نام کنسرت",required=False)

class ConcertForm(forms.ModelForm):
    class Meta:
        model=concertModel
        fields=['Name','SingerName','lenght']
        #exclude=["Poster"]