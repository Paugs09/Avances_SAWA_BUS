import kivy 
from kivy.app import App
from kivy.uix.label import Label 

class KivyPrueba(App):

    def build(self):

        return Label(text="Hola SAWA BUS")

KivyPrueba().run()