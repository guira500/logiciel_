from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import ReservForm
from .forms import FacturierForm


from decimal import Decimal, InvalidOperation

from django.db.models import Sum
from datetime import datetime

from django.contrib import messages

from .models import info, chambre, client, restaurant, outils, administrateur, employe, reserv, restaurer, facturier, entretien, travailler, consommation, salle

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError

from django.core.mail import EmailMessage
from .utils import render_to_pdf 

from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import render_to_string

from .forms import administrateurRegistration
import os
# Create your views here.



def config(request):
    user = request.user
    mail = user.email
    return render(request, 'detail_config.html', {'mail':mail})

def hotel(request):
    t = timezone.localtime(timezone.now())

    if request.method == 'POST':
        nom_hotel = request.POST.get('nom_hotel')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        etoile = request.POST.get('etoile')
        Telephone = request.POST.get('Telephone')
        parking = request.POST.get('parking')
        boite = request.POST.get('boite')
        bordure = request.POST.get('bordure')
        africain = request.POST.get('africain')
        europe =request.POST.get('europe')
        buffet = request.POST.get('buffet')
        camera = request.POST.get('camera')
        paiement = request.POST.get('paiement')
        piscine = request.POST.get('piscine')
        air = request.POST.get('air')
        acces = request.POST.get('acces')
        amerique = request.POST.get('amerique')
        wifi = request.POST.get('wifi')
        repassage = request.POST.get('repassage')
        conference = request.POST.get('conference')
        carte = request.POST.get('carte')
        bar = request.POST.get('bar')
        reunion = request.POST.get('reunion')
        local = request.POST.get('local')
        asiatique = request.POST.get('asiatique')
        handicap = request.POST.get('handicap')
        extincteur = request.POST.get('extincteur')
        parking_prive = request.POST.get('parking_prive')
        reservation = request.POST.get('reservation')

        if nom_hotel and ville and adresse and email and etoile and Telephone :

            """ Info = info()
            Info.nom_hotel = nom_hotel
            Info.ville = ville
            Info.adresse = adresse
            Info.email = email
            Info.etoile = etoile
            Info.Telephone = Telephone """

            Info = info(nom_hotel = nom_hotel, ville = ville, adresse = adresse, email = email, etoile = etoile, Telephone = Telephone, parking = parking, boite = boite, bordure = bordure, africain = africain, europe = europe, buffet = buffet, 
                    camera = camera, paiement = paiement, piscine = piscine, air = air, acces = acces, amerique = amerique,
                    wifi = wifi, repassage = repassage, conference = conference, carte = carte, bar = bar, reunion = reunion,
                    local = local, asiatique = asiatique, handicap = handicap, extincteur = extincteur, parking_prive = parking_prive,
                    reservation = reservation)
            Info.save()

    user = request.user
    mail = user.email

    i = info.objects.first()

    context = {
        't':t,
        'mail':mail,
        'i':i
    }
    return render(request, 'form2.html', context)


def chmbre(request):
    t = timezone.localtime(timezone.now())

    if request.method == 'POST':
        nom_batiment = request.POST.get('nom_batiment')
        img = request.POST.get('img')
        type_lit = request.POST.get('type_lit')
        ventilateur = request.POST.get('ventilateur')
        repas_soir = request.POST.get('repas_soir')
        table = request.POST.get('table')
        bagages = request.POST.get('bagages')
        nom_chambre = request.POST.get('nom_chambre')
        type_chambre = request.POST.get('type_chambre')
        climatiseur = request.POST.get('climatiseur')
        repas_matin = request.POST.get('repas_matin')
        eau_chaude = request.POST.get('eau_chaude')
        repassage = request.POST.get('repassage')
        nbr_personne = request.POST.get('nbr_personne')
        prix_local = request.POST.get('prix_local')
        prix_online = request.POST.get('prix_online')
        num_chambre =request.POST.get('num_chambre')
        television = request.POST.get('television')
        repas_midi = request.POST.get('repas_midi')
        type_access = request.POST.get('type_access')
        coffre = request.POST.get('coffre')

        if nom_batiment and img and type_lit and ventilateur and repas_soir and table and bagages and nom_chambre and type_chambre and climatiseur and repas_matin and eau_chaude and repassage and nbr_personne and prix_local and prix_online and num_chambre and television and repas_midi and type_access and coffre :

            Chambre = chambre()
            Chambre.nom_batiment = nom_batiment
            Chambre.img = img
            Chambre.type_lit = type_lit
            Chambre.ventilateur = ventilateur
            Chambre.repas_soir = repas_soir
            Chambre.table = table
            Chambre.bagages = bagages
            Chambre.nom_chambre = nom_chambre
            Chambre.type_chambre = type_chambre
            Chambre.climatiseur = climatiseur
            Chambre.repas_matin = repas_matin
            Chambre.eau_chaude = eau_chaude
            Chambre.repassage = repassage
            Chambre.nbr_personne = nbr_personne
            Chambre.prix_local = prix_local
            Chambre.prix_online = prix_online
            Chambre.num_chambre = num_chambre
            Chambre.television = television
            Chambre.repas_midi = repas_midi
            Chambre.type_access = type_access
            Chambre.coffre = coffre

            Chambre.save()

    ch = chambre.objects.all()
    c = chambre.objects.count()

    user = request.user
    mail = user.email

    context = {
        't':t,
        'ch':ch,
        'mail':mail,
        'c':c
    }
    return render(request, 'chambre.html', context)


def salles(request):
    t = timezone.localtime(timezone.now())

    if request.method == 'POST':
        nom_batiment = request.POST.get('nom_batiment')
        img = request.POST.get('img')
        ventilateur = request.POST.get('ventilateur')
        nom_salle = request.POST.get('nom_salle')
        type_salle = request.POST.get('type_salle')
        climatiseur = request.POST.get('climatiseur')
        nbpers = request.POST.get('nbpers')
        prix_local = request.POST.get('prix_local')
        num_salle =request.POST.get('num_salle')
        type_access = request.POST.get('type_access')
        autre = request.POST.get('autre')

        if nom_batiment and img and ventilateur and nom_salle and type_salle and climatiseur and nbpers and prix_local and num_salle and type_access or autre :

            Salle = salle()
            Salle.nom_batiment = nom_batiment
            Salle.img = img
            Salle.type_salle = type_salle
            Salle.ventilateur = ventilateur
            Salle.nom_salle = nom_salle
            Salle.climatiseur = climatiseur
            Salle.nbpers = nbpers
            Salle.prix_local = prix_local
            Salle.num_salle = num_salle
            Salle.type_access = type_access
            Salle.autre = autre

            Salle.save()

    ch = salle.objects.all()
    c = salle.objects.count()

    user = request.user
    mail = user.email

    context = {
        't':t,
        'ch':ch,
        'mail':mail,
        'c':c
    }
    return render(request, 'salle.html', context)


def restau(request):
    t = timezone.localtime(timezone.now())
    if request.method == 'POST':
        categorie = request.POST.get('categorie')
        nom_plat = request.POST.get('nom_plat')
        prix_unitaire = request.POST.get('prix_unitaire')

        if categorie and nom_plat and prix_unitaire :
            plat = restaurant(
                categorie = categorie,
                nom_plat = nom_plat,
                prix_unitaire = prix_unitaire
            )

            plat.save()

    Plat = restaurant.objects.all()

    pl = restaurant.objects.count()

    user = request.user
    mail = user.email

    context={
        't':t,
        'Plat':Plat,
        'mail':mail,
        'pl':pl
    }
    return render(request, 'restaurant.html', context)



def resto(request):
    user = request.user
    mail = user.email

    c = chambre.objects.all()
    s = salle.objects.all()
    Emp = employe.objects.filter(email=mail).first()
    res = restaurant.objects.all()

    if request.method == 'POST':
        num_chambre = request.POST.get('num_chambre')
        num_salle = request.POST.get('num_salle')
        quantite = int(request.POST.get('quantite'))
        restau_id = request.POST.get('restau_id')

        selected_res = get_object_or_404(restaurant, id=restau_id)

        if num_chambre != '--Choix--':
            customer = client.objects.filter(num_chambre_id=num_chambre).first()
            customers = None
        else:
            customer = None
            customers = client.objects.filter(num_salle_id=num_salle).first()

        """ customer = client.objects.filter(num_chambre_id=num_chambre).first()
        customers = client.objects.filter(num_salle_id=num_salle).first()
        selected_res = get_object_or_404(restaurant, id=restau_id) """

        if (customer or customers) and selected_res:
            prix_total = selected_res.prix_unitaire * quantite

            # Enregistrer la commande de restauration
            r = restaurer()
            r.Restau=selected_res
            if customer:
                r.Chambre_id=customer.num_chambre_id
                r.Client_id=customer.id
            elif customers:
                r.Salle_id=customers.num_salle_id
                r.Client_id=customers.id
            r.Emp=Emp  # Passer l'objet employe
            r.quantite=quantite
            r.total=prix_total  # Initialiser avec le prix_total directement
            r.date_jour=timezone.now()
            
            r.save()

            # Mettre à jour ou créer une consommation associée à la réservation
            """ reservation = reserv.objects.filter(Client_id=customer.id).first()
            reservations = reserv.objects.filter(Client_id=customers.id).first()

            if reservation:
                    consommation_obj, created = consommation.objects.get_or_create(
                        reserves=reservation,
                        Rest=r
                    )

                    if not created:
                        consommation_obj.montant += prix_total
                    else:
                        consommation_obj.montant = prix_total

                    consommation_obj.save()
            else:
                    consommation_obj, created = consommation.objects.get_or_create(
                        reserves=reservations,
                        Rest=r
                    )

                    if not created:
                        consommation_obj.montant += prix_total
                    else:
                        consommation_obj.montant = prix_total

                    consommation_obj.save() """
            reservation = reserv.objects.filter(Client_id=customer.id if customer else customers.id).first()

            if reservation:
                consommation_obj, created = consommation.objects.get_or_create(
                    reserves=reservation,
                    Rest=r
                )
                consommation_obj.montant = consommation_obj.montant + prix_total if not created else prix_total
                consommation_obj.save()

            print('Commande enregistrée avec succès.')
        else:
            print('Erreur lors de l\'enregistrement de la commande.')

    ct = restaurer.objects.count()
    r = reserv.objects.filter()
    consomme = consommation.objects.all()

    context = {
        'mail': mail,
        'c': c,
        's':s,
        'res': res,
        'Emp': Emp,
        'ct': ct,
        'consomme':consomme,
    }
    return render(request, 'resto.html', context)



def reservation(request):
    user = request.user
    mail = user.email

    Emp = employe.objects.filter(email=mail).first()

    return render(request, 'detail_reservation.html', {'mail':mail, 'Emp':Emp})

def nouveau_achat(request):
    t = timezone.localtime(timezone.now())
    quantite = 0
    prix_unitaire = 0
    if request.method == 'POST':
        nom_outil = request.POST.get('nom_outil')
        quantite = request.POST.get('quantite')
        prix_unitaire = request.POST.get('prix_unitaire')

        if nom_outil and quantite and prix_unitaire :

            Outil = outils()
            Outil.nom_outil = nom_outil
            Outil.quantite = quantite
            Outil.prix_unitaire = prix_unitaire

            Outil.save()
    
    tool = outils.objects.all()
    total = quantite * prix_unitaire
    tools = outils.objects.count()

    user = request.user
    mail = user.email

    context={
        't':t,
        'tool':tool,
        'total':total,
        'mail':mail,
        'tools':tools
    }
    return render(request, 'achat_outil.html', context)

def list_chbr(request):
    t = timezone.localtime(timezone.now())
    
    # Obtenir les IDs des chambres à exclure
    """ entretiens_chambres_ids = entretien.objects.values_list('Chambre_id', flat=True)
    clients_chambres_ids = client.objects.values_list('num_chambre_id', flat=True)
    
    # Fusionner les deux ensembles d'IDs
    exclude_ids = set(entretiens_chambres_ids) | set(clients_chambres_ids)

    # Filtrer les chambres disponibles
    ch = chambre.objects.exclude(id__in=exclude_ids) """

    entretiens_chambres_ids = entretien.objects.values_list('Chambre_id', flat=True)
    
    # Obtenir les IDs des chambres actuellement occupées par des clients
    clients_chambres_ids = client.objects.filter(date_depart__gte=timezone.now()).values_list('num_chambre_id', flat=True)
    
    # Fusionner les deux ensembles d'IDs
    exclude_ids = set(entretiens_chambres_ids) | set(clients_chambres_ids)

    # Inclure les chambres dont la date de départ est arrivée
    chambres_disponibles_ids = chambre.objects.exclude(id__in=exclude_ids).values_list('id', flat=True)
    
    # Inclure les chambres dont la date de départ est arrivée
    chambres_disponibles = chambre.objects.filter(id__in=chambres_disponibles_ids)

    user = request.user
    mail = user.email

    Emp = employe.objects.filter(email=mail).first()

    context = {
        't': t,
        'mail': mail,
        'Emp': Emp,
        'chambres_disponibles':chambres_disponibles
    }
    return render(request, 'liste_chambre.html', context)


def form(request, id_chambre):

    c = get_object_or_404(chambre, id=id_chambre)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        Telephone = request.POST.get('Telephone')
        provenance = request.POST.get('provenance')
        type_piece = request.POST.get('type_piece')
        num_piece = request.POST.get('num_piece')
        date_expire = request.POST.get('date_expire')
        email = request.POST.get('email')
        date_arriver = request.POST.get('date_arriver')
        date_depart = request.POST.get('date_depart')
        mode_paye = request.POST.get('mode_paye')

        inf = client.objects.filter(Telephone = Telephone).first()

        if inf:
            inf.date_arriver = date_arriver
            inf.date_depart = date_depart
            inf.mode_paye = mode_paye
            inf.num_chambre_id = id_chambre
            inf.save()
            return redirect('reserve', id_chambre=c.id)
        
        else:
            if nom and prenom and Telephone and provenance and type_piece and num_piece and date_expire and email and date_arriver and date_depart and mode_paye :

                fm = client()
                fm.nom = nom
                fm.prenom = prenom
                fm.Telephone = Telephone
                fm.provenance = provenance
                fm.type_piece = type_piece
                fm.num_piece = num_piece
                fm.date_expire = date_expire
                fm.email = email
                fm.date_arriver = date_arriver
                fm.date_depart = date_depart
                fm.mode_paye = mode_paye
                fm.num_chambre_id = id_chambre
                fm.save()

                return redirect('reserve', id_chambre=c.id)
        

    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()
    
    context = {
        'mail':mail,
        'Emp':Emp,
        'c':c
    }
    return render(request, 'form.html', context)


def info_chbr(request, id_chambre):
    t = timezone.localtime(timezone.now())
    c = get_object_or_404(chambre, id=id_chambre)
    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()

    context = {
        't':t,
        'mail':mail,
        'Emp':Emp,
        'c':c
    }
    return render(request, 'info_chambre.html', context)

def outil(request):
    return render(request, 'detail_outil.html', {})


def travaux(request):
    return render(request, 'detail_travaux.html', {})

def personnel(request):
    return render(request, 'personnel.html', {})

def occupe(request):
    t = timezone.localtime(timezone.now())

    user = request.user
    mail = user.email

    O = client.objects.all()
    nombre_chambres_occupees = reserv.objects.filter(date_fin__gt=timezone.now()).values('Chambre_id').distinct().count()

    Emp = employe.objects.filter(email=mail).first()

    context = {
        't':t,
        'mail':mail,
        'O':O,
        'nombre_chambres_occupees':nombre_chambres_occupees,
        'Emp':Emp
    }
    return render(request, 'occupation_chambre.html', context)


def custom(request):

    user = request.user
    mail = user.email

    O = client.objects.all()

    Emp = employe.objects.filter(email=mail).first()

    context = {
        'mail':mail,
        'O':O,
        'Emp':Emp
    }
    return render(request, 'detail_client.html', context)


def reserve(request, id_chambre):

    c = get_object_or_404(chambre, id=id_chambre)

    user = request.user
    mail = user.email

    t = timezone.now()

    Client = client.objects.filter(num_chambre_id=c.id).first()
    Rest = restaurer.objects.filter(Restau_id__in=restaurant.objects.values_list('id', flat=True))

    date_depart_str = Client.date_depart
    date_arriver_str = Client.date_arriver

    # Conversion des chaînes en objets datetime
    date_depart = datetime.strptime(date_depart_str, "%Y-%m-%d")
    date_arriver = datetime.strptime(date_arriver_str, "%Y-%m-%d")

    nb_jour = (date_depart - date_arriver).days

    print(f"{c.prix_local}")
    print(f"{nb_jour}")

    c.prix_local = float(c.prix_local)

    pt = nb_jour * c.prix_local
    print(f"{pt}")

    if request.method == 'POST':
        sexe = request.POST.get('sexe')
        statut = request.POST.get('statut')
        nbr_personne = request.POST.get('nbr_personne')

        if sexe and statut:
             
            Reser = reserv()
            Reser.sexe = sexe
            Reser.jr = nb_jour
            Reser.statut = statut
            Reser.prix_total = pt
            Reser.Chambre_id = id_chambre
            Reser.Client_id = Client.id
            Reser.Emp_id = user.id
            Reser.restau_id = Rest.first().id if Rest.exists() else None
            Reser.date_reservation=t
            Reser.date_debut = Client.date_arriver
            Reser.date_fin = Client.date_depart
            Reser.mode_paiement = Client.mode_paye
            Reser.nbr_personne = nbr_personne

            Reser.save()

    Emp = employe.objects.filter(email=mail).first()

    context = {
        'mail':mail,
        'Emp':Emp,
        'c':c,
        'Client':Client,
        'pt':pt,
        't':t
    }
    return render(request, 'reserver.html', context)


def historique(request):
    user = request.user
    mail = user.email

    Emp = employe.objects.filter(email=mail).first()

    c = reserv.objects.filter(Chambre__isnull=False, Salle__isnull=True).count()
    t = reserv.objects.filter(Salle__isnull=False, Chambre__isnull=True).count()
    
    reser = reserv.objects.filter(Chambre__isnull=False, Salle__isnull=True)
    vr = reserv.objects.filter(Salle__isnull=False, Chambre__isnull=True)

    clients = client.objects.all()

    #res = restaurer.objects.all()

    context = {
        'mail':mail,
        'Emp':Emp,
        'reser':reser,
        'c':c,
        'clients':clients,
        'vr':vr,
        't':t
    }
    return render(request, 'historique.html', context)


def log_out(request):
    logout(request)
    return redirect('log_in')


def entretenir(request):
    cr = chambre.objects.all()
    emp = employe.objects.all()

    if request.method == 'POST':
        date_nettoyage = request.POST.get('date_nettoyage')
        Chambre_id = request.POST.get('Chambre_id')
        Emp_id = request.POST.get('Emp_id')

        if date_nettoyage and Chambre_id and Emp_id:

            s = entretien()
            s.date_nettoyage = date_nettoyage
            s.Chambre_id = Chambre_id
            s.Emp_id = Emp_id

            s.save()
    
    element = entretien.objects.all()
    c = entretien.objects.count()

    user = request.user
    mail = user.email

    context = {
        'cr':cr,
        'mail':mail,
        'emp':emp,
        'element':element,
        'c':c
    }
    return render(request, 'entretien.html', context)


def travail(request):

    cr = chambre.objects.all()
    emp = employe.objects.all()

    if request.method == 'POST':
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        Chambre_id = request.POST.get('Chambre_id')
        mtnt = request.POST.get('mtnt')
        motif = request.POST.get('motif')
        autre_motif = request.POST.get('autre_motif')

        if Chambre_id and date_debut and date_fin and mtnt and motif and autre_motif:

            sauver = travailler()
            sauver.Chambre_id = Chambre_id
            sauver.date_debut = date_debut
            sauver.date_fin = date_fin
            sauver.mtnt = mtnt
            sauver.motif = motif
            sauver.autre_motif = autre_motif

            sauver.save()
    
    element = travailler.objects.all()
    c = travailler.objects.count()

    user = request.user
    mail = user.email

    context = {
        'cr':cr,
        'mail':mail,
        'emp':emp,
        'element':element,
        'c':c
    }
    return render(request, 'travaux.html', context)


def employer(request):
    t = timezone.localtime(timezone.now())

    if request.method == 'POST':
        nom_emp = request.POST.get('nom_emp')
        prenom_emp = request.POST.get('prenom_emp')
        poste = request.POST.get('poste')
        datenaiss = request.POST.get('datenaiss')
        email = request.POST.get('email')
        Telephone = request.POST.get('Telephone')
        password = request.POST.get('password')

        if nom_emp and prenom_emp and poste and datenaiss and email and (Telephone or password):

            Emp = employe()
            Emp.nom_emp = nom_emp
            Emp.prenom_emp = prenom_emp
            Emp.poste = poste
            Emp.datenaiss = datenaiss
            Emp.email = email
            Emp.Telephone = Telephone
            Emp.set_password(password)

            Emp.save()

            msg = EmailMessage(
                "Creation de compte",
                f"Bonjour. Cher {Emp.nom_emp} <br> Ci-joint vos identifiants de connexion en tant que {Emp.poste} <br> email : {Emp.email}, <br> Mot de passe : {Emp.password}.<br> Vous changerez le mot de passe lors de votre première Connexion ! <br> Bien cordialement !",
                "SOMKIETA <guiraismael0@gmail.com>",
                [Emp.email]
            )
            msg.content_subtype = "html"
            msg.send()

    user = request.user
    mail = user.email

    emp = employe.objects.all()

    context = {
        't':t,
        'mail':mail,
        'emp':emp,
    }
    return render(request, 'personnel_hotel.html', context)


def log_in(request):
    msg = ""
    error = False

    if request.method == 'POST':

            email = request.POST.get('email')
            password = request.POST.get('password')

            # Rechercher l'employé ou l'administrateur
            user = employe.objects.filter(email=email).first() or administrateur.objects.filter(email=email).first()

            if user:
                # Authentifier l'utilisateur

                auth_user = authenticate(request, email=email, password=password)
                print(f"{user.password}")
                print(f"{password}")
                print(f"{make_password(password)}")
                if auth_user:
                    # Connecter l'utilisateur
                    auth_login(request, auth_user)
                    
                    # Vérifier le type d'utilisateur et rediriger en conséquence
                    if isinstance(user, administrateur):
                        return redirect('dashboard')
                    else:
                        if user.last_login is None:
                            return redirect('sign_in') 
                        else:
                            return redirect('dashboard')
                else:
                    error = True
                    msg = "Le mot de passe entré est incorrect"
            else:
                error = True
                msg = "Le nom d'utilisateur est incorrect"

    context = {
        'error': error,
        'msg': msg,
    }

    return render(request, 'login.html', context)



def sign_in(request):
    """ if request.method == "POST":
        fm = administrateurRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = administrateurRegistration()
    else:
        fm = administrateurRegistration()

    context = {
        'fm': fm,
    } """

    msg = ""
    error = False

    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            user = request.user

            if user.is_authenticated:
                try:
                    # Valider le mot de passe
                    validate_password(password, user)
                    user.set_password(password)
                    user.save()
                    return redirect('dashboard')
                except ValidationError as e:
                    # Gestion des erreurs de validation de mot de passe
                    error = True
                    msg = str(e)
            else:
                error = True
                msg = "L'utilisateur n'est pas connecté"
        else:
            error = True
            msg = "Les deux mots de passe ne correspondent pas"

    context = {
        'error': error,
        'msg': msg
    }

    return render(request, 'creation.html', context)


@login_required(login_url = 'log_in')
def dashboard(request):
    user = request.user
    mail = user.email

    # Obtenir les IDs des chambres occupées
    """ chambres_occupees_ids = list(reserv.objects.filter(date_fin__gt=timezone.now()).values_list('Chambre_id', flat=True))

    # Calculer le nombre de chambres occupées
    nombre_chambres_occupees = len(chambres_occupees_ids) """

    chambres_occupees_ids = list(
    reserv.objects.filter(
        date_fin__gt=timezone.now(),  # La réservation est encore active
        Chambre_id__isnull=False  # Inclure seulement celles avec un Chambre_id
    ).values_list('Chambre_id', flat=True)
    )

    # Calculer le nombre de chambres occupées
    nombre_chambres_occupees = len(chambres_occupees_ids)

    # Exclure les chambres occupées pour obtenir les chambres disponibles
    chambres_disponibles = chambre.objects.exclude(id__in=chambres_occupees_ids)
    nombre_chambres_disponibles = chambres_disponibles.count()

    Emp = employe.objects.filter(email=mail).first()

    c = client.objects.count()

    clients_actifs_ids = reserv.objects.filter(date_fin__gt=timezone.now(), statut='Confirmée').values_list('Client_id', flat=True).distinct()
    nombre_clients_actifs = clients_actifs_ids.count()

    c = reserv.objects.filter(Chambre__isnull=False, Salle__isnull=True).count()
    t = reserv.objects.filter(Salle__isnull=False, Chambre__isnull=True).count()
    
    reser = reserv.objects.filter(Chambre__isnull=False, Salle__isnull=True)
    vr = reserv.objects.filter(Salle__isnull=False, Chambre__isnull=True)


    context = {
        'mail': mail,
        'Emp': Emp,
        'nombre_chambres_occupees': nombre_chambres_occupees,
        'nombre_chambres_disponibles': nombre_chambres_disponibles,
        'c':c,
        'nombre_clients_actifs':nombre_clients_actifs,
        'reser':reser,
        'vr':vr
    }

    return render(request, 'index.html', context)


def reglement(request):
    user = request.user
    mail = user.email

    phone = client.objects.all()
    Emp = employe.objects.filter(email=mail).first()

    msg = ""
    error = False

    if request.method == 'POST':
        Telephone = request.POST.get('Telephone')
        print(f"Received Telephone: {Telephone}")

        if Telephone:
            try:
                ch = client.objects.get(Telephone=Telephone)
                return redirect('facture', id_client=ch.id)
            except client.DoesNotExist:
                error = True
                msg = "Le numéro de telephone n\'existe pas"
                print("Client does not exist.")
        else:
            error = True
            msg= "Le numéro de telephone n\'a pas été fourni"
            print("Client does not exist.")

    context = {
        'mail': mail,
        'Emp': Emp,
        'phone': phone,
        'msg':msg,
        'error':error
    }
    print(f"Error: {error}, Message: {msg}")
    return render(request, 'paiement.html', context)


def facture(request, id_client):

    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()

    client_instance = get_object_or_404(client, id=id_client)

    reservation = reserv.objects.filter(Client_id = client_instance.id)

    reser = reservation.first()

    if not reser :
        print(f"Aucune réservation trouvée pour le client avec l'ID {id_client}")
        return redirect('reglement')
    
    c = reservation.filter(Chambre__isnull=False, Salle__isnull=True).count()
    t = reservation.filter(Salle__isnull=False, Chambre__isnull=True).count()
    
    r = reservation.filter(Chambre__isnull=False, Salle__isnull=True).first()
    vr = reservation.filter(Salle__isnull=False, Chambre__isnull=True).first()
    
    rest = restaurer.objects.filter(Client_id=client_instance.id).first()

    consommations = consommation.objects.filter(reserves__in=reservation)
    total_consommation = consommations.aggregate(total=Sum('montant'))['total']

    total_consommation = total_consommation if total_consommation is not None else Decimal('0')

    total_r = r.prix_total if r else Decimal('0')
    total_vr = vr.prix_total if vr else Decimal('0')

    pt = total_r + total_consommation
    p = total_vr + total_consommation

    t = reser.prix_total + total_consommation

    if request.method == 'POST':
        mnt_verse = request.POST.get('mnt_verse')

        if mnt_verse:
            try:
                mnt_verse = Decimal(mnt_verse)  # Conversion en Decimal pour éviter des erreurs
            except (ValueError, InvalidOperation):
                print("Montant versé invalide.")
                return redirect('reglement')
            
            fact = facturier()
            if r:
                fact.Reserv = r
            else:
                fact.Reserv = vr
            fact.mnt_verse = mnt_verse
            if pt:
                if pt > mnt_verse:
                    fact.remise = pt - mnt_verse
                else:
                    fact.remise = mnt_verse - pt
            else:
                if p > mnt_verse:
                    fact.remise = p - mnt_verse
                else:
                    fact.remise = mnt_verse - p
            fact.statut = 'Complet'
            if pt:
                fact.total_paye = pt
            else:
                fact.total_paye = p
            fact.date_reglement = timezone.now()
            fact.Emp = Emp

            fact.save()
    
    #f = facturier.objects.filter(Reserv__in=r) | facturier.objects.filter(Reserv__in=vr) 

    if r and vr:
        f = facturier.objects.filter(Reserv=r) | facturier.objects.filter(Reserv=vr)
    elif r:
        f = facturier.objects.filter(Reserv=r)
    elif vr:
        f = facturier.objects.filter(Reserv=vr)
    else:
        f = facturier.objects.none()

    context = {
        'client': client_instance,
        'r':r,
        'vr':vr,
        'c':c,
        'reser':reser,
        't':t,
        'rest':rest,
        'pt':pt,
        'mail':mail,
        'Emp':Emp,
        'f':f,
        'pt':pt,
        't':t,
        'consommations': consommations,
        'total_consommation': total_consommation if total_consommation else 0
    }
    return render(request, 'facture.html', context)



class GeneratePdf(View):
    def get(self, request, id_client, *args, **kwargs):
        t = timezone.now()
        client_instance = get_object_or_404(client, id=id_client)
        r = reserv.objects.filter(Client_id=client_instance.id).first()

        if not r:
            return HttpResponse("Aucune réservation trouvée pour ce client")

        rest = restaurer.objects.filter(Client_id=client_instance.id).first()
        
        f = facturier.objects.filter(Reserv_id=r.id).first()

        consommations = consommation.objects.filter(reserves=r)
        total_consommation = consommations.aggregate(total=Sum('montant'))['total']

        total_consommation = total_consommation if total_consommation is not None else Decimal('0')

        pt = r.prix_total + total_consommation

        # Contexte pour le PDF
        pdf_context = {
            'client': client_instance,
            'r': r,
            'rest': rest,
            'pt': pt,
            'statut_facturier': f.statut if f else 'Non défini',
            'h': info.objects.first(),
            'f': f,
            't': t,
            'consommations': consommations,
            'total_consommation': total_consommation if total_consommation else 0
        }

        # Génération du PDF
        pdf_file_path = render_to_pdf('pdf_facture.html', pdf_context)
        if not pdf_file_path:
            return HttpResponse("Erreur lors de la génération du PDF")

        # Créer la réponse HTTP pour retourner le PDF
        try:
            with open(pdf_file_path, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="facture.pdf"'
            return response
        finally:
            # Supprimez le fichier PDF temporaire
            if os.path.exists(pdf_file_path):
                os.remove(pdf_file_path)



def envoimail(request, id_client):
    m = ""
    success = False
    t = timezone.now()
    client_instance = get_object_or_404(client, id=id_client)
    r = reserv.objects.filter(Client_id=client_instance.id).first()

    if not r:
        return HttpResponse("Aucune réservation trouvée pour ce client")

    rest = restaurer.objects.filter(Client_id=client_instance.id).first()
    pt = r.prix_total
    f = facturier.objects.filter(Reserv_id=r.id).first()

    # Définir le message qui sera inclus dans l'email
    email_message = f"Bonjour cher {client_instance.nom},"

    # Contexte pour le PDF
    pdf_context = {
        'client': client_instance,
        'r': r,
        'rest': rest,
        'pt': pt,
        'statut_facturier': f.statut if f else 'Non défini',
        'h': info.objects.first(),
        'f': f,
        'm':m,
        'success':success,
        't':t
    }

    # Génération du PDF
    pdf_file_path = render_to_pdf('fact.html', pdf_context)
    if not pdf_file_path:
        return HttpResponse("Erreur lors de la génération du PDF")

    try:
        # Contexte pour l'email
        email_context = {
            'message': email_message,
        }

        # Rendu du contenu de l'email
        html_text = render_to_string("email.html", email_context)
        msg = EmailMessage(
            "Facture de réservation",
            html_text,
            "SOMKIETA <guiraismael0@gmail.com>",
            [client_instance.email]
        )
        msg.content_subtype = "html"  # Spécifie que le contenu est HTML
        with open(pdf_file_path, 'rb') as pdf:
            msg.attach("facture_chambre.pdf", pdf.read(), 'application/pdf')
        msg.send()
    except Exception as e:
        #return HttpResponse(f"")
        messages.success(request, "Erreur lors de l'envoi de l'email : {e}")
    finally:
        # Supprimez le fichier PDF temporaire
        if os.path.exists(pdf_file_path):
            os.remove(pdf_file_path)

    messages.success(request, "Email envoyé avec succès")

    #return HttpResponse("Email envoyé avec succès")
    return redirect('historique')


def listeSalle(request):

    clients_salles_ids = client.objects.values_list('num_salle_id', flat=True)
    
    # Fusionner les deux ensembles d'IDs
    exclude_ids = set(clients_salles_ids)

    # Filtrer les chambres disponibles
    ch = salle.objects.exclude(id__in=exclude_ids)

    user = request.user
    mail = user.email

    Emp = employe.objects.filter(email=mail).first()

    context = {
        'mail':mail,
        'Emp':Emp,
        'ch':ch,
    }
    return render(request, 'listerSalle.html', context)



def reservationSalle(request, id_salle):

    s = get_object_or_404(salle, id=id_salle)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        Telephone = request.POST.get('Telephone')
        provenance = request.POST.get('provenance')
        type_piece = request.POST.get('type_piece')
        num_piece = request.POST.get('num_piece')
        date_expire = request.POST.get('date_expire')
        email = request.POST.get('email')
        date_arriver = request.POST.get('date_arriver')
        date_depart = request.POST.get('date_depart')
        mode_paye = request.POST.get('mode_paye')

        inf = client.objects.filter(Telephone = Telephone).first()

        if inf:
            inf.date_arriver = date_arriver
            inf.date_depart = date_depart
            inf.mode_paye = mode_paye
            inf.num_salle_id = id_salle
            inf.save()
            return redirect('reservations', id_salle=s.id)
        
        else:
            if nom and prenom and Telephone and provenance and type_piece and num_piece and date_expire and email and date_arriver and date_depart and mode_paye :

                fm = client()
                fm.nom = nom
                fm.prenom = prenom
                fm.Telephone = Telephone
                fm.provenance = provenance
                fm.type_piece = type_piece
                fm.num_piece = num_piece
                fm.date_expire = date_expire
                fm.email = email
                fm.date_arriver = date_arriver
                fm.date_depart = date_depart
                fm.mode_paye = mode_paye
                fm.num_salle_id = id_salle
                fm.save()

                return redirect('reservations', id_salle=s.id)
        

    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()
    
    context = {
        'mail':mail,
        'Emp':Emp,
        's':s
    }
    return render(request, 'reservationSalle.html', context)


def reservations(request, id_salle):
    t = timezone.now()
    s = get_object_or_404(salle, id=id_salle)

    user = request.user
    mail = user.email

    Client = client.objects.filter(num_salle_id=s.id).first()
    Rest = restaurer.objects.filter(Restau_id__in=restaurant.objects.values_list('id', flat=True))

    date_depart_str = Client.date_depart
    date_arriver_str = Client.date_arriver

    # Conversion des chaînes en objets datetime
    date_depart = datetime.strptime(date_depart_str, "%Y-%m-%d")
    date_arriver = datetime.strptime(date_arriver_str, "%Y-%m-%d")

    nb_jour = (date_depart - date_arriver).days

    print(f"{s.prix_local}")
    print(f"{nb_jour}")

    s.prix_local = float(s.prix_local)

    pt = nb_jour * s.prix_local
    print(f"{pt}")

    if request.method == 'POST':
        sexe = request.POST.get('sexe')
        statut = request.POST.get('statut')
        nbr_personne = request.POST.get('nbr_personne')

        if sexe and statut:
             
            Reser = reserv()
            Reser.sexe = sexe
            Reser.jr = nb_jour
            Reser.statut = statut
            Reser.prix_total = pt
            Reser.Salle_id = id_salle
            Reser.Client_id = Client.id
            Reser.Emp_id = user.id
            Reser.restau_id = Rest.first().id if Rest.exists() else None
            Reser.date_reservation=t
            Reser.date_debut = Client.date_arriver
            Reser.date_fin = Client.date_depart
            Reser.mode_paiement = Client.mode_paye
            Reser.nbr_personne = nbr_personne

            Reser.save()

    Emp = employe.objects.filter(email=mail).first()

    context = {
        'mail':mail,
        'Emp':Emp,
        's':s,
        'Client':Client,
        'pt':pt,
        't':t
    }

    return render(request, 'reservations.html', context)


def info_salle(request, id_salle):

    s = get_object_or_404(salle, id=id_salle)
    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()

    context = {

        'mail':mail,
        'Emp':Emp,
        's':s
    }
    return render(request, 'info_salle.html', context)



def modifier(request, reserv_id):

    reservation = get_object_or_404(reserv, id=reserv_id)

    if request.method == "POST":
        form = ReservForm(request.POST, instance=reservation)
        
        if form.is_valid():
            form.save()

            return redirect('historique')
    else:
        form = ReservForm(instance=reservation)

    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()

    context = {
        'form': form,
        'mail':mail,
        'Emp':Emp
    }
    return render(request, 'modifierReservation.html', context)




def modifierfacture(request, id_client):
    reservation = get_object_or_404(facturier, id=id_client)

    if request.method == 'POST':
        form = FacturierForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('facture')
    else:
        form = FacturierForm(instance=reservation)
    
    user = request.user
    mail = user.email
    Emp = employe.objects.filter(email=mail).first()

    context = {
        'form': form,
        'mail':mail,
        'Emp':Emp
    }
    return render(request, 'modifierPaiement.html', context)


def register_administrateur(request):
    if request.method == 'POST':
        form = administrateurRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = administrateurRegistration()
    
    return render(request, 'administrateur.html', {'form': form})