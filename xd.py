from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina
app = Ursina()

player = FirstPersonController(
    position=(0,4,0)
)


caja = Entity(
    model='cube',
    texture='white_cube',
    Collider='box'
)


for z in range(100):
    for x in range(10):

            caja = Entity(
                model='cube',
                texture='white_cube',
                collider='box',
                position=(x,0,z)
            )

app.run()
