from vpython import *

circle = ring(pos=vec(0,0,0), axis=vec(0,0,1), radius=5, thickness=0.1, color=color.red)
ball = sphere(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius=0.5, color=color.green, mass=1, acceleration=vec(0,0,0), velocity=vec(-5*sin(pi/4),-5*cos(pi/4),0))
velocityvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.velocity), color=color.orange)
accelerationvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.acceleration), color=color.cyan)
dt = 0.01


speed = 5
def newVariables():
    ball.acceleration = ((mag(ball.velocity) ** 2) / 5) * -norm(ball.pos)
    #print("acc: ", ball.acceleration)
    ball.velocity = ball.velocity + ball.acceleration * dt 
    print("vel: ", ball.velocity)
    print(degrees(diff_angle(ball.acceleration, ball.velocity)))
    ball.pos = ball.pos + ball.velocity * dt + .5 * ball.acceleration * dt ** 2
    #print("pos: ", ball.pos)
    newVectors()
    
def newVectors():
    velocityvec.pos = ball.pos
    velocityvec.axis = ball.velocity
    accelerationvec.pos = ball.pos
    accelerationvec.axis = ball.acceleration


while True:
    rate(100)
    newVariables()
    
    
    
    
    
    
    
    
    
    
    
    
    
    