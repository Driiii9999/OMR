from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
Window.size = (310, 580)

kv = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    ScreenManager:
        id: scr
        transition: NoTransition()
        MDScreen:
            name: "home"
            MDLabel:
                text: "Home"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "key"
            MDLabel:
                text: "Answer Key"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "scan"
            MDLabel:
                text: "Scanner"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "sheet"
            MDLabel:
                text: "Sheet"
                pos_hint: {"center_y": .5}
                halign: "center"
            MDCard:
                size_hint: None, None
                size: "300dp", "90dp"
                pos_hint: {"center_x": .5, "center_y": .90}
                elevation: 1
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                MDLabel:
                    text: "Answer Sheet 1-20"
                    font_size: "18sp"
                    halign: "center"
                MDRaisedButton:
                    text: "Download PDF"
                    pos_hint: {"center_x": .5}
                    on_release:
                        app.download_pdf()
            MDCard:
                size_hint: None, None
                size: "300dp", "90dp"
                pos_hint: {"center_x": .5, "center_y": .73}
                elevation: 1
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                MDLabel:
                    text: "Answer Sheet 1-20"
                    font_size: "18sp"
                    halign: "center"
                MDRaisedButton:
                    text: "Download PDF"
                    pos_hint: {"center_x": .5}
                    on_release:
                        app.download_pdf()
        
        MDScreen:
            name: "profile"
            MDLabel:
                text: "Profile"
                pos_hint: {"center_y": .5}
                halign: "center"
    NavBar:
        size_hint: 1, .1
        pos_hint: {"center_x": .5, "center_y": .05}
        elevation: .3
        md_bg_color: 1, 1, 1, 1
        radius: [5]
        MDGridLayout:
            cols: 5
            size_hint_x: .9
            spacing: 8
            pos_hint: {"center_x": .5, "center_y": .5}
            MDIconButton:
                id: nav_icon1
                icon: "account-group-outline"
                ripple_scale: 0
                user_font_size: "40sp"
                theme_text_color: "Custom"
                text_color: 102/255, 154/255, 204/255, 1
                on_release:
                    scr.current = "home"
            MDIconButton:
                id: nav_icon2
                icon: "cellphone-key"
                ripple_scale: 0
                user_font_size: "40sp"
                theme_text_color: "Custom"
                text_color: 102/255, 154/255, 204/255, 1
                on_release:
                    scr.current = "key"
            MDIconButton:
                id: nav_icon3
                icon: "line-scan"
                ripple_scale: 0
                user_font_size: "40sp"
                theme_text_color: "Custom"
                text_color: 102/255, 154/255, 204/255, 1
                on_release:
                    scr.current = "scan"
            MDIconButton:
                id: nav_icon4
                icon: "printer-outline"
                ripple_scale: 0
                user_font_size: "40sp"
                theme_text_color: "Custom"
                text_color: 102/255, 154/255, 204/255, 1
                on_release:
                    scr.current = "sheet"
            MDIconButton:
                id: nav_icon5
                icon: "account-outline"
                ripple_scale: 0
                user_font_size: "40sp"
                theme_text_color: "Custom"
                text_color: 102/255, 154/255, 204/255, 1
                on_release:
                    scr.current = "profile"
"""

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class BottomNavBar(MDApp):

    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    BottomNavBar().run()