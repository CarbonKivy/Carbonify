from carbonkivy.utils import update_system_ui

from View.base_screen import BaseScreenView


class ProductScreenView(BaseScreenView):
    def __init__(self, *args, **kwargs):
        super(ProductScreenView, self).__init__(*args, **kwargs)

    def on_enter(self, *args):
        update_system_ui(self.app.layer_01, self.app.background, "Dark")

    def on_leave(self, *args):
        self.app.apply_styles()
