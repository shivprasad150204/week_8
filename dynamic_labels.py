from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        names = ["John", "Alice", "Bob", "Eve", "Mallory"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

if __name__ == "__main__":
    DynamicLabelsApp().run()
