# This is where Exercise 5.6 goes
# Name:Olha Vasylevska

from swampy.TurtleWorld import *		
world = TurtleWorld()			
bob = Turtle()	
print bob	

#-------- koch() function ------
# This function takes two parameters (turtle and curve length) and draws a Koch curve 

def koch(t, x):
	if x<3:
		fd(t, x)
		return
	length=x/3.0
	angle=60
	koch(t, length)
	lt(t, angle)
	koch(t, length)
	rt(t, 2*angle)
	koch(t, length)
	lt(t, angle)
	koch(t, length)

bob.delay=0.01
koch(bob, 100)

pu(bob)
fd(bob, 50)
pd(bob)


# ---------snowflake() function----------
# This function takes two parameters (turtle and curve length) and uses koch() function 
# to draw a snowflake

def snowflake(t, x):
	for i in range(3):
		koch(t, x)
		rt(t, 120)

snowflake(bob, 100)
wait_for_user()

