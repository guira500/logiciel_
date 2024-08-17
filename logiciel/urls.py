from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import GeneratePdf

from logiciel.views import (
    log_in, dashboard, config, hotel, chmbre, restau, reservation, list_chbr, form, outil, travaux, personnel, log_out, nouveau_achat, entretenir, info_salle, modifier, register_administrateur,
    travail, employer, sign_in, info_chbr, occupe, custom, reserve, historique, resto, reglement, facture, envoimail, salles, reservationSalle, listeSalle, reservations, modifierfacture
)

urlpatterns = [
    path('', log_in, name='log_in'),
    path('bureau', dashboard, name='dashboard'),
    path('configuration', config, name='config'),
    path('hotel', hotel, name='hotel'),
    path('suite', chmbre, name='chambre'),
    path('conf', salles, name='salles'),
    path('restaurant', restau, name='restau'),
    path('reserver', reservation, name='reservation'),
    path('chambr', list_chbr, name='list_chbr'),
    path('salles', listeSalle, name='listeSalle'),
    path('formulaire_client/<int:id_chambre>', form, name='form'),
    path('formulaireClient/<int:id_salle>', reservationSalle, name='reservationSalle'),
    path('detail_chambre/<int:id_chambre>', info_chbr, name='info_chbr'),
    path('detail_salle/<int:id_salle>', info_salle, name='info_salle'),
    path('outils', outil, name='outil'),
    path('travaux', travaux, name='travaux'),
    path('personnel', personnel, name='personnel'),
    path('deconnexion', log_out, name='log_out'),
    path('achat', nouveau_achat, name='nouveau_achat'),
    path('entretien', entretenir, name='entretenir'),
    path('travail', travail, name='travail'),
    path('employer', employer, name='employer'),
    path('sign', sign_in, name='sign_in'),
    path('client',custom, name='custom'),
    path('occuper', occupe, name='occupe'),
    path('reserver/<int:id_chambre>', reserve, name='reserve'),
    path('reservation_salle/<int:id_salle>', reservations, name='reservations'),
    path('historiser/', historique, name='historique'),
    path('historiser/modifier/<int:reserv_id>/', modifier, name='modifier_reservation'),
    path('se-restaurer', resto, name='resto'),
    path('facture', reglement, name='reglement'),
    path('gestionnaire', register_administrateur, name='register_administrateur'),
    path('facture/<int:id_client>/', facture, name='facture'),
    path('facture/modifier/<int:id_client>/', modifierfacture, name='modifierfacture'),
    path('pdf/<int:id_client>', GeneratePdf.as_view(), name='cours_pdf'),
    path('pdf_email/<int:id_client>', envoimail, name='envoimail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)