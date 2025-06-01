from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class CircularLoader(Widget):

    angle = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(CircularLoader, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        self.angle = (self.angle + 6) % 360

