from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        self.options = ['Scissor', 'Paper', 'Rock']
        main_layout = BoxLayout(orientation = "horizontal")

        main_layout.add_widget(TextInput(background_color="blue", size= (70, 100)))
        
        layout = FloatLayout()
        layout.add_widget(main_layout)
        button_size = (100, 60)  # Define the size of the buttons
        
        Scissor_but = Button(text="Scissor", font_size=20, size_hint=(None, None), size=button_size, pos_hint={'center_x': 0.3, 'center_y': 0.5})  # Centered horizontally, 60% from bottom
        Paper_but = Button(text="Paper", font_size=20, size_hint=(None, None), size=button_size, pos_hint={'center_x': 0.5, 'center_y': 0.5})  # Centered
        Rock_but = Button(text="Rock", font_size=20, size_hint=(None, None), size=button_size, pos_hint={'center_x': 0.7, 'center_y': 0.5})  # Centered horizontally, 40% from top

        layout.add_widget(Scissor_but)
        layout.add_widget(Paper_but)
        layout.add_widget(Rock_but)

        return layout

if __name__ == '__main__':
    MyApp().run()
