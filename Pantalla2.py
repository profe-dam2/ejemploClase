from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


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
        self.add_widget(etiqueta1)