from kivy.uix.recycleview import RecycleView

from carbonkivy.theme.icons import ibm_icons

from View.base_screen import BaseScreenView


class IconView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        for icons in ibm_icons.keys():
            self.data.extend([{"icon": icons, "text": icons}])


class IconScreenView(BaseScreenView):

    def __init__(self, *args, **kwargs):
        self.icon_count = len(ibm_icons.keys())
        super(IconScreenView, self).__init__(*args, **kwargs)

