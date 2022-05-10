from threading import Timer
from hubspot.crm.objects import ApiException
from hubspot.crm.contacts.exceptions import ApiException
from hubspot.crm.contacts import SimplePublicObjectInput
from django.http import JsonResponse
import requests
import time
import json
from django.http import JsonResponse
from hubspot import HubSpot
# Token
from hubspot.auth.oauth import ApiException
from django.core import serializers


api_client = HubSpot()
api_client = HubSpot(api_key='22566d87-b1c4-4e7e-aa84-d0d72b9a4887')
print(api_client)


def CreateContact(self):
    try:
        simple_public_object_input = SimplePublicObjectInput(
            properties={"email": "jorge@gmail.com.co"}
        )
        api_response = api_client.crm.contacts.basic_api.create(
            simple_public_object_input=simple_public_object_input
        )
    except ApiException as e:
        print("Exception when creating contact: %s\n" % e)


    responseData = {
        'url': "Contacto creado con exito"        
    }

    return JsonResponse(responseData)

def CreateTiket(self):
    try:
        simple_public_object_input = SimplePublicObjectInput(
            properties={
                "content": "",
                "hs_pipeline": "0",
                "hs_pipeline_stage": "1",
                "subject": "Creando ticket desde una view"
            }
        )
        api_response = api_client.crm.tickets.basic_api.create(
            simple_public_object_input=simple_public_object_input
        )
    except ApiException as e:
        print("Exception when creating contact: %s\n" % e)

    responseData = {
        'url': "Ticket creado exitosamente"        
    }

    return JsonResponse(responseData)

def ListTikets(self):
    all_tikets = api_client.crm.tickets.get_all()
    print(all_tikets)

    return JsonResponse({"models_to_return": "Lista de tikets cargada"})


def ListContacts(self):
    all_contacts = api_client.crm.contacts.get_all()
    print(all_contacts)

    return JsonResponse({"models_to_return": "Lista de contactos cargada"})









# try:
#     tokens = api_client.auth.oauth.tokens_api.create_token(
#         grant_type="authorization_code",
#         redirect_uri='http://localhost',
#         client_id='client_id',
#         client_secret='client_secret',
#         code='code'
#     )
#     print(" ***** TOKENS: ===> ",tokens)
# except ApiException as e:
#     print("Exception when calling create_token method: %s\n" % e)


# all_contacts = api_client.crm.tickets.get_all()
# print(all_contacts)


# test=requests.post("https://api.hubapi.com/crm-objects/v1/objects/tickets?hapikey=22566d87-b1c4-4e7e-aa84-d0d72b9a4887")
# print("TEST ****: ",test)


def TestApp(self):

    responseData = {
        'url': "oki"
    }

    return JsonResponse(responseData)
