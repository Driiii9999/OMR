from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
Window.size = (310, 580)


# kv = """
# MDScreen:
#     name: "login"
#     MDFloatLayout:
#         md_bg_color: 1, 1, 1, 1
#         MDIconButton:
#             icon: "arrow-left"
#             pos_hint: {"center_y": .95}
#             user_font_size: "30sp"
#             theme_text_color: "Custom"
#             text_color: rgba(26, 24, 58, 255)
#             on_release:
#                 root.manager.transition.direction = "right"
#                 root.manager.current = "main"
#         MDLabel:
#             text: "LOGIN"
#             font_name: "BPoppins"
#             font_size: "26sp"
#             pos_hint: {"center_x": .6, "center_y": .85}
#             color: 0/255, 59/255, 109/255, 1
#         MDLabel:
#             text: "Sign In to continue"
#             font_name: "MPoppins"
#             font_size: "18sp"
#             pos_hint: {"center_x": .6, "center_y": .79}
#             color: rgba(135, 135, 135, 255)
#         MDFloatLayout:
#             size_hint: .7, .07
#             pos_hint: {"center_x": .5, "center_y": .63}
#             TextInput:
#                 id: email
#                 hint_text: "Email"
#                 font_name: "MPoppins"
#                 pos_hint: {"center_x": .43, "center_y": .5}
#                 background_color: 1, 1, 1, 0
#                 foreground_color: rgba(0, 0, 59, 255)
#                 cursor_color: rgba(0, 0, 59, 255)
#                 font_size: "14sp"
#                 cursor_width: "2sp"
#                 multiline: False
#             MDFloatLayout:
#                 pos_hint: {"center_x": .45, "center_y": .20}
#                 size_hint_y: .03
#                 md_bg_color: rgba(178, 178, 178, 255)
#         MDFloatLayout:
#             size_hint: .7, .07
#             pos_hint: {"center_x": .5, "center_y": .5}
#             TextInput:
#                 id: password
#                 hint_text: "Password"
#                 font_name: "MPoppins"
#                 pos_hint: {"center_x": .43, "center_y": .5}
#                 background_color: 1, 1, 1, 0
#                 foreground_color: rgba(0, 0, 59, 255)
#                 cursor_color: rgba(0, 0, 59, 255)
#                 font_size: "14sp"
#                 cursor_width: "2sp"
#                 multiline: False
#                 password: True
#             MDFloatLayout:
#                 pos_hint: {"center_x": .45, "center_y": .20}
#                 size_hint_y: .03
#                 md_bg_color: rgba(178, 178, 178, 255)
#         Button:
#             text: "LOGIN"
#             size_hint: .80, .075
#             pos_hint: {"center_x": .5, "center_y": .34}
#             background_color: 0, 0, 0, 0
#             font_name: "BPoppins"
#             on_release:
#                 app.verify_data(email.text, password.text)
#                 root.manager.transition.direction = "left"
#                 root.manager.current = "login"
#
#             canvas.before:
#                 Color:
#                     rgba: 102/255, 154/255, 204/255, 1
#                 RoundedRectangle:
#                     size: self.size
#                     pos: self.pos
#                     radius: [5]
#         MDTextButton:
#             text: "Forgot Password?"
#             pos_hint: {"center_x": .5, "center_y": .26}
#             font_size: "12sp"
#             font_name: "BPoppins"
#             canvas.before:
#                 Color:
#                     rgba: 102/255, 154/255, 204/255, 1
#         MDLabel:
#             text: "or login with"
#             color: 102/255, 154/255, 204/255, 1
#             pos_hint: {"center_y": .19}
#             font_size: "13sp"
#             font_name: "BPoppins"
#             halign: "center"
#         MDFloatLayout:
#             md_bg_color: rgba(178, 178, 178, 255)
#             size_hint: .25, .002
#             pos_hint: {"center_x": .2, "center_y": .188}
#         MDFloatLayout:
#             md_bg_color: rgba(178, 178, 178, 255)
#             size_hint: .25, .002
#             pos_hint: {"center_x": .8, "center_y": .188}
#         MDGridLayout:
#             cols: 1
#             size_hint: .48, .07
#             pos_hint: {"center_x": .5, "center_y": .113}
#             Image:
#                 source: "E:\google.png"
#         MDLabel:
#             text: "Don't have an account?"
#             font_name: "BPoppins"
#             font_size: "11sp"
#             pos_hint: {"center_x": .68, "center_y": .04}
#             color: rgba(135, 133, 133, 255)
#         MDTextButton:
#             text: "Sign up"
#             font_name: "BPoppins"
#             font_size: "11sp"
#             pos_hint: {"center_x": .75, "center_y": .04}
#             color: rgba(0, 59, 109, 255)
#             on_release:
#                 root.manager.transition.direction = "left"
#                 root.manager.current = "signup"
# """
class OptiCheck(MDApp):

    def build(self):
        # return Builder.load_string(kv)
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("resetpass.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("resetpass.kv"))
        return screen_manager

    # def verify_data(self, email, password):
    #     from firebase import firebase
    #
    #     # Initialize Firebase
    #     firebase = firebase.FirebaseApplication('https://test-a1fc4-default-rtdb.firebaseio.com/', None)
    #
    #     # Get data from Firebase
    #     result = firebase.get('https://test-a1fc4-default-rtdb.firebaseio.com/', '')
    #
    #     # Debugging: Print the structure of the result
    #     print(result)
    #
    #     # Verify email and password
    #     if result:
    #         for i in result.keys():
    #             print(f"Checking record {i}: {result[i]}")
    #             if isinstance(result[i], dict) and 'Email' in result[i]:
    #                 if result[i]['Email'] == email:
    #                     if result[i]['Password'] == password:
    #                         print(email + " Logged in!")
    #                         return True
    #     print("Login failed")
    #     return False


if __name__ == '__main__':
    # LabelBase.register(name="MPoppins", fn_regular="E:\\Poppins\\Poppins-Medium.ttf")
    # LabelBase.register(name="BPoppins", fn_regular="E:\\Poppins\\Poppins-SemiBold.ttf")
    OptiCheck().run()