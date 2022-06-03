import kivy
from kivy.app import App 
from kivy.uix.button import Button 
from functools import partial 

class miBoton(App):

    def disabled(self, instance, args):

        instance.disabled= True
    
    def update(self, instance, args):

        instance.text= "Estoy desabilitado"
    
    def build(self):
        
        mybtn= Button(text= "Haz click para desactivarse")

        mybtn.bind(on_press=partial(self.disabled, mybtn))

        mybtn.bind(on_press=partial(self.update, mybtn))

        return mybtn

miBoton().run()
