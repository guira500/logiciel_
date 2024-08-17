from django import forms
from django.forms import fields, widgets
from .models import administrateur, reserv, facturier, restaurer

class administrateurRegistration(forms.ModelForm):
    class Meta:
        model = administrateur
        fields = ['nom_admin','prenom_admin', 'email', 'password']
        widgets = {
            'nom_admin': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_admin': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        } 


    def save(self, commit=True):
        administrateur = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            administrateur.set_password(password)
        if commit:
            administrateur.save()
        return administrateur
    


class ReservForm(forms.ModelForm):
    class Meta:
        model = reserv
        fields = ['Chambre', 'Salle', 'jr', 'statut', 'sexe', 'prix_total', 'date_debut', 'date_fin', 'rest', 'mode_paiement', 'nbr_personne']
        
        widgets = {
            'Chambre': forms.TextInput(attrs={'class': 'form-control'}),
            'Salle': forms.TextInput(attrs={'class': 'form-control'}),
            'jr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de jours'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'prix_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix total'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rest': forms.Select(attrs={'class': 'form-control'}),
            'mode_paiement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mode de paiement'}),
            'nbr_personne': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de personnes'}),
        }


class FacturierForm(forms.ModelForm):
    class Meta:
        model = facturier
        fields = ['mnt_verse', 'remise', 'total_paye', 'statut', 'Emp']
        
        widgets = {
            'mnt_verse': forms.TextInput(attrs={'class': 'form-control'}),
            'remise': forms.TextInput(attrs={'class': 'form-control'}),
            'total_paye': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }






class RestaurerForm(forms.ModelForm):
    class Meta:
        model = restaurer
        fields = ['Restau', 'Chambre', 'Salle', 'Client', 'quantite', 'total', 'Emp']
        
        widgets = {
            'quantite': forms.TextInput(attrs={'class': 'form-control'}),

        }
