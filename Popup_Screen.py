from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

kv = '''

ScreenManagement:
    id: 'manager2'
    BrokenPopup:
        name: 'broken'
        manager2: 'manager2'

<BrokenPopup>:
    BoxLayout:
        Button:
            text: 'Test UP'
            on_release: root.p.open()

'''

class ScreenManagement(ScreenManager):
    pass

class BrokenPopup(Screen):

    def __init__(self, **kwargs):
        super(BrokenPopup,self).__init__(**kwargs)

        self.p = Popup(auto_dismiss=False, size_hint_x=.6, size_hint_y=None, title='Верх имя')
        self.g = GridLayout(cols=1, spacing=10)
        self.g.add_widget(Button(text='Test1!!!!!!', size_hint_y=None, height=32))
        self.g.add_widget(Button(text='Test2', size_hint_y=None, height=32))
        self.g.bind(minimum_height=self.g.setter('height'))
        self.p.add_widget(self.g)
        self.p.bind(height=self.g.setter('height')) #<- this does not work to change the popup height!

class TheApp(App):

    def build(self):
        return Builder.load_string(kv)

TheApp().run()