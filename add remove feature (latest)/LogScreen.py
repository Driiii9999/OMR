from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty

Window.size = (310, 580)

class ClassCard(MDCard):
    section_name = StringProperty("")

class StudentList(MDCard):
    student_name = StringProperty("")

class OptiCheck(MDApp):
    dialog = None
    add_class_dialog = None

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("testry.kv"))
        return screen_manager

    def on_start(self):
        self.class_data = {
            "BSIT 3-A": ["John Doe", "Jane Doe"],
            "BSIT 3-B": ["Alice", "Bob"],
            # Additional classes here...
        }

        self.current_class = None
        self.show_class_cards()

    def show_class_cards(self):
        grid = self.root.get_screen('testing').ids.class_section_grid
        grid.clear_widgets()

        top_bar = self.root.get_screen('testing').ids.top_bar
        top_bar.title = "Classes"
        top_bar.left_action_items = []  # No back button in the class list

        # Show the add class button
        add_class_button = self.root.get_screen('testing').ids.add_class_button
        add_class_button.opacity = 1
        add_class_button.disabled = False

        # Hide add student button
        add_student_button = self.root.get_screen('testing').ids.add_student_button
        add_student_button.opacity = 0
        add_student_button.disabled = True

        for class_name in self.class_data.keys():
            card = ClassCard(section_name=class_name)
            card.bind(on_release=self.on_card_click)
            grid.add_widget(card)

    def on_card_click(self, card):
        class_name = card.section_name
        self.current_class = class_name
        student_names = self.class_data.get(class_name, [])

        grid = self.root.get_screen('testing').ids.class_section_grid
        grid.clear_widgets()

        top_bar = self.root.get_screen('testing').ids.top_bar
        top_bar.title = class_name
        top_bar.left_action_items = [["arrow-left", lambda x: self.show_class_cards()]]

        # Show the add student button
        add_student_button = self.root.get_screen('testing').ids.add_student_button
        add_student_button.opacity = 1
        add_student_button.disabled = False

        # Hide add class button
        add_class_button = self.root.get_screen('testing').ids.add_class_button
        add_class_button.opacity = 0
        add_class_button.disabled = True

        for student in student_names:
            student_card = StudentList(student_name=student)
            grid.add_widget(student_card)

    def open_student_input_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add Student",
                type="custom",
                content_cls=MDTextField(hint_text="Enter Student Name"),
                buttons=[
                    MDRaisedButton(text="Cancel", on_release=self.close_dialog),
                    MDRaisedButton(text="Add", on_release=self.add_student)
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def add_student(self, *args):
        student_name = self.dialog.content_cls.text
        if student_name and self.current_class:
            self.class_data[self.current_class].append(student_name)
            self.on_card_click(ClassCard(section_name=self.current_class))  # Refresh UI
            self.close_dialog()

    def add_student(self, *args):
        student_name = self.dialog.content_cls.text  # Get the text entered in the dialog
        if student_name and self.current_class:  # Ensure a name is entered and a class is selected
            self.class_data[self.current_class].append(student_name)  # Add the student to the class list
            self.on_card_click(ClassCard(section_name=self.current_class))  # Refresh the student list UI

            # Clear the text box for future input (if the dialog opens again)
            self.dialog.content_cls.text = ""

            # Close the dialog after adding the student
            self.close_dialog()

    def remove_student(self, student_name):
        if self.current_class and student_name in self.class_data[self.current_class]:
            self.class_data[self.current_class].remove(student_name)
            self.on_card_click(ClassCard(section_name=self.current_class))  # Refresh UI

    def open_class_input_dialog(self):
        if not self.add_class_dialog:
            self.add_class_dialog = MDDialog(
                title="Add Class Section",
                type="custom",
                content_cls=MDTextField(hint_text="Enter Class Section Name"),
                buttons=[
                    MDRaisedButton(text="Cancel", on_release=self.close_add_class_dialog),
                    MDRaisedButton(text="Add", on_release=self.add_class_section)
                ],
            )
        self.add_class_dialog.open()

    def close_add_class_dialog(self, *args):
        self.add_class_dialog.dismiss()

    def add_class_section(self, *args):
        class_name = self.add_class_dialog.content_cls.text
        if class_name and class_name not in self.class_data:
            self.class_data[class_name] = []  # Initialize with an empty student list
            self.show_class_cards()  # Refresh class section view
            self.close_add_class_dialog()
    def add_class_section(self, *args):
        class_name = self.add_class_dialog.content_cls.text  # Get the text entered in the dialog
        if class_name and class_name not in self.class_data:  # Ensure a name is entered and it's not a duplicate
            self.class_data[class_name] = []  # Add the new class section with an empty student list
            self.show_class_cards()  # Refresh the class section list UI

            # Clear the text box for future input (if the dialog opens again)
            self.add_class_dialog.content_cls.text = ""

            # Close the dialog after adding the class section
            self.close_add_class_dialog()


if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="C:\\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Poppins-SemiBold.ttf")
    OptiCheck().run()
