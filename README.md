# Custum_Kivy_Elements
This repo contains the custum kivy elements. 

## 1. Rounded Button
  RoundedButton class implements a rounded corner button. I have added two properties:
    (1) bg_color: This let you give a color to the button
    (2) rad: This lets you adjust the border radius.


https://github.com/user-attachments/assets/362eae79-c4f3-4f99-b1c8-bcf10f9f60c6

  
## Code for above example:
```
from rounded_button import RoundedButton
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    canvas.before:
        Color:
            rgba: [247/255, 242/255, 250/255]

        Rectangle:
            size: self.size
            pos: self.pos    
    RoundedButton:
        rad: 50
        bg_color: [102/255, 79/255, 161/255, 1]
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: (0.8, 0.1)
        text: "Rounded Button"
        font_size: 25'''                   
)

class RootWidget(FloatLayout):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
```
