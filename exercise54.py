# This is where Exercise 5.4 goes
# Name:Olha Vasylevska

def is_triangle(a, b, c):
	if a > b+c or b > a+c or c > a+b:
		print "No"
	else:
		print "Yes"

is_triangle(5, 7, 9)
is_triangle(12, 1, 1)
is_triangle(10, 5, 5)


def triangle():
	a,b,c=input('Please enter length of the three sides separated with commas:'+'\n')
	is_triangle(a,b,c)

triangle()