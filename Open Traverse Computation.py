#Barış Özçimenli - ID: 010210616 
#Geo108E Term Project - Open Traverse Computation


import math
print(">>>")
print("This program calculates the coordinates in open traverse serie")
print("−"*62)

#Lists
ID_list = []
T_List = []
Distance_list = []
Azimuth_list = []
d_x = [] #delta x list
d_y = [] #delta y list
x_list = []
y_list = []

#Input part

f_id = input("Enter the point ID of first known point: ")
f_id_y = float(input("Enter the Y coordinates of first known point (m): "))
f_id_x = float(input("Enter the X coordinates of first known point (m): "))
ID_list.append(f_id)
ID_list[0] = f_id

s_id = input("Enter the point ID of second known point: ")
s_id_y = float(input("Enter the Y coordinates of second known point (m): "))
s_id_x = float(input("Enter the X coordinates of second known point (m): "))
ID_list.append(s_id)
ID_list[1] = s_id

#Unknkown Points
unknown_points = int(input("Enter the number of unknown traverse points: "))

#Point ID
b = 1
for b in range(unknown_points):
    b += 1
    print(f"Enter the point ID of unknown point {b}: ")
    c = input()
    ID_list.append(c)

#Traverse Angle
d = 0
while d < (len(ID_list)-2):
    d += 1
    print(f"Enter the traverse angle of {ID_list[d]} (grad): ")
    traverse = float(input())
    T_List.append(traverse)

#Horizontal Distance
e = 1
while e < (len(ID_list)-1):
    print(f"Enter the horizontal distance between {ID_list[e]} and {ID_list[e+1]} (m): ")
    distance = float(input())
    Distance_list.append(distance)
    e += 1

#Azimuth Calculation Part-1
f_y = s_id_y - f_id_y
f_x = s_id_x - f_id_x

if f_y > 0 and f_x > 0:
    radian = math.atan(abs(f_y/f_x))
    azimuth = radian * 200 / math.pi
    table = azimuth

    Azimuth_list.append(table)
    Azimuth_list[0] = table

elif f_y < 0 and f_x < 0 :
    radian = math.atan(abs(f_y/f_x))
    azimuth = radian * 200 / math.pi
    table = 200 + azimuth

    Azimuth_list.append(table)
    Azimuth_list[0] = table

elif f_y > 0 and f_x < 0 :
    radian = math.atan(abs(f_y/f_x))
    azimuth = radian * 200 / math.pi
    table = 200 - azimuth

    Azimuth_list.append(table)
    Azimuth_list[0] = table

elif f_y == 0:
    if f_x > 0:
        Azimuth_list.append(300)
        Azimuth_list[0] = 300

    else:
        Azimuth_list.append(100)
        Azimuth_list[0] = 100

elif f_x == 0:
    if f_y > 0:
        Azimuth_list.append(300)
        Azimuth_list[0] = 300
    else:
        Azimuth_list.append(200)
        Azimuth_list[0] = 200

elif f_y == 0 and f_x == 0:
    print("Same point.")

else:
    radian = math.atan(abs(f_y/f_x))
    azimuth = radian * 200 / math.pi
    table = 400 - azimuth

    Azimuth_list.append(table)
    Azimuth_list[0] = table

#Azimuth Calculation Part-2
h = 0
while h < (len(T_List)):
    e = Azimuth_list[h] + T_List[h]
    if e < 200:
        e += 200
        Azimuth_list.append(e)

    elif e>200 and e<600:
        e = e - 200
        Azimuth_list.append(e)
    elif e > 600:
        e -= 600
        Azimuth_list.append(float(e))
    h += 1

#Delta X and Delta Y
k = 0
while k < (len(Azimuth_list)-1):
    delta_x = math.cos(Azimuth_list[k+1]*math.pi/200)*Distance_list[k]
    delta_y = math.sin(Azimuth_list[k+1]*math.pi/200)*Distance_list[k]

    if Azimuth_list[0] == 0:
        delta_x = 0
        delta_y = 0
    elif Azimuth_list[0] == 100:
        delta_y = 0
        delta_x = -delta_x
    elif Azimuth_list[0] == 200:
        delta_x = 0
        delta_y = -delta_y
    elif Azimuth_list[0] == 300:
        delta_y = 0
        delta_x = -delta_x
    else:
        delta_x = math.cos(Azimuth_list[k+1]*math.pi/200)*Distance_list[k]
        delta_y = math.sin(Azimuth_list[k+1]*math.pi/200)*Distance_list[k]

    d_x.append(delta_x)
    d_y.append(delta_y)
    k += 1

#Coordinates of X and Y
q = 0
while q < (len(Azimuth_list)-1):
    #X
    X = d_x[q] + s_id_x
    s_id_x = X
    x_list.append(s_id_x)

    #Y
    Y = d_y[q] + s_id_y
    s_id_y = Y
    y_list.append(s_id_y)

    q += 1

#Output adjustments

print (format ("Point ID","<10s") ,format ("Point ID","<10s"),format ("Azimuth","<10s"),format ("Delta Y","<10s"),format ("Delta X","<10s"))
print("-"*73)
print(format(ID_list[0],"<10s"),format(str(ID_list[1]),"<10s"),format(str(format(Azimuth_list[0],".4f")),"<10s"))

for p in range(len(d_x)):
    v1 = format(str(ID_list[p+1]), "<10s")
    v2 = format(str(ID_list[p+2]),"<10s")
    v3 = format(str(format(Azimuth_list[p+1], ".4f")),"<10s")
    v4 = format(str(format(d_y[p],".2f")),"<10s")
    v5 = format(str(format(d_x[p],".2f")),"<10s")
    print(v1,v2,v3,v4,v5)
print("-"*73)

print (format ("Point ID","<10s") ,format("Coordinate(Y)","<10s"),format("Coordinate(X)","<10s"))
print("-"*73)

for t in range(len(x_list)):
    v6 = format(str(ID_list[t+2]),"<10s")
    v7 = format(str(format(y_list[t],".2f")),"<10s")
    v8 = format(str(format(x_list[t],".2f")),"<10s")
    print(v6,v7,v8)
print("-"*73)
















































