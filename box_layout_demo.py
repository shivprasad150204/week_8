from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""

if __name__ == "__main__":
    BoxLayoutDemo().run()
