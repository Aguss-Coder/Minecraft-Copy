# ctrl + b to run in Sublime Text
from ursina import *

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

app.run()