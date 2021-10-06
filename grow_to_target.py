from vpython import*
import numpy as np
import sys
sys.path.append(".")
import grow
from grow import *
import matplotlib.pyplot as plt
import time

scene2 = canvas(title='Simulation System', width=800, height=700, center=vector(0,0,0),
                background=color.white)



#target
ball_position = vector(3,3,1)#vector(-4,-2,0)
ball_radius = 1
ball = sphere(pos=ball_position, radius=ball_radius, color = color.white) #(vec(246/255, 177/255, 76/255))

rod = cylinder(pos=ball_position,  axis=vector(-3,-1,2), radius=ball_radius, color =color.white)

end_ball_position = rod.pos+rod.axis
end_ball = sphere(pos=end_ball_position, radius=ball_radius, color = color.white)# vec(246/255, 177/255, 76/255))
bottom_plane = box(pos=vec(0,0,-0.2),axis = vec(1,0,0), length=20, height=0.1, width=20,color = vec(180/255,180/255,180/255), up=vec(0,0,1))
#background1 = box(pos=vec(0,100,0),axis = vec(0,0,1), length=20, height=0.1, width=20,color = vec(180/255,180/255,180/255),texture = "sky.jpg")#'D:/Santanna/3D Grow/sky.jpg')

# plat initial
spr_dis = np.sqrt(3)/2*0.5
spr_len = 0.6
test = grow.Cell(Spr_distance = spr_dis, Spr_len = spr_len)

# light
lamp1 = local_light(pos=vec(100,100,-100), color=color.white*0.2)
lamp2 = local_light(pos=vec(100,-100,-100), color=color.white*0.2)
lamp3 = local_light(pos=vec(-100,-100,100), color=color.white*0.2)
lamp4 = local_light(pos=vec(100,-100,100), color=color.white*0.2)

#light2 = distant_light(direction=vector(100,100,100), color=color.white*0.2)


scene2.camera.up = vec(0,0,1)
scene2.camera.pos = vec(-6.60371, 1.34283, 2.26781) #(-4.21826, -6.77872, 2.1207)
scene2.camera.axis = vec(6.60371, -1.34283, -2.26781) #(4.21826, 6.77872, -2.1207)
time.sleep(5)
t=0
delt = 0.1
dt=spr_len*delt
dt_L = spr_len*delt
rate(200)





#######################   reaching part    ################################
#res = Grow_toward_one_target(test,steplenght = dt, ball_pos = ball_position, ball_rad = ball_radius)
#dis_list = test.Distance_from_top_to_target( ball_pos = ball_position, ball_rad = ball_radius)
res = Grow_toward_one_target(test, steplenght = dt,rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius)
dis_list = test.Distance_from_top_to_target(rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius)


min_dist = min(dis_list)
while (min_dist> spr_dis*2/np.sqrt(3) *1):

    #res = Grow_toward_one_target(test, steplenght = dt, ball_pos = ball_position, ball_rad = ball_radius)
    #dis_list = test.Distance_from_top_to_target(ball_pos = ball_position,ball_rad =  ball_radius)

    res = Grow_toward_one_target(test, steplenght = dt,rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius)
    dis_list = test.Distance_from_top_to_target(rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius)
    min_dist = min(dis_list)
    if res == 0:
        test.add_one_layer_on_top()
        res = 1

###########################################################################

#dis = test.Distance_from_top_to_rod_shape(test, steplenght = dt, rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius )

Prepare_for_grasping(test, steplenght = dt, rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius )
Grow_coiling(test, steplenght = dt, rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius )

#Grow_climbing(test, steplenght = dt, rod_pos = rod.pos, rod_axis = rod.axis, rod_rad = rod.radius )

print("end")




