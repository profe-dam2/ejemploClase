import json
import datetime
from hashlib import sha256
import asynckivy as ak
import ResponseModel
from ResponseModel import *
import requests
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

url = 'http://192.168.1.116:8071'

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

        btnROJO = Button()
        btnROJO.pos_hint = {'center_x':.25, 'center_y':.5}
        btnROJO.size_hint = (.15,.2)



        btnROJO.bind(on_press=lambda x:self.EjecutarAccion2())

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


    def EjecutarAccion2(self):
        print('PRESIONANDO')
        USER = '1damX'
        PASS = '1234'
        passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
        minutes = str(datetime.datetime.now().minute)
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
        requestModel = {'led': 11, 'state': None}
        response = requests.post(url + '/raspberrySemaforo1',
                                 data=json.dumps(requestModel),
                                 headers={"Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        print(responseJSON['data'])
        if responseJSON['data']:
            requestModel = {'led': 11, 'state': False}
        else:
            requestModel = {'led': 11, 'state': True}

        response = requests.post(url + '/raspberrySemaforo1',
                                 data=json.dumps(requestModel),
                                 headers={
                                     "Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256))

    def EjecutarAccion(self, accion, color):
        self.etiqueta2.text = accion
        self.etiqueta2.color = color

        # if color == 'verde':
        #     self.etiqueta2.color = (0,1,0,1)
        # elif color == 'rojo':
        #     self.etiqueta2.color = (1,0,0,1)
        # else:
        #     self.etiqueta2.color = (1,1,0,1)



class BotonRojo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('INICIA')
        self.background_normal = 'imagenes/ledROJO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)
        #await ak.event(self, 'on_press')



    def on_touch_down(self, touch):
        if touch.grab is not self:
            print('PRESIONANDO')
            USER = '1damX'
            PASS = '1234'
            passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
            minutes = str(datetime.datetime.now().minute)
            tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
            tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
            requestModel = {'led': 11, 'state':None}
            response = requests.post(url + '/raspberrySemaforo1', data=json.dumps(requestModel),
                              headers={"Content-Type": "application/json"},
                              auth=(USER, tokenSHA256)).json()

            responseJSON = json.loads(response['response'])
            print(responseJSON['data'])
            if responseJSON['data'] :
                requestModel = {'led': 11, 'state': False}
            else:
                requestModel = {'led': 11, 'state': True}

            response = requests.post(url + '/raspberrySemaforo1',
                                     data=json.dumps(requestModel),
                                     headers={
                                         "Content-Type": "application/json"},
                                     auth=(USER, tokenSHA256))






class BotonAmarillo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledAMARILLO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)

    def on_press(self):
        USER = '1damX'
        PASS = '1234'
        passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
        minutes = str(datetime.datetime.now().minute)
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
        requestModel = {'led': 13, 'state':None}
        response = requests.post(url + '/raspberrySemaforo1', data=json.dumps(requestModel),
                          headers={"Content-Type": "application/json"},
                          auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        print(responseJSON['data'])
        if responseJSON['data'] :
            requestModel = {'led': 13, 'state': False}
        else:
            requestModel = {'led': 13, 'state': True}

        response = requests.post(url + '/raspberrySemaforo1',
                                 data=json.dumps(requestModel),
                                 headers={
                                     "Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256))

class BotonVerde(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledVERDE.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)


    def on_press(self):
        USER = '1damX'
        PASS = '1234'
        passSHA256 = sha256(PASS.encode('utf-8')).hexdigest()
        minutes = str(datetime.datetime.now().minute)
        tokenString = USER + '/raspberrySemaforo1' + passSHA256 + minutes
        tokenSHA256 = sha256(tokenString.encode('utf-8')).hexdigest()
        requestModel = {'led': 15, 'state':None}
        response = requests.post(url + '/raspberrySemaforo1', data=json.dumps(requestModel),
                          headers={"Content-Type": "application/json"},
                          auth=(USER, tokenSHA256)).json()

        responseJSON = json.loads(response['response'])
        print(responseJSON['data'])
        if responseJSON['data'] :
            requestModel = {'led': 15, 'state': False}
        else:
            requestModel = {'led': 15, 'state': True}

        response = requests.post(url + '/raspberrySemaforo1',
                                 data=json.dumps(requestModel),
                                 headers={
                                     "Content-Type": "application/json"},
                                 auth=(USER, tokenSHA256))