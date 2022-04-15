
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, CardTransition
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class EjemploApp(App):
    def build(self):
        Window.size = (800,480)
        return layout

def cambiarPantalla(pantalla):
    sm.current = pantalla


url = 'http://192.168.3.10:8071'

layout = FloatLayout()
etiqueta1 = Label()
etiqueta2 = Label()

sm = ScreenManager(transition=CardTransition())
sm.size_hint = (1,.9)
sm.pos_hint = {'x':0,'y':0}

btn1 = Button()
btn1.text = 'IR A PANTALLA 1'
btn1.size_hint = (.5,.1)
btn1.pos_hint = {'x':0,'y':.9}
btn1.bind(on_press=lambda x: cambiarPantalla('pantalla1'))

btn2 = Button()
btn2.text = 'IR A PANTALL2'
btn2.size_hint = (.5,.1)
btn2.pos_hint = {'x':.5,'y':.9}
btn2.bind(on_press=lambda x: cambiarPantalla('pantalla2'))

etiqueta1.text = 'PANTALLA1'
etiqueta1.font_size = 30
etiqueta1.bold = True
etiqueta1.color = (1,0,0,1)

etiqueta2.text = 'PANTALLA2'
etiqueta2.font_size = 30
etiqueta2.bold = True
etiqueta2.color = (1,0,0,1)

screen1 = Screen(name='pantalla1')
screen1.pos_hint = {'x':0,'y':0}
screen1.size_hint = (1,.9)
screen1.add_widget(etiqueta1)

screen2 = Screen(name='pantalla2')
screen2.pos_hint = {'x':0,'y':0}
screen2.size_hint = (1,.9)
screen2.add_widget(etiqueta2)

sm.add_widget(screen1)
sm.add_widget(screen2)


layout.add_widget(btn1)
layout.add_widget(btn2)
layout.add_widget(sm)



if __name__ == '__main__':
    EjemploApp().run()


