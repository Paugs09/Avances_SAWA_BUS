import kivy
from kivy.app import App 
from kivy.uix.button import Button 

class miBoton(App):

    def build(self):

        return Button(text="Ingresar",background_color=(155,0,51,53))

miBoton().run()