from kivy.clock import Clock
from kivy.utils import platform

from View.base_screen import BaseScreenView

if platform == 'android':
    from libs.kivmob import TestIds


class AdmobScreenView(BaseScreenView):

    def __init__(self, *args, **kwargs) -> None:
        super(AdmobScreenView, self).__init__(*args, **kwargs)

    def on_pre_enter(self, *args) -> None:
        if platform == 'android':
            try:
                self.app.ads.request_banner()
            except Exception: # nosec
                pass

    def on_enter(self, *args) -> None:
        if platform == 'android':

            try:
                self.app.ads.show_banner()
            except Exception: # nosec
                pass

            try:
                self.app.ads.show_interstitial()
            except Exception: # nosec
                pass

            try:
                self.app.ads.show_rewarded_ad()
            except Exception: # nosec
                pass

    def on_leave(self, *args) -> None:
        if platform == 'android':

            try:
                self.app.ads.hide_banner()
                self.app.ads.load_interstitial(TestIds.INTERSTITIAL)
                self.app.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)
            except Exception: # nosec
                pass

    def refresh_ads(self, type: str) -> None:
        if platform == 'android':
            try:
                if type == "interstitial":
                    self.app.ads.load_interstitial(TestIds.INTERSTITIAL)
                    Clock.schedule_once(
                        lambda e: self.app.ads.show_interstitial(),
                        2
                    )
                elif type == "rewarded":
                    self.app.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)
                    Clock.schedule_once(
                        lambda e: self.app.ads.show_rewarded_ad(),
                        2
                    )
            except Exception: # nosec
                pass
            
