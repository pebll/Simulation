import pyglet

window = pyglet.window.Window(fullscreen=False)

particule = pyglet.resource.image('particule.png')


@window.event
def on_draw():
    window.clear()
    particule.blit(0, 0)


pyglet.app.run()
