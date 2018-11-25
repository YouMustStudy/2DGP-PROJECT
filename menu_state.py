from pico2d import *

image = None

def enter():
    global image
    image = load_image('.\\popup\\menu.png')

def exit():
    global image
    del(image)

def update(): pass
def draw(): pass
def handle_events(): pass
def pause(): pass
def resume(): pass