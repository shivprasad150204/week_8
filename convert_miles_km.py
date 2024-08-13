from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = "0.0"
        return self.root

    def handle_convert(self):
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, increment):
        miles = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

if __name__ == "__main__":
    ConvertMilesKmApp().run()

