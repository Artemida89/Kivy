from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

KV = '''
<Drawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    
    #Верхняя часть
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        # логотип
        Image:
            id: avatar
            source: "kivymd_logo.png"

    # Данные Список текстов
    MDLabel:
        text: "АлюминикА"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    # ТО ЧТО БУДЕТ Скролить
    ScrollView:

        # Список меню
        MDList:

            # Меню №1
            OneLineListItem:
                text: "Меню 1"
                on_press:
                    # Закрытие Меню
                    root.nav_drawer.set_state("close")
                    # Открытие содержимого меню № 1
                    root.screen_manager.current = "scr 1"

            # Меню №2
            OneLineListItem:
                text: "Меню 2"
                on_press:
                    # Закрытие Меню
                    root.nav_drawer.set_state("close")
                    # Открытие содержимого меню № 2
                    root.screen_manager.current = "scr 2"


# Сам экран
Screen:
    # Панель меню
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Меню"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            
            Screen:
                # Данные меню №1 id = "scr 1"
                name: "scr 1"

                
                MDLabel:
                    text: "Screen 1"
                    halign: "center"
                    
                Button:
                    id: Button1
                    text: "Данные получить"
                    on_press:
                        # Открытие содержимого № 3
                        screen_manager.current = "scr 3"
                    
            Screen:
                # Данные меню №1 id = "scr 2"
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                    
            
            Screen:
                id: proba
                # Данные id = "scr 3"
                name: "scr 3"

                MDLabel:
                    text: "Данные получены"
                    halign: "center"
                    
            
        MDNavigationDrawer:
            id: nav_drawer

            Drawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                
                

'''


class Drawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Main1(MDApp):
    def build(self):
        return Builder.load_string(KV)


Main1().run()