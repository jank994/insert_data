from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.name_input = TextInput(hint_text='Name')
        self.surname_input = TextInput(hint_text='Surname')
        self.age_input = TextInput(hint_text='Age')

        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.submit_data)

        layout.add_widget(self.name_input)
        layout.add_widget(self.surname_input)
        layout.add_widget(self.age_input)
        layout.add_widget(submit_button)

        return layout

    def submit_data(self, instance):
        name = self.name_input.text
        surname = self.surname_input.text
        age = self.age_input.text
        data = {'name': name, 'surname': surname, 'age': age}

        response = requests.post('http://your_flask_api_url/insert', json=data)
        print(response.json())

if __name__ == '__main__':
    MyApp().run()