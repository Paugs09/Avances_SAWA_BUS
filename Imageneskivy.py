import kivy 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder


Builder.load_string(""" 

<KivyButton>:
    Button:
        
        text:'Haz click aquí'

        size_hint: .1, .1

        pos:(300,350)

        Image: 
                
            source:'bus.png'
            center_x: self.parent.center_x
            center_y: self.parent.center_y


""")

class KivyButton(App, BoxLayout):

    def build(self):

        return self

KivyButton().run()