import pygame
import sys

### Prelude on typing
# The main thing I want to teach in this file is types. Types might seem a bit
# unmotivated or cumbersome at first, you have to type more, but they offer so
# many advantages, both for math and programming.
import typing

# In math, types are helpful for understanding conceptually what is going on.
# In my opinion, in good mathematics, everything should be typed. To say that some thing x is of type T, we write x: T, or use a fancy e character instead of
# the colon that I can't write here. Types give us a conceptual framework for
# distinguishing things like:
# Expressions, 5*x + 1: R
# Functions, f: R -> R where f(x) := 5*x + 1
# Equations, y = 5*x + 1; This is itself a type of a special kind, a proposition
# Sets, The graph of the function f, or the solution set of the equation above,
# which we can denote in math {(x,y) | y = 5*x + 1} (you would read this as
# "the set of points x y such that y equals 5 x plus 1"). Sets are types, and
# they're typically the main things mathematicians use as types.

# In math and programming, types are helpful for understanding if what you are
# doing makes sense. It makes sense to solve an equation 5*x + 1 = 4*x + 3, but
# it does not make sense to solve 5*x + 1. What it means to graph the function
# f(x) = 5*x + 1 is very different from what it means to plot the solution set
# of the equation y = 5*x + 1, even if we end up with the same line.
# It is an abuse of notation to write y(x). We can guess at what that means
# for the equation y = 5*x + 1, but if we consider instead the equation
# x^2 + y^2 = 1, then y(x) is meaningless

# In programming, there are a lot of very nice things about types. One of the
# biggest reasons they are nice in programing is that if we can catch errors
# before we run our code, that is much better and easier to debug than if those
# errors show up at runtime. Without types, we can write things like this

def some_line(x):
    return 4*x + 3

#print("This makes sense:")
#print(some_line(4))

# This somewhat makes sense, but do you end up with a float or an int? This can
# propagate through your code in an unpredicatble way
#print("This somewhat makes sense:")
#print(some_line(4) + some_line(4.0))

# comment those print lines afterwards to clean up the interpreter window


# This doesn't make any sense
if False:
    some_line("banana")
    some_line(some_line)
    some_line(pygame)
    # this isn't an issue with typing, but a more general issue with python:
    some_line(i_havent_even_defined_this)

# Two things can happen if python tries to execute some of the code in that if
# block. What usually happens is once the code is run, python will realize that
# it makes no sense and throw a TypeError. Sometimes it will compute anyways,
# and do some unintended behaviour. That's what we call a logic error, and
# those are typically the hardest kind to debug.
    
# Now suppose that instead of "if False" it was some more complicated condition.
# Imagine you're writing some code for a menu option that people rarely use, and
# you accidentally write something like the two lines above. Then you can
# compile and run the game just fine, but whenever someone selects that menu
# option, your program will crash, or open an error prompt, or do something
# unpredictable.

# But with types, we can catch this kind of error before we even run our code.
# This is called static type checking, as opposed to dynamic type checking.

# This function takes in an integer and returns an integer
def another_line(x: int) -> int:
    return 4*x+3

# In math notation, we would write (Z stands for Zahlen which is the German
# word for numbers)
# another_line: Z -> Z

# Now unfortunately, python was not originally defined with types in mind. In
# most languages, you need to specify the types, and doing so is enough to get
# the compiler to type check. I think you need to use a third party extension
# like mypy in order to do static type checking, and your IDE might do something
# like that for you.

# In a regular python interpreter, the following code will run, though it should
# not, or it should at least give a warning.

if False:
    another_line(4.1)
    another_line("banana")
    another_line(another_line)

# So for the rest of the file, I will try to give types when possible, or give
# them in comments when it isn't (or when it would be difficult to do so). It
# would be good to figure out how to make python check types, but that's a
# project for later.


pygame.init
WIDTH: int = 800
HEIGHT: int = 600
# python notation for tuples is cumbersome
size: tuple[int,int] = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Linear Graphs")


# Not going to bother to do types for these since we're not doing much with them
# Should be something like "BLACK: colour = (0,0,0)" or "BLACK: [int,int,int]"
# or "BLACK: (int8, int8, int8)" (int8 means 8 bit integer, which are integers
# that can be written using 8 binary numbers, like 0b10011011 (0b indicates
# binary). 8 bit integers go from 0 to 255).
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (0,64,255)
RED = (255,0,0)
            
# I've taken the graphing code out of the game loop because I just want to
# render one frame. I added the game loop at the end as a hack because I didn't
# want to figure out a reasonable way to make the window stay open and quit
# when you press close

screen.fill(BLACK)


# we can change this later to change where we render the graph
# pixel coordinate of the origin
origin_x: int = int(WIDTH/2)
origin_y: int = int(HEIGHT/2)
# scale factors
scale_x: float = 1
scale_y: float = .07


# Math points and screen points are quite different. Math points are real
# numbers (though we are representing them with floats here), and screen points
# are pixels (represented by integers). We want the origin to be able to be
# anywhere on the screen (the middle by default). x-coordinates go left in both
# math and screen points, but y-coordinates go up in math points and down in
# screen points.

# Math points can be operated on by math functions, and screen points should
# for the most part just be rendered on the screen (although we will also use
# them to determine the domain of our functions).

# Because of this, I define two different classes (user defined types) and keep
# the appropriate methods for these types inside those class definitions.

# This also gives us a nicer syntax than what python gives us. Tuples in python
# are immutable lists. This means that to access the first coordinate of a
# tuple, or first element of a list, we write p[0]. This means that we can't
# tell what kind of thing p is, how long it is, whether it is mutable or not,
# or what kind of thing p[0] is, if we just see that notation. On the other hand
# in this class notation, we can write p.x and p.y for the coordinates and it is
# a lot less ambiguous.

# The math notation for this is R^2 or RxR. R stands for "real"
class MathPoint:
    # This is a special function that we use to define objects of this class
    # To define a point p with coordinates (4,7), write
    # p = MathPoint(4,7)
    # To get its coordinates, write p.x and p.y
    def __init__(self,x: float,y: float):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    # this transforms math points to screen points
    # To understand this, think of where (1,0) are in the math plane and where
    # we want it to go on the screen. That determines the value of x. Similarly
    # for (0,1) and y
    # to_screen: MathPoint^2 -> ScreenPoint^2
    def to_screen(self):
        x: int = int(self.x*scale_x + origin_x)
        y: int = int(-self.y*scale_y + origin_y)  
        return ScreenPoint(x,y)


# The math notation for this would be Z^2 or ZxZ 
class ScreenPoint:
    def __init__(self,x: int,y: int):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    # transform a screen point back into a math point. For defining ranges of
    # inputs for math functions
    def to_math(self):
        # Here there is an implicit conversion int -> float. We do the same
        # in math. The fact that every integer is a real number is actually an
        # implicit type coersion, which happens when we say "is".
        x: float = self.x/scale_x - origin_x
        y: float = -self.y/scale_y - origin_y
        return MathPoint(x,y)

# I'd like to do away with this fuunction but idk how to do it cleanly
def translate_inv_x(x):
    return (x - WIDTH//2)


# draw the axes
pygame.draw.aaline(screen,BLUE,(origin_x,0),(origin_x,HEIGHT),5)
pygame.draw.aaline(screen,BLUE,(0,origin_y),(WIDTH,origin_y),5)

print(MathPoint.x )

# I'd like to write both of these in terms of the to_math() function but I
# haven't figured out the right way to do it
# the domain of our function in math coordinates. Number of points and distance between them is defined in terms of number of pixels
domain = range(translate_inv_x(0),translate_inv_x(WIDTH))

# Every function has both a range (sometimes also called an "image") and a
# codomain. The codomain is the type of the output of a function. The range is
# the subset of the codomain that the function lands in
# the codomain of our function in math coordinates. Number of points and distance between them is defined in terms of number of pixels
codomain = range(0 - origin_y, HEIGHT - origin_y)


# Now for the meat of the code. We want to be able to define some function f in
# python, in terms of math coordinates, and then graph that function.

# Here is an example of a linear function we could graph:
def my_line(x: float) -> float:
    return 2*x+50

# we denote its type like this:
# my_line: R -> R

# In math, we want to be able to say "graph the function f(x)". This is itself a
# sort of function which takes in the function f(x) and gives you the graph of
# that function. We call functions which take in other functions "higher order"
# functions.
# This function takes in a function f:R -> R and gives us a graph, which is a
# subset of points of R^2, the plane. In math notation, we call the set of
# subsets of R^2 by P(R^2) (or for any set X, P(X), called the power set), but
# here we are storing that as a list of points, so the computer type is
# [MathPoint]
#
# Math type:
# graph_points : (R -> R) -> P(R^2)
# Which is represented as a computer type:
# graph_points : (R -> R) -> [MathPoint]
def graph_points(f) -> [MathPoint]:
    points: [MathPoint] = []
    for x in domain:
        points.append(MathPoint(x,f(x))) 
    return points
print(graph_points(my_line)[0].y)
# How many fence posts does it take to put up 7 fence segments in a single line?
# There are two hard problems in computer science. Cache invalidation, naming
# things, and off-by-one errors.
# The fence posts are the points, and the fences are the lines between them.
# This takes a list of fence posts and gives us a list of fences. This allows
# us to do a for loop which doesn't run outside of the bounds of that loop,
# which would otherwise happen when we try to plot the line from the last point
# to the non-existant point after
# fence_post_to_fences: [T] -> [T^2] (T is an arbitrary type)
def fence_post_to_fences(fence_posts):
    # using slice notation to skip the last element and then the first
    left_posts = fence_posts[:-1]
    right_posts = fence_posts[1:]
    return list(zip(left_posts,right_posts))           

# Things like drawing on the screen, getting key inputs, dealing with I/O in
# general, anything which is not taking in data and then outputing other data,
# are called side effects. This function doesn't return any data, all it does
# is a side effect. Functions like this have None as the return type.
def draw_line(start: ScreenPoint, end: ScreenPoint) -> None:
    pygame.draw.aaline(screen,GREEN,(start.x,start.y),(end.x,end.y),5)

# given a graph (as a list of (x,f(x)) MathPoints), draw them on the screen
def draw_graph(points: [ScreenPoint]) -> None:
    for fence in fence_post_to_fences(points):
        left = fence[0]
        right = fence[1]
        draw_line(left,right)

        
# I need this for the next part. There is almost certainly a better way
def to_screen(p: MathPoint) -> ScreenPoint:
    return p.to_screen()


# draw the graph of the function f
# draw_graph_of_function: (R->R) -> None
def draw_graph_of_function(f) -> None:
    screen_points: [ScreenPoint] = list(map(to_screen, graph_points(f)))
    draw_graph(screen_points)


# and now we can draw the graph of a function. Uncomment this:
#draw_graph_of_function(my_line)

# and then comment it again after

# We want to be able to talk about general linear equations, but the "obvious"
# way has us defining the function with m, b, and x as variables at the same
# level. 
# Here is the type of the function in math notation
# slope_interceptp: R^3 -> R
def slope_interceptp(m: float,b: float,x: float) -> float:
    return m*x+b





# In mathematical practice, we give the m and b first, and keep x as a variable.
# Here is a way to do this in python. We define a function which takes in our
# parameters, and output a function defined in terms of those parameters, which
# takes in our variable x. This is called Currying after the computer scientist
# Haskell Curry.
# slope_intercept: R^2 -> (R -> R)
def slope_intercept(m,b):
    def f(x):
        return m*x+b
    return f

def factored_quadratic(p: float,q: float) -> float:
    def f(x: float) -> float:
        return (x-p)*(x-q)
    return f




# a parabola, for fun
def parabola(a,b,c):
    def f(x):
        return a*x*x + b*x + c
    return f

# Now we can draw a bunch of graphs of functions

draw_graph_of_function(factored_quadratic(0,100))


# What if we want to draw the set of points which are the solution to any
# equation?

# This immediately gets into very difficult problems. With a function, we can
# take an x value, plug it into f, and get a y value, which gives us a point
# (x,y) we can plot. If instead we have an arbitrary equation like x^2+y^2=1,
# then we need to check all the points to see if they satisfy the equation.

# But which points do we check? There are an infinite number of points in the
# plane, and the points which satisfy the equation could be irrational. The
# natural thing to do would be to check the math points that correspond to the
# screen points, like we did with the domain in the function grapher, but
# those are really just a grid of points in the infinite continuous plane. The
# cureve defined by an equation could dodge all of those points.

# And to make things worse, math equations are exact, but floats on computers
# are not. All math operations on floats introduce a bit of error and that
# error could explode. Managing that error is pretty complex and tbh I don't
# exactly know how to do it. If you want me to show you what happens, I can
# do that, but it's a bit beyond the scope of this file.

print("this should be true but it's not, because floats are spooky:")
print(0.1+0.1+0.1 == 0.3)


draw_graph_of_function(parabola(1/200,-2,-200))

pygame.display.flip()

done: bool = False
clock = pygame.time.Clock()

while not done:
    
    #screen.fill(BLACK)
    
    pygame.draw.aaline(screen,BLUE,(origin_x,0),(origin_x,HEIGHT),5)
    pygame.draw.aaline(screen,BLUE,(0,origin_y),(WIDTH,origin_y),5)


    draw_graph_of_function(parabola(1/200,-2,-200))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    



pygame.quit()
sys.exit()
