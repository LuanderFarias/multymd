from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from tkinter import *
from tkinter import filedialog
import ctypes
from pynput import keyboard

KV = '''

GerenciadorDeTelas:
    TelaMain:
    Menu:
    Wallpaper:
    Keys:
    Files:
    Music:

<TelaMain>: 
    BoxLayout:
        Menu:

<Menu>:
    name: 'Menu'
    MDIcon:
        id: 'icon'
        pos_hint:{'center_x': .5, 'center_y': .8}
        icon: 'application-array'
        font_size: '85sp'
    
    MDLabel:
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .7}
        text: 'MultyMD'
        text_color: "white"
        font_style: 'H4'

    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .6}
        text: 'Wallpaper'
        md_bg_color: 'white'
        on_release: app.root.current = 'Wallpaper'

    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .5}
        text: 'Keys'
        md_bg_color: 'white'
        on_release: app.root.current = 'Keys'
    
    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .4}
        text: 'Files'
        md_bg_color: 'white'
        on_release: app.root.current = 'Files'

    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .3}
        text: 'Music'
        md_bg_color: 'white'
        on_release: app.root.current = 'Music'

    MDLabel:
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .1}
        text: 'Made By: @LuanderFarias'
        text_color: "white"
    
    MDIconButton:
        pos_hint:{'center_x': .9, 'center_y': .1}
        icon: 'github'
        on_release:
            import webbrowser
            webbrowser.open('http://www.github.com/luanderfarias/multymd')
    
    MDIconButton:
        pos_hint:{'center_x': .8, 'center_y': .1}
        icon: 'instagram'
        on_release:
            import webbrowser
            webbrowser.open('https://www.instagram.com/luanderfarias/')

    MDIconButton:
        pos_hint:{'center_x': .1, 'center_y': .1}
        icon: 'white-balance-sunny'
        on_press:
            app.LightTheme()

    MDIconButton:
        pos_hint:{'center_x': .2, 'center_y': .1}
        icon: 'weather-night'
        on_press:
            app.DarkTheme()

<Wallpaper>:
    name: 'Wallpaper'
    MDRaisedButton:
        size_hint_x: .5
        pos_hint:{'center_x': .5, 'center_y': .6}
        text: 'Select File'
        md_bg_color: 'white'
        on_press:
            app.browseFiles()
    
    MDRaisedButton:
        size_hint_x: .5
        pos_hint:{'center_x': .5, 'center_y': .5}
        text: 'Apply'
        md_bg_color: 'white'
        on_press:
            app.change_wall()
    
    MDRaisedButton:
        pos_hint:{'center_x': .1, 'center_y': .9}
        text: '<'
        on_release: app.root.current = 'Menu'
        md_bg_color: 'red'
    
    MDLabel:
        pos_hint: {"center_x": .5, "center_y": .4}
        halign: "center"
        text: 'Support for .png, .jpeg and .img'
        text_color: 'gray'

<Keys>:
    name: 'Keys'
    MDLabel:
        halign: "center"
        text: 'Your pressed key is:'
    
    MDRaisedButton:
        pos_hint:{'center_x': .1, 'center_y': .9}
        text: '<'
        on_release: app.root.current = 'Menu'
        md_bg_color: 'red'

<Files>:
    name: 'Files'
    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .3}
        text: 'Upload a File'
    
    MDRaisedButton:
        pos_hint:{'center_x': .1, 'center_y': .9}
        text: '<'
        on_release: app.root.current = 'Menu'
        md_bg_color: 'red'

<Music>:
    name: 'Music'
    MDRaisedButton:
        size_hint_x: .3
        pos_hint:{'center_x': .5, 'center_y': .3}
        text: 'Play'
    
    MDRaisedButton:
        pos_hint:{'center_x': .1, 'center_y': .9}
        text: '<'
        on_release: app.root.current = 'Menu'
        md_bg_color: 'red'
    
    MDLabel:
        halign: "center"
        text: 'Library'
'''

class GerenciadorDeTelas(ScreenManager):
    pass

class TelaMain(Screen):
    pass

class Menu(Screen):
    pass

class Wallpaper(Screen):
    pass

class Keys(Screen):
    pass

class Files(Screen):
    pass

class Music(Screen):
    pass

class MeuApp(MDApp):
    dialog = None
    def build(self):
        self.title = 'MultyMD'
        self.icon = 'icon.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_string(KV)
    
    # Color Themes
    def LightTheme(self):
        self.theme_cls.theme_style = 'Light'
    
    def DarkTheme(self):
        self.theme_cls.theme_style = 'Dark'
    
    # Wallpaper
    def close_dialog(self, obj):
        self.dialog.dismiss()

    def browseFiles(self):
        global filename
        global path

        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        path = filename

    def change_wall(self):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            self.dialog = MDDialog(
                title = "Wallpaper Changed.",
                buttons =[
                    MDRectangleFlatButton(
                        text="ok", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                    )
                ]
            )

            self.dialog.open()
        except:
            self.dialog = MDDialog(
                title = "Archive Not Selected",
                buttons =[
                    MDRectangleFlatButton(
                        text="Retry", text_color=self.theme_cls.primary_color, on_release = self.close_dialog
                    )
                ]
            )

            self.dialog.open()

    
    # Keys
    def on_press(key):
        print(key)
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

MeuApp().run()