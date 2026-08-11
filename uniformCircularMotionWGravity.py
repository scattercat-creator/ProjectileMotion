from vpython import *


circle = ring(pos=vec(0,0,0), axis=vec(0,0,1), radius=5, thickness=0.1, color=color.red)
ball = sphere(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius=0.5, color=color.green, mass=1, acceleration=vec(0,0,0), velocity=vec(-5*sin(pi/4),-5*cos(pi/4),0))
velocityvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.velocity), color=color.purple)
accelerationvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.acceleration), color=color.orange)
acvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.acceleration), color=color.red)
atvec = cylinder(pos=vec(5*cos(pi/4),-5*sin(pi/4),0), radius = 0.1, axis=(2 * ball.acceleration), color=color.blue)

dt = 0.01



def newVariables():
    global ac, at
    
    at = proj(vec(0,-2,0),ball.velocity)
    
    ac = ((mag(ball.velocity) ** 2) / 5) * -norm(ball.pos)
    ball.acceleration = ac + at
    ball.pos = ball.pos + ball.velocity * dt + .5 * ball.acceleration * dt ** 2
    ball.velocity = ball.velocity + ball.acceleration * dt 
    
    print(degrees(diff_angle(ac, ball.velocity)))
    # update vectors
    newVectors()
    
def newVectors():
    velocityvec.pos = ball.pos
    velocityvec.axis = ball.velocity
    accelerationvec.pos = ball.pos
    accelerationvec.axis = ball.acceleration
    acvec.pos = ball.pos
    atvec.pos = ball.pos
    acvec.axis = 2 * ac 
    atvec.axis = 2 * at
    

    


for i in range(0,40, 0.01):
    rate(100)
    print(ball.velocity)
    newVariables()

















