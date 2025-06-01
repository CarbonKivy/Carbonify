from kivy.uix.recycleview import RecycleView

from carbonkivy.app import CarbonApp
from carbonkivy.theme.color_tokens import thematic_tokens, static_tokens

from View.base_screen import BaseScreenView


class ColorView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = CarbonApp.get_running_app()
        self.data = []
        tokenl = {}
        tokenl.update(thematic_tokens)
        tokenl.update(static_tokens)
        for token in tokenl.keys():
            if hasattr(self.app, token):
                self.data.extend([
                    {
                        "bg_color": getattr(self.app, token),
                        "token": token,
                    }
                ])


class ColorScreenView(BaseScreenView):
    def __init__(self, *args, **kwargs):
        super(ColorScreenView, self).__init__(*args, **kwargs)
