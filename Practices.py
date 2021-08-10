# ctrl + b to run in Sublime Text
from ursina import *

class Test_cube(Entity):
	def __init__(self):
		super().__init__(
			model = 'cube',
			color = color.white,
			texture = 'white_cube',
			rotation = Vec3(45,45,45)
			)

class Test_button(Button):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'cube',
			texture = 'brick',
			color = color.blue,
			highlight_color = color.red,
			pressed_color = color.lime
			)

# in order for the button to work, we need this code
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				print('button pressed')

# here i control the X and Y axes with the WASD keys.
def update():
	if held_keys['a']:
		test.x  -= 4 * time.dt
	elif held_keys['d']:
		test.x += 4 * time.dt
	elif held_keys['s']:
		test.y -= 4 * time.dt
	elif held_keys['w']:
		test.y += 4 * time.dt

app = Ursina()

test = Entity(
	model = 'quad',
	color = color.red,
	scale = (1,4),
	position = (5,4))

test = Test_button()

app.run()