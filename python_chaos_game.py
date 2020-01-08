#.___________________________________________________________________________________.
#| 07/01/2020                                                                        |
#| Este código originalmente genera triángulos de Sierpiński a partir de puntos pse_ |
#| udoaleatorios, pero con más puntos, con otras restricciones y con proporciónes de |
#| división de distancia diferentes se pueden crear diferentes fractales.            |
#| https://en.wikipedia.org/wiki/Chaos_game#/media/File:V4_ban1.gif                  |
#.___________________________________________________________________________________.
#imports
import cv2;import numpy as np
from math import ceil , sqrt
import os ; import datetime
from random import sample
#Params
image_size = 800; #500x500
n_points = 300; #Número de puntos a dibujar
point_size = 1; #Tamaño de punto
prop = 1/2; #Proporción de división de distancia entre puntos
repetir_vertice = True; #Puede repetir el mismo vertice dos veces seguidas
save = False
save_path = "/res"
#vértices de la forma
shape_coords = [[0,image_size],[image_size,image_size],[image_size//2,0]]
"""shape_coords = [[0,0],[0,image_size],[image_size,0],[image_size,image_size]]"""
"""shape_coords = [[image_size//2,0],[0,image_size//2],[image_size//4,image_size],\
    [3*image_size//4,image_size],[image_size,image_size//2]]"""

current_path = os.getcwd().replace("\\",'/')
coord_act = shape_coords[0] #Punto actual
vertex = 0;
img = np.zeros((image_size,image_size,3), np.uint8)

def pp_average(p1,p2):
    """Redondea un punto medio"""
    return [ceil(p1[0]*prop + p2[0]*(1-prop)) , ceil(p1[1]*prop + p2[1]*(1-prop))]

def mark_vertex(_shape_coords,_img,_rad):
    for p in _shape_coords:
        cv2.circle(_img,(p[0],p[1]), _rad, (0,255,0), -1)
    return True

if (__name__ == '__main__'):
    res = mark_vertex(shape_coords,img,ceil(0.01*image_size))
    for _ in range(n_points):
        vertex_op = set(range(0,len(shape_coords)))
        if not(repetir_vertice) : vertex_op -= {vertex} #Saca de las opciones el punto anterior
        vertex = sample(vertex_op,1)[0]
        next_coord = shape_coords[vertex] #Siguente esquina
        next_coord = pp_average(next_coord,coord_act)
        coord_act = next_coord
        cv2.circle(img,(next_coord[0],next_coord[1]), point_size, (0,0,255), -1)
        if(_%100 == 0):
            print(_)
        cv2.imshow('w',img)
        k = cv2.waitKey(1)
        if(k == ord('q')):
            cv2.destroyAllWindows()
            break
    cv2.imshow('w',img)
    cv2.waitKey(0)
    if(save):
        print(str(current_path+save_path))
        os.chdir(current_path+save_path)
        filename = "points={};vertex={};fractions={};repeat_vertex={};size{}.jpg".format(n_points,
            len(shape_coords),prop,repetir_vertice,image_size)
        cv2.imwrite(filename, img)
        print('Successfully saved at ' + current_path+save_path)
    pass
