from django import forms

class createListForm(forms.Form):
    title = forms.CharField(label = "Title of the List",max_length=200,required = True)
    id = forms.IntegerField(label = "ID")