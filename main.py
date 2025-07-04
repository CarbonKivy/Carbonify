import os

import registers
import webbrowser

from kivy.clock import Clock
from kivy.core.window import Window

from carbonkivy.app import CarbonApp
from carbonkivy.utils import update_system_ui
# from carbonkivy.uix.screenmanager import CScreenManager

from View.components.LazyManager import LazyManager
from View.components.LoadingLayout import LoadingLayout
from View.screens import screens


def set_softinput(*args) -> None:
    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
    Window.softinput_mode = "below_target"


Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

from kivy.utils import platform
if platform == 'android':
    from libs.kivmob import KivMob, TestIds, RewardedListenerInterface

    
    class RewardsHandler(RewardedListenerInterface):
    
        def __init__(self, *args, **kwargs) -> None:
            super(RewardsHandler, self).__init__(*args, **kwargs)
    
        def on_rewarded(self, *args) -> None:
            CarbonApp.get_running_app().ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)


class UI(LazyManager):
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)
        self.raw_views = screens
        self.loading_layout = LoadingLayout()


class Carbonify(CarbonApp):
    def __init__(self, *args, **kwargs):
        super(Carbonify, self).__init__(*args, **kwargs)
        # self.load_all_kv_files(os.path.join(self.directory, "View"))
        self.manager_screens = UI()

    def build(self) -> UI:
        if platform == 'android':
            self.ads = KivMob(TestIds.APP)
            self.ads.new_banner(TestIds.BANNER,top_pos=False)
            self.ads.load_interstitial(TestIds.INTERSTITIAL)
            self.ads.set_rewarded_ad_listener(RewardsHandler())
        # self.generate_application_screens()
        self.manager_screens.switch("home screen")
        self.apply_styles()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        # adds different screen widgets to the screen manager

        for i, name_screen in enumerate(screens.keys()):
            view = screens[name_screen]["object"]()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def apply_styles(self, style: str = "White") -> None:
        self.theme = style
        update_system_ui(self.background, self.background, "Dark")

    def referrer(self, destination: str = None) -> None:
        if self.manager_screens.current != destination:
            self.manager_screens.switch(destination)

    def web_open(self, url: str) -> None:
        webbrowser.open_new_tab(url)

    def on_start(self, *args) -> None:
        Window.bind(on_keyboard=self.back_callback)

    def back_callback(self, window: Window, key: int, *args) -> bool | None:
        if key==27 or key==1001:
            if self.manager_screens.current == "home screen":
                return
            else:
                self.manager_screens.switch("home screen")
                return True


if __name__ == "__main__":
    import os, sys
    from kivy.resources import resource_add_path, resource_find

    if hasattr(sys, "_MEIPASS"):
        resource_add_path(resource_find(sys._MEIPASS))
    app = Carbonify()
    app.run()
