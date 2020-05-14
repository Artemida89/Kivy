from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
GridLayout:
    rows: 2
    id: main_win
    Dropdown:
        id: dropdown
        Button:
            id: btn1
            text: 'option 1'
        Button:
            id: btn2
            text: 'option 2'
    BoxLayout:

    BoxLayout:
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return Builder.load_string(KV)


Test().run()