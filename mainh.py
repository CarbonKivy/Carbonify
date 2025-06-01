import importlib
import os, glob

from kivy import Config
from PIL import ImageGrab

resolution = ImageGrab.grab().size

# Change the values of the application window size as you need.
Config.set("graphics", "height", "700")
Config.set("graphics", "width", "350")

from kivy.core.window import Window

# Place the application window on the right side of the computer screen.
Window.top = 30
Window.left = resolution[0] - Window.width + 5

import webbrowser

from carbonkivy.app import CarbonApp
from carbonkivy.uix.screenmanager import CScreenManager

from kaki.app import App

import registers

class UI(CScreenManager):
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)


class Carbonify(App, CarbonApp):
    def __init__(self, *args, **kwargs):
        super(Carbonify, self).__init__(*args, **kwargs)
        self.DEBUG=True
        self.KV_FILES=[]
        for file in glob.glob(f"{self.directory}/View/**/*.kv", recursive=True):
            self.KV_FILES.append(file) # load all kv file in a certain directory
        self.CLASSES={
            "UI":"main" # main file name or root file name
        }
        self.AUTORELOADER_PATHS=[
            (".",{"recursive":True}),
        ]

    def build_app(self) -> UI:
        self.manager_screens = UI()
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Adds different screen widgets to the screen manager
        """
        import View.screens

        importlib.reload(View.screens)
        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            view = screens[name_screen]["object"]()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def apply_styles(self, style: str = "White") -> None:
        self.theme = style

    def referrer(self, destination: str = None) -> None:
        if self.manager_screens.current != destination:
            self.manager_screens.current = destination

    def web_open(self, url: str) -> None:
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    Carbonify().run()
