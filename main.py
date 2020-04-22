from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.config import Config

Config.set("kivy", "keyboard_mode", "systemanddock")

Window.size = (360, 600)


root_kv = """
GridLayout:
    rows: 5
    padding: 10

    BoxLayout:
        padding: 15
        spacing: 15
        cols: 2
        size_hint: 1, 0.05
        Label:
            font_size: "15sp"
            text: "Dohod"
        Label:
            font_size: "15sp"
            text: "Rashod"

    BoxLayout:
        padding: 15
        spacing: 5
        cols: 2
        size_hint: 1, 0.1
        TextInput:
            multiline: False
            font_size: 14
            input_type: "number"
            input_filter: "float"
        TextInput:
            multiline: False
            font_size: 14
            input_type: "number"
            input_filter: "float"

    GridLayout:
        cols: 2
        size_hint: 1, 0.75
        BoxLayout:
            orientation: 'vertical'

            Label:
                font_size: "15sp"
                text: "Yanvar`"
            CheckBox:
                group: 'check'
            Label:
                font_size: "15sp"
                text: "Fevral`"
            Label:
                font_size: "15sp"
                text: "Mart"

            Label:
                font_size: "15sp"
                text: "Aprel`"
            Label:
                font_size: "15sp"
                text: "May"
            Label:
                font_size: "15sp"
                text: "Iyun`"
        BoxLayout:
            orientation: 'vertical'

            Label:
                font_size: "15sp"
                text: "Iyul`"
            Label:
                font_size: "15sp"
                text: "Avgust"
            Label:
                font_size: "15sp"
                text: "Sentabr`"

            Label:
                font_size: "15sp"
                text: "Oktyabr`"
            Label:
                font_size: "15sp"
                text: "Noyabr`"
            Label:
                font_size: "15sp"
                text: "Dekabr`"

    BoxLayout:
        padding: 15
        spacing: 5
        cols: 2
        size_hint: 1, 0.05
        Label:
            font_size: "15sp"
            text: "Zberezenie"
        Label:
            font_size: "15sp"
            text: "Itogo"

    BoxLayout:
        padding: 15
        spacing: 5
        cols: 2
        size_hint: 1, 0.05
        MDRaisedButton:
            text: "Click me!"
            on_release: print("Hi!")

        Button:
            text: "Расход menu"
"""


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MyApp().run()