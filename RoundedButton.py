from kivy.uix.button import Button
from kivy.graphics import RoundedRectangle, Color
from kivy.properties import ListProperty

class RoundedButton(Button):
    bg_color = ListProperty([1, 0, 0, 1])
    """Contains the color of the button
    """
    border_radius = ListProperty([50])
    """Contains the radius of each border
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.background_normal = ''
        self.background_down = ''  


        with self.canvas.before:
            self.bg_color_instruction = Color(*self.bg_color) 
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=self.border_radius)

        self.bind(size=self._update_rect, pos=self._update_rect)
        self.bind(bg_color=self._update_bg_color)
        self.bind(border_radius=self._update_border_radius)
        
    def on_press(self, *args):
        new_color = []
        for i, c in enumerate(self.bg_color):
            if i < 3:
                new_color.append(c)
        new_color.append(0.5)
        self.bg_color_instruction.rgba = new_color
    
    def on_release(self, *args):
        self.bg_color_instruction.rgba = self.bg_color

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
    def _update_bg_color(self, *args):
        self.bg_color_instruction.rgba = self.bg_color
        
    def _update_border_radius(self, *kwargs):
        self.rect.radius = self.border_radius
