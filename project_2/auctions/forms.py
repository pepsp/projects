from django import forms


class NewListingForm(forms.Form):
    title = forms.CharField(label="Title:")
    description = forms.CharField(label="Item's description:")
    image = forms.CharField(label="Image URL: ")
    category = forms.ChoiceField(label="Choose a Category")
    