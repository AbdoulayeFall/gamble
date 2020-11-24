from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

import datetime
# from django.forms.extras.widgets import SelectDateWidget


from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class form_type_pari(forms.Form):
    TYPE_PARI =[("1", "AutrePari"), ("2", "Match"), ("3", "Combat")]
    type = forms.ChoiceField(
        required=True,
        label="Type",
        choices=TYPE_PARI,
        widget = forms.Select(attrs = {'onchange' : 'this.form.submit();'})
    )

class form_autre_pari(forms.Form):
    name = forms.CharField(label='Nom')
    description = forms.CharField(label='Description')
    date = forms.DateField(label= "Date", widget=forms.SelectDateWidget(), required=True,)
    # date = forms.DateField(widget=SelectDateWidget)

class form_combat(forms.Form):
    name = forms.CharField(label='Nom')
    joueur1 = forms.CharField(label='Joueur1')
    joueur2 = forms.CharField(label='Joueur2')
    date = forms.DateField(label= "Date", widget=forms.SelectDateWidget(), required=True,)


class form_match(forms.Form):
    name = forms.CharField(label='Nom')
    equipe1 = forms.CharField(label='Equipe1')
    equipe2 = forms.CharField(label='Equipe2')
    date = forms.DateField(label= "Date", widget=forms.SelectDateWidget(), required=True,)
