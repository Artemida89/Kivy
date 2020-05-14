import kivy
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout


KV = '''

<MainWid>:
    ScrollView:
        GridLayout:
            id: container_y
            cols: 1
            row_default_height: root.height*0.2
            height: self.minimum_height
                
                    
        
'''

class MainWid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):

            self.ids.container_y.add_widget(Button())

    def build(self):
        return Builder.load_string(KV)


class ProbaApp(App):
    MainWid()


if __name__ == '__main__':
    ProbaApp().run()