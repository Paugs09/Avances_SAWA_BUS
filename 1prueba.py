import kivy
kivy.require('1.9.0')
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 

class Contenedor_01(BoxLayout):
    None

class MainApp(App):
    tittle="Hola mundo"
    def build(self):
        return Contenedor_01()

MainApp().run()    