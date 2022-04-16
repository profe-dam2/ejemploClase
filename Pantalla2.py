from threading import Thread
from time import sleep

from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from APIHandler import *

class Pantalla2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        fondo = Image(source='imagenes/FONDO2.jpg', keep_ratio=False,
                       allow_stretch=True)
        fondo.size_hint = self.size_hint
        fondo.pos_hint = self.pos_hint
        self.add_widget(fondo)
        etiqueta1 = Label(text='PANTALLA 2', color=(1,0,0,1), font_size=30,
                          bold=True, size_hint=(.5,.2),
                          pos_hint={'center_x': .5, 'center_y': .5})

        btnSecuencia = BotonSecuencia()
        btnSecuencia.pos_hint = {'center_x': .5, 'center_y': .5}
        btnSecuencia.size_hint = (.1, .2)

        self.imagenROJO = Image(source='imagenes/ledGRIS.png')
        self.imagenROJO.pos_hint = {'center_x': .75, 'center_y': .75}
        self.imagenROJO.size_hint = (.1, .2)
        self.imagenAMARILLO = Image(source='imagenes/ledGRIS.png')
        self.imagenAMARILLO.pos_hint = {'center_x': .75, 'center_y': .5}
        self.imagenAMARILLO.size_hint = (.1, .2)
        self.imagenVERDE = Image(source='imagenes/ledGRIS.png')
        self.imagenVERDE.pos_hint = {'center_x': .75, 'center_y': .25}
        self.imagenVERDE.size_hint = (.1, .2)

        self.add_widget(etiqueta1)
        self.add_widget(btnSecuencia)
        self.add_widget(self.imagenROJO)
        self.add_widget(self.imagenAMARILLO)
        self.add_widget(self.imagenVERDE)

class BotonSecuencia(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledROJO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0,0,0,0)
        self.threadSECUENCIA = Thread(target=self.secuencia, args=())
        self.killed = False

    def on_release(self):

        if self.threadSECUENCIA.is_alive():
            print("IS ALIVE")
            self.background_normal = 'imagenes/ledGRIS.png'
            self.killed = True
            #self.threadSECUENCIA.join()
        else:
            self.background_normal = 'imagenes/ledROJO.png'
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

            self.parent.imagenROJO.source= 'imagenes/ledROJO.png'
            self.parent.imagenAMARILLO.source = 'imagenes/ledGRIS.png'
            self.parent.imagenVERDE.source = 'imagenes/ledGRIS.png'


            sleep(3)
            request = {'led': 11, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 13, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 15, 'state': True}
            response = APIHandler().sendRequest(request)

            self.parent.imagenROJO.source = 'imagenes/ledGRIS.png'
            self.parent.imagenAMARILLO.source = 'imagenes/ledGRIS.png'
            self.parent.imagenVERDE.source = 'imagenes/ledVERDE.png'


            sleep(3)
            request = {'led': 11, 'state': False}
            response = APIHandler().sendRequest(request)
            request = {'led': 13, 'state': True}
            response = APIHandler().sendRequest(request)
            request = {'led': 15, 'state': False}
            response = APIHandler().sendRequest(request)

            self.parent.imagenROJO.source = 'imagenes/ledGRIS.png'
            self.parent.imagenAMARILLO.source = 'imagenes/ledAMARILLO.png'
            self.parent.imagenVERDE.source = 'imagenes/ledGRIS.png'


            sleep(1)

            self.secuencia()
        request = {'led': 13, 'state': False}
        response = APIHandler().sendRequest(request)