from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from Pantalla1 import *
from Pantalla2 import *

class Boton2(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'IR A 2'

    def on_press(self):
        cambiarPantalla('screen2')


class Boton1(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'IR A 1'

    def on_press(self):
        cambiarPantalla('screen1')






class EjemploApp(App):
    def build(self):
        Window.size = (800,480)

        return layout

def cambiarPantalla(nombrePantalla):
    sm.current = nombrePantalla


if __name__ == '__main__':
    layout = FloatLayout()
    layout.size_hint = (1,1)
    layout.pos_hint = {'x':0,'y':0}

    sm = ScreenManager()
    sm.size_hint = (1,.9)
    sm.pos_hint = {'x':0,'y':0}

    screen1 = Pantalla1(name='screen1')
    screen1.size_hint = (1, 1)
    screen1.pos_hint = {'x':0,'y':0}

    screen2 = Pantalla2(name='screen2')
    screen2.size_hint = (1, 1)
    screen2.pos_hint = {'x': 0, 'y': 0}

    sm.add_widget(screen1)
    sm.add_widget(screen2)

    sm.current = 'screen1'

    btn1 = Boton1()
    btn1.size_hint = (.5, .1)
    btn1.pos_hint = {'top': 1}


    btn2 = Boton2()
    btn2.size_hint = (.5, .1)
    btn2.pos_hint = {'top': 1, 'right':1}



    #INCLUIR OBJETO AL LAYOUT PRINCIPAL
    layout.add_widget(sm)
    #layout.add_widget(etiqueta)
    layout.add_widget(btn1)
    layout.add_widget(btn2)


    EjemploApp().run()