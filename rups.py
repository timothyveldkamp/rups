import random
import turtle as t

t.bgcolor('yellow')

rups = t.Turtle()
rups.shape('square')
rups.color('red')
rups.speed(0)
rups.penup()
rups.hideturtle()

blad = t.Turtle()
blad_vorm = ((0, 0), (14, 2), (18, 6), (20, 20),
             (6, 18), (2, 14))
t.register_shape('blad', blad_vorm)
blad.color('green')
blad.penup()
blad.hideturtle()
blad.speed(0)

spel_gestart = False
tekst_turtle = t.Turtle()
tekst_turtle._write('Druk SPATIE om te beginnen', align='center',
                    font=('arial', blad_vorm))
tekst_turtle.hideturtle()

score_turtel = t.Turtle()
score_turtel.hideturtle()
score_turtel.speed(0)


def biuten_venster():
    pass


def game_over():
    pass


def toon_score(huidige_score):
    pass


def plaats_blad():


def
