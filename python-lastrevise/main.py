from Graphics.circ import *
from Graphics.rect import *
from Graphics.threedgraphics.cuboid import *
from Graphics.threedgraphics.sphere import *
r=int(input("Enter radius of circle and sphere"))
print(f"circle area {cirArea(r):.2f}  and sphere area is {sphereArea(r):.2f}")
l,w,h=map(int,input("Enter the values l,b,h").split())
print(f"{cuboidArea(l,w,h)} and {cuboidVol(l,w,h)}")