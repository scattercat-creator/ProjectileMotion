from vpython import *
#Web VPython 3.2
theta = 0

def make_grid(xmax,dx):
    # xmax = extent of grid in each direction
    # dx = grid spacing
    for x in range(-xmax, xmax + dx, dx):
        curve(pos=[vector(x,xmax,0),vector(x,-xmax,0)])
    for y in range(-xmax,xmax+dx,dx):
        curve(pos=[vector(-xmax, y, 0),vector(xmax,y,0)])

make_grid(200,20)

timeVpos = gcurve(color=color.red)

ball = sphere(radius=1, pos=vec(0,0,0), color=color.green, velocity=vec(0,0,0), acceleration=vec(0,-10,0), make_trail=True)
cannon = cylinder(pos=vec(0,0,0), axis=vec(8,0,0), color=color.red, radius=4)
cube = box(pos=vec(0,0,0), length=10, height=10, width=10, color=color.purple)

def changeTheta(evt):
    theta = radians(evt.value)
    widgetThetaText.text = f'theta = {evt.value} degrees\n'
    cannon.axis = vec(8*cos(theta),8*sin(theta),0)

def shootBall():
    oldPos = ball.pos 
    ball.velocity = cannon.axis * shootVel
    dt = 0.01
    time = 0
    while(True):
        
        rate(20)
        time += dt
        
        timeVpos.plot(ball.pos.x, ball.pos.y)
        
        ball.pos = oldPos + ball.velocity * time + 1/2 * ball.acceleration * time * time
        ball.velocity = ball.velocity + ball.acceleration * time
        oldPos = ball.pos
        if ball.pos.y <= -1:
            ball.velocity = vec(0,0,0)
            ball.make_trail = False
            ball.pos = vec(0,0,0)
            
            ball.make_trail = True
            break

def setVel(evt):
    global shootVel
    shootVel = evt.value
    widgetVelText.text = f'velocity = {evt.value} m/s\n'
    
def noMoreTrail():
    ball.clear_trail()

velocitySlider = slider(bind=setVel, min=0, max=5, step=1, align='left')
widgetVelText = wtext(text="velocity:\n")
angleSlider = slider(bind=changeTheta, max=90, min=0, step=1, align='left', top=12)
widgetThetaText = wtext(text="theta:\n", margin=12)
shoot = button(bind=shootBall, text="Run")
clear = button(bind=noMoreTrail, text="reset")


