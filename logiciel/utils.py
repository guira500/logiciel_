""" from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import os
from django.conf import settings


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    output_path = os.path.join(settings.BASE_DIR, 'static', 'chargement')
    
    # Assurez-vous que le dossier 'static/chargement' existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    pdf_file_path = os.path.join(output_path, 'temp_pdf.pdf')
    result = open(pdf_file_path, 'wb')  # Chemin temporaire pour stocker le PDF généré
    pisa_status = pisa.CreatePDF(html.encode("UTF-8"), dest=result, encoding='UTF-8')
    result.close()

    if pisa_status.err:
        return HttpResponse('nous avons rencontré une erreur <pre>' + html + '</pre>')
    else:
        with open(pdf_file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="facture.pdf"'
        os.remove(pdf_file_path)  # Supprimez le fichier temporaire
        return response
     """


from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import os
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    output_path = os.path.join(settings.BASE_DIR, 'static', 'chargement')

    # Assurez-vous que le dossier 'static/chargement' existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    pdf_file_path = os.path.join(output_path, 'temp_pdf.pdf')

    try:
        # Créez un contexte de gestion pour assurer la fermeture du fichier
        with open(pdf_file_path, 'wb') as result:
            pisa_status = pisa.CreatePDF(html.encode("UTF-8"), dest=result, encoding='UTF-8')

        # Vérifiez le statut de la création du PDF
        if pisa_status.err:
            return None
        else:
            return pdf_file_path
    except Exception as e:
        print(f"Exception lors de la génération du PDF : {e}")
        return None 



""" def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    output_path = os.path.join(settings.BASE_DIR, 'static', 'chargement')

    # Assurez-vous que le dossier 'static/chargement' existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    pdf_file_path = os.path.join(output_path, 'temp_pdf.pdf')

    try:
        with open(pdf_file_path, 'wb') as result:
            pisa_status = pisa.CreatePDF(html.encode("UTF-8"), dest=result, encoding='UTF-8')

        if pisa_status.err:
            return None
        else:
            with open(pdf_file_path, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="facture.pdf"'
            os.remove(pdf_file_path)
            return response
    except Exception as e:
        print(f"Exception lors de la génération du PDF : {e}")
        return None """
