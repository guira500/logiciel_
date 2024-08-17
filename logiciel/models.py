from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from decimal import Decimal
import uuid
# Create your models here.


class info(models.Model):

    choix = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    ]

    chx = [
        ('Non','Non'),
        ('Oui','Oui'),
    ]

    nom_hotel = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    etoile = models.CharField(max_length=20, choices=choix)
    Telephone = models.CharField(max_length=50)
    parking = models.CharField(max_length=20, choices=chx)
    boite = models.CharField(max_length=20, choices=chx)
    bordure = models.CharField(max_length=20, choices=chx)
    africain = models.CharField(max_length=20, choices=chx)
    europe = models.CharField(max_length=20, choices=chx)
    buffet = models.CharField(max_length=20, choices=chx)
    camera = models.CharField(max_length=20, choices=chx)
    paiement = models.CharField(max_length=20, choices=chx)
    piscine = models.CharField(max_length=20, choices=chx)
    air = models.CharField(max_length=20, choices=chx)
    acces = models.CharField(max_length=20, choices=chx)
    amerique = models.CharField(max_length=20, choices=chx)
    wifi = models.CharField(max_length=20, choices=chx)
    repassage = models.CharField(max_length=20, choices=chx)
    conference = models.CharField(max_length=20, choices=chx)
    carte = models.CharField(max_length=20, choices=chx)
    bar = models.CharField(max_length=20, choices=chx)
    reunion = models.CharField(max_length=20, choices=chx)
    local = models.CharField(max_length=20, choices=chx)
    asiatique = models.CharField(max_length=20, choices=chx)
    handicap = models.CharField(max_length=20, choices=chx)
    extincteur = models.CharField(max_length=20, choices=chx)
    parking_prive = models.CharField(max_length=20, choices=chx)
    reservation = models.CharField(max_length=20, choices=chx)


class salle(models.Model):

    chx = [
        ('Oui','Oui'),
        ('Non','Non'),
    ]

    choix = [
        ('Conférence', 'Conférence'),
        ('Reception', 'Reception'),
        ('Autre', 'Autre'),
    ]

    ch = [
        ('cle','cle'),
        ('carte','carte'),
        ('reconnaissance faciale','reconnaissance faciale'),
        ('emprunte digital','emprunte digital'),
    ]

    nom_batiment = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/', null=True, max_length=None)
    ventilateur = models.CharField(max_length=20, choices=chx)
    nom_salle = models.CharField(max_length=100)
    type_salle = models.CharField(max_length=20, choices=choix)
    autre = models.CharField(max_length=100)
    climatiseur = models.CharField(max_length=20, choices=chx)
    nbpers = models.CharField(max_length=100)
    prix_local = models.CharField(max_length=50)
    num_salle = models.CharField(max_length=50)
    type_access = models.CharField(max_length=100, choices=ch)



class chambre(models.Model):

    chx = [
        ('Oui','Oui'),
        ('Non','Non'),
    ]

    choix = [
        ('premium', 'premium'),
        ('standard', 'standard'),
        ('suite royale', 'suite royale'),
    ]

    select = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    ]

    ch = [
        ('cle','cle'),
        ('carte','carte'),
        ('reconnaissance faciale','reconnaissance faciale'),
        ('emprunte digital','emprunte digital'),
    ]

    nom_batiment = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/', null=True, max_length=None)
    type_lit = models.CharField(max_length=50)
    ventilateur = models.CharField(max_length=20, choices=chx)
    repas_soir = models.CharField(max_length=100)
    table = models.CharField(max_length=20, choices=chx)
    bagages = models.CharField(max_length=20, choices=chx)
    nom_chambre = models.CharField(max_length=100)
    type_chambre = models.CharField(max_length=50, choices=choix)
    climatiseur = models.CharField(max_length=20, choices=chx)
    repas_matin = models.CharField(max_length=20, choices=chx)
    eau_chaude = models.CharField(max_length=20, choices=chx)
    repassage = models.CharField(max_length=20, choices=chx)
    nbr_personne = models.CharField(max_length=20, choices=select)
    prix_local = models.CharField(max_length=50)
    prix_online = models.CharField(max_length=50)
    num_chambre = models.CharField(max_length=50)
    television = models.CharField(max_length=20, choices=chx)
    repas_midi = models.CharField(max_length=20, choices=chx)
    type_access = models.CharField(max_length=100, choices=ch)
    coffre = models.CharField(max_length=20, choices=chx)


class client(models.Model):

    type = [
        ('CNIB','CNIB'),
        ('PASSEPORT','PASSEPORT'),
        ('CARTE CONSULAIRE','CARTE CONSULAIRE'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    num_chambre = models.ForeignKey(chambre, on_delete=models.SET_NULL, null=True, blank=True)
    num_salle = models.ForeignKey(salle, on_delete=models.SET_NULL, null=True, blank=True)
    Telephone = models.CharField(max_length=100)
    provenance = models.CharField(max_length=100)
    type_piece = models.CharField(max_length=100, choices=type)
    num_piece = models.CharField(max_length=100)
    date_expire = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_arriver = models.CharField(max_length=100)
    date_depart = models.CharField(max_length=100)
    mode_paye = models.CharField(max_length=100)


class restaurant(models.Model):

    type = [
        ('plat', 'plat'),
        ('boisson', 'boisson'),
    ]

    categorie = models.CharField(max_length=100, choices=type)
    nom_plat = models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)


class outils(models.Model):

    nom_outil = models.CharField(max_length=100)
    quantite = models.CharField(max_length=100)
    prix_unitaire = models.CharField(max_length=100)


class AdministrateurManager(BaseUserManager):
    def create_user(self, email, nom_admin, prenom_admin, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email doit être fournie')
        email = self.normalize_email(email)
        administrateur = self.model(email=email, nom_admin=nom_admin, prenom_admin=prenom_admin, **extra_fields)
        #administrateur.set_password(password)
        administrateur.save(using=self._db)
        return administrateur

    def create_superuser(self, email, nom_admin, prenom_admin, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(email, nom_admin, prenom_admin, password, **extra_fields)

class administrateur(AbstractBaseUser, PermissionsMixin):
    nom_admin = models.CharField(max_length=100)
    prenom_admin = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdministrateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom_admin', 'prenom_admin']

    #def set_password(self, raw_password):
        #self.password = make_password(raw_password)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    # Ajouter des related_name pour éviter les conflits avec auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user'
    )



class EmployeManager(BaseUserManager):
    def create_user(self, email, nom_emp, prenom_emp, poste, datenaiss, telephone, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email doit être fournie')
        email = self.normalize_email(email)
        employe = self.model(
            email=email,
            nom_emp=nom_emp,
            prenom_emp=prenom_emp,
            poste=poste,
            datenaiss=datenaiss,
            telephone=telephone,
            **extra_fields
        )
        employe.set_password(password)
        employe.save(using=self._db)
        return employe

    def create_superuser(self, email, nom_emp, prenom_emp, poste, datenaiss, telephone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nom_emp, prenom_emp, poste, datenaiss, telephone, password, **extra_fields)

class employe(AbstractBaseUser):
    
    nom_emp = models.CharField(max_length=100)
    prenom_emp = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    datenaiss = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Telephone = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom_emp', 'prenom_emp', 'poste', 'datenaiss', 'telephone']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email



class restaurer(models.Model):

    Restau = models.ForeignKey(restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    Chambre = models.ForeignKey(chambre, on_delete=models.SET_NULL, null=True, blank=True)
    Salle = models.ForeignKey(salle, on_delete=models.SET_NULL, null=True, blank=True)
    Client = models.ForeignKey(client, on_delete=models.CASCADE)
    quantite = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_jour = models.DateTimeField(auto_now_add=True)
    Emp = models.ForeignKey(employe, on_delete=models.SET_NULL, null=True, blank=True)



class reserv(models.Model):
    statut = [
        ('Confirmée', 'Confirmée'),
        ('Annulée', 'Annulée'),
        ('En attente', 'En attente'),
    ]

    chx = [
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    ]

    STATUT_CONSO = [
        ('Aucun', 'Aucun'),
        ('Consommé', 'Consommé'),
    ]
    
    Chambre = models.ForeignKey(chambre, on_delete=models.SET_NULL, null=True, blank=True)
    Client = models.ForeignKey(client, on_delete=models.CASCADE)
    Salle = models.ForeignKey(salle, on_delete=models.SET_NULL, null=True, blank=True)
    jr = models.DecimalField(max_digits=10, decimal_places=2)
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=statut, default='En attente')
    sexe = models.CharField(max_length=100, choices=chx)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    Emp = models.ForeignKey(employe, on_delete=models.SET_NULL, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    rest = models.ForeignKey(restaurer, on_delete=models.SET_NULL, null=True, blank=True)
    mode_paiement = models.CharField(max_length=50, null=True, blank=True)
    nbr_personne = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Réservation {self.id} - {self.Client} pour {self.Chambre}"
    

class facturier(models.Model):

    chx = [
        ('Complet', 'Complet'),
        ('En attente', 'En attente'),
    ]

    Reserv = models.ForeignKey(reserv, on_delete=models.CASCADE)
    mnt_verse = models.CharField(max_length=100)
    remise = models.CharField(max_length=100, default=0)
    total_paye = models.CharField(max_length=100)
    statut = models.CharField(max_length=100, choices=chx, default='En attente')
    date_reglement = models.DateTimeField(auto_now_add=True)
    Emp = models.ForeignKey(employe, on_delete=models.SET_NULL, null=True, blank=True)


class entretien(models.Model):

    Chambre = models.ForeignKey(chambre, on_delete=models.CASCADE)
    Emp = models.ForeignKey(employe, on_delete=models.CASCADE)
    date_nettoyage = models.DateField(auto_now_add=True)


class travailler(models.Model):

    Chambre = models.ForeignKey(chambre, on_delete=models.CASCADE)
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField()
    mtnt = models.CharField(max_length=100)
    motif = models.CharField(max_length=200)
    autre_motif = models.TextField(max_length=None)


class consommation(models.Model):
    reserves = models.ForeignKey(reserv, on_delete=models.CASCADE, related_name='consommation_details')
    Rest = models.ForeignKey(restaurer, on_delete=models.CASCADE, related_name='consommations')
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0'))
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return f"Consommation: {self.reserves} - {self.Rest} - {self.montant}"