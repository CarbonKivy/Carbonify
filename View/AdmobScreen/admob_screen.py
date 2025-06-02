from kivy.app import App
from kivy.utils import platform

from View.base_screen import BaseScreenView

if platform == 'android':
    from libs.kivmob import TestIds, RewardedListenerInterface

    class RewardsHandler(RewardedListenerInterface):

        def __init__(self, *args, **kwargs) -> None:
            super(AdmobScreenView, self).__init__(*args, **kwargs)

        def on_rewarded(self, *args) -> None:
            App.get_running_app().ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)

class AdmobScreenView(BaseScreenView):

    def __init__(self, *args, **kwargs) -> None:
        super(AdmobScreenView, self).__init__(*args, **kwargs)

    def on_pre_enter(self, *args) -> None:
        if platform == 'android':
            try:
                self.app.ads.request_banner()
            except Exception: # nosec
                pass

            try:
                self.app.ads.load_interstitial(TestIds.INTERSTITIAL)
            except Exception: # nosec
                pass

            try:
                self.app.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)
                self.ads.set_rewarded_ad_listener(RewardsHandler())
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
