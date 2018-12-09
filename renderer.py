import turtle
import numpy as np
import math

#########################################################################
#                                                                       #
# Utility class to render robot onscreen using Python turtle graphics.  #
#                                                                       #
#########################################################################

class Renderer:

    def __init__(self, n=1):
        turtle.radians()
        self.n = n
        self.count = -1

    def render_clear():
        turtle.clear()
        self.count = -1

    def render_reset(self, environment):
        self.count += 1
        self.render_backdrop(environment.bot)

    def render_backdrop(self, bot):
        if self.count % self.n == 0:
            turtle.hideturtle()
            turtle.colormode(255)
            turtle.pencolor((np.random.randint(255),np.random.randint(255),np.random.randint(255)))
            turtle.pensize(3+np.random.randint(5))
            for o in bot.obstacles:
                self.render_obstacle(o)
            turtle.penup()
            turtle.goto(bot.x, bot.y)
            turtle.setheading(bot.heading)
            turtle.turtlesize(3)
            turtle.showturtle()

    def render_obstacle(self, obstacle):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(obstacle.x+obstacle.radius,obstacle.y)
        turtle.setheading(math.pi/2)
        turtle.pendown()
        turtle.circle(obstacle.radius)

    def render_raytrace(self, env):
        turtle.hideturtle()
        turtle.goto(env.bot.x, env.bot.y)
        turtle.showturtle()
        for o in self.obstacles:
            a,b,m,n = env.bot.bearings_to_ob(o)
            d = env.bot.distance_to_ob(o)
            env.render_reset_turtle()
            turtle.pendown()
            turtle.goto(m[0], m[1])
            env.render_reset_turtle()
            turtle.pendown()
            turtle.goto(n[0], n[1])
        env.render_reset_turtle()

    def render_step(self, environment):
        if self.count % self.n == 0:
            turtle.setheading(environment.bot.heading)
            turtle.pendown()
            turtle.goto(environment.bot.x, environment.bot.y)
