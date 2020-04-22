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
    
    
    GridLayout:
        
        rows: 2
        padding: 11
        spacing: 10
        size_hint: 0.7, 0.2
        #Input №1
        
        GridLayout:
            rows: 2
                    
            BoxLayout:
                padding: [0, 10, 0, 0]
                spacing: 5
                cols: 2
                MDRaisedButton:
                    text: "Click me!"
                    on_release: print("Hi!")
                MDRaisedButton:
                    text: "Click me!"
                    on_release: print("Hi!")
            
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: 10
                MDTextField:
                    hint_text: "Приход Денег"
                    mode: "rectangle"
                    multiline: False
                    font_size: 5
                    input_type: "number"
                    input_filter: "float"
                
    # Середина
    GridLayout:
        cols: 2
        size_hint: 1, 0.6
        BoxLayout:
            orientation: 'vertical'
        
            MDLabel:
                font_size: "15sp"
                text: "Январь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
            
            MDLabel:
                font_size: "15sp"
                text: "Февраль"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Март"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1

            MDLabel:
                font_size: "15sp"
                text: "Апрель"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Май"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Июнь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
        BoxLayout:
            orientation: 'vertical'
            
            MDLabel:
                font_size: "15sp"
                text: "Июль"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Август"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
            
            MDLabel:
                font_size: "15sp"
                text: "Сентябрь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1

            MDLabel:
                font_size: "15sp"
                text: "Октябрь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Ноябрь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "Декабрь"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1

    # Кнопки
    GridLayout:
        cols: 2
        size_hint: 1, 0.1
        
        BoxLayout:
            MDLabel:
                font_size: "10sp"
                text: "Сбережение"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                    
            MDLabel:
                font_size: "15sp"
                text: "0"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
            
        BoxLayout:
            MDLabel:
                font_size: "10sp"
                text: "Итого"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                
            MDLabel:
                font_size: "15sp"
                text: "0"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
    
    # Кнопки
    BoxLayout:
        spacing: 5
        cols: 2
        size_hint: 1, 0.1
        MDRaisedButton:
            text: "Click me!"
            on_release: print("Hi!")

        MDRaisedButton:
            text: "Click me!"
            on_release: print("Hi!")
"""


class MyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MyApp().run()
