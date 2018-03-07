import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.lang import Builder

import cloudspeech_demo
import assistant_library_demo

kv = '''
<ColoredLabel>:
    size: (100,100)
    background_color:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
     '''

Builder.load_string(kv)


class MyLabel(Label): pass

class MyButton(Button):
    def callback(instance, value):
        print('My button <%s> state is <%s>' % (instance, value))
    btn1 = Button(text='Hello world 1')
    btn1.bind(state=callback)

class ColoredLabel(Label):
    background_color = ListProperty((0,0,0,1))



class MyApp(App):

    def build(self):

        def googleAssistant(instance):
            print("---------------\n----------------\n")
            assistant_library_demo.main()
            print("Google Assistant")

        def cloudSpeech(instance):
            print("---------------\n----------------\n")
            cloudspeech_demo.main()
        
        def on_touch_up(self, touch):
            print("Touch Up")
        def on_touch_down(self, touch):
            print("Touch Down")


        floatLayout = FloatLayout()
        layout = BoxLayout(height=50, spacing=10, padding=10)

        label1 = ColoredLabel(text="Google Assistant", background_color=(160,160,160,.5))
        #layout.add_widget(label1)

        label2 = ColoredLabel(text="Voice Commands", background_color=(160,160,160,.5))
        #layout.add_widget(label2)

        button = Button(text='Google Assistant', font_size=14)
        button.bind(on_press=googleAssistant)
        #button.bind(on_touch_up=googleAssistant)
        layout.add_widget(button)

        button2 = Button(text='Voice Commands', font_size=20)
        button2.bind(on_press=cloudSpeech)
        #button2.bind(on_touch_up=cloudSpeech)
        layout.add_widget(button2)

        

        floatLayout.add_widget(layout)

        return floatLayout


if __name__ == '__main__':
    MyApp().run()
