import kivy 
from kivy.app import App 
from kivy.uix.button import Label 

class KivyLabel(App):
    
    def build(self):
        return Label (text="[u][color=ff0066][b]Bienvenidos[/b][/color] a [i][color=ff0033] SAWA[/i] BUS[/color][/u]",markup=True)

KivyLabel().run() 

