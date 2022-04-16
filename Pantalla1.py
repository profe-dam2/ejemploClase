import json
import datetime
from hashlib import sha256
from threading import Thread
from time import sleep

import asynckivy as ak

from APIHandler import *
import ResponseModel
from ResponseModel import *
import requests
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

URL = 'http://192.168.1.116:8071'
USER = '1damX'
PASS = '1234'
passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
minutes = str(datetime.datetime.now().minute)


class Pantalla1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        fondo = Image(source='imagenes/FONDO1.jpg', keep_ratio=False,
                       allow_stretch=True)
        fondo.size_hint = self.size_hint
        fondo.pos_hint = self.pos_hint
        self.add_widget(fondo)
        etiqueta1 = Label(text='PANTALLA 1', color=(1,0,0,1), font_size=30,
                          bold=True, size_hint=(.5,.2),
                          pos_hint={'top': 1, 'center_x': .5})

        self.etiqueta2 = Label(text='Accion', color=(0, 1, 0, 1), font_size=20,
                          bold=True, size_hint=(.5, .2),
                          pos_hint={'bottom': 1, 'center_x': .5})

        btnROJO = BotonRojo()
        btnROJO.pos_hint = {'center_x':.25, 'center_y':.5}
        btnROJO.size_hint = (.15,.2)


        #btnROJO.bind(on_press=lambda x: )

        btnAMARILLO = BotonAmarillo()
        btnAMARILLO.pos_hint = {'center_x': .5, 'center_y': .5}
        btnAMARILLO.size_hint = (.15, .2)
        btnAMARILLO.bind(
            on_press=lambda x: self.EjecutarAccion('Has pulsado AMARILLO',(1,1,0,1)))

        btnVERDE = BotonVerde()
        btnVERDE.pos_hint = {'center_x': .75, 'center_y': .5}
        btnVERDE.size_hint = (.15, .2)
        btnVERDE.bind(on_press=lambda x:self.EjecutarAccion('Has pulsado VERDE',(0,1,0,1)))

        self.add_widget(btnROJO)
        self.add_widget(btnAMARILLO)
        self.add_widget(btnVERDE)
        self.add_widget(etiqueta1)
        self.add_widget(self.etiqueta2)

    def EjecutarAccion(self, accion, color):
        self.etiqueta2.text = accion
        self.etiqueta2.color = color



class BotonRojo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledROJO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)
        self.threadSECUENCIA = Thread(target=self.secuencia, args=())
        self.killed = False

    def on_release(self):

        # request = {'led': 11, 'state': None}
        # response = APIHandler().sendRequest(request)
        #
        # if response['data']:
        #     request = {'led': 11, 'state': False}
        # else:
        #     request = {'led': 11, 'state': True}
        #
        # response = APIHandler().sendRequest(request)



        if self.threadSECUENCIA.is_alive():
            print("IS ALIVE")
            self.killed = True
            #self.threadSECUENCIA.join()
        else:
            self.killed = False
            self.threadSECUENCIA = Thread(target=self.secuencia, args=())
            self.threadSECUENCIA.start()


    def secuencia(self):
        while not self.killed:
            request = {'led': 11, 'state': True}
            response = APIHandler().sendRequest(request)
            request = {'led': 13, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 15, 'state': False}
            response = APIHandler().sendRequest(request)

            sleep(3)
            request = {'led': 11, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 13, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 15, 'state': True}
            response = APIHandler().sendRequest(request)

            sleep(3)
            request = {'led': 11, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 13, 'state': True}
            response = APIHandler().sendRequest(request)
            request = {'led': 15, 'state': False}
            response = APIHandler().sendRequest(request)

            sleep(1)

            self.secuencia()


class BotonAmarillo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledAMARILLO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)

    def on_release(self):
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
        request = {'led': 13, 'state':None}
        response = requests.post(URL + '/raspberrySemaforo1', data=json.dumps(request),
                          headers={"Content-Type": "application/json"},
                          auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        print(responseJSON['data'])
        if responseJSON['data'] :
            request = {'led': 13, 'state': False}
        else:
            request = {'led': 13, 'state': True}

        response = requests.post(URL + '/raspberrySemaforo1',
                                 data=json.dumps(request),
                                 headers={
                                     "Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256))

class BotonVerde(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledVERDE.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)


    def on_release(self):
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
        request = {'led': 15, 'state':None}
        response = requests.post(URL + '/raspberrySemaforo1', data=json.dumps(request),
                          headers={"Content-Type": "application/json"},
                          auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        print(responseJSON['data'])
        if responseJSON['data'] :
            request = {'led': 15, 'state': False}
        else:
            request = {'led': 15, 'state': True}

        response = requests.post(URL + '/raspberrySemaforo1',
                                 data=json.dumps(request),
                                 headers={
                                     "Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256))