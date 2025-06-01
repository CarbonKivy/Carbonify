from View.LinkScreen.link_screen import LinkScreenView
from View.ButtonScreen.button_screen import ButtonScreenView
from View.TextinputScreen.textinput_screen import TextinputScreenView
from View.AdditionalScreen.additional_screen import AdditionalScreenView
from View.ColorScreen.color_screen import ColorScreenView
from View.IconScreen.icon_screen import IconScreenView
from View.LabelScreen.label_screen import LabelScreenView
from View.GridScreen.grid_screen import GridScreenView
from View.HomeScreen.home_screen import HomeScreenView
from View.AdmobScreen.admob_screen import AdmobScreenView

screens = {
    'home screen': {
        'object': HomeScreenView,
        'module': 'View.HomeScreen'
    },
    'link screen': {
        'object': LinkScreenView,
        'module': 'View.LinkScreen'
    },
    'button screen': {
        'object': ButtonScreenView,
        'module': 'View.ButtonScreen'
    },
    'textinput screen': {
        'object': TextinputScreenView,
        'module': 'View.TextinputScreen'
    },
    'additional screen': {
        'object': AdditionalScreenView,
        'module': 'View.AdditionalScreen'
    },
    'color screen': {
        'object': ColorScreenView,
        'module': 'View.ColorScreen'
    },
    'icon screen': {
        'object': IconScreenView,
        'module': 'View.IconScreen'
    },
    'label screen': {
        'object': LabelScreenView,
        'module': 'View.LabelScreen'
    },
    'grid screen': {
        'object': GridScreenView,
        'module': 'View.GridScreen'
    },
    'admob screen': {
        'object': AdmobScreenView,
        'module': 'View.AdmobScreen'
    },
}
