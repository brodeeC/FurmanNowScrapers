# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:30:05 2024

@author: mdavi
"""

from math import cos, sin, radians, sqrt
from numpy import arctan2, degrees
from dataclasses import dataclass

@dataclass
class Positioned():
    lat: float
    lon: float
    
    def distBetween(first : "Positioned", second : "Positioned"):
        # Approximate radius of earth in miles
        R = 3958.8 
        
        lat1 = radians(first.lat)
        lon1 = radians(first.lon)
        lat2 = radians(second.lat)
        lon2 = radians(second.lon)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * arctan2(sqrt(a), sqrt(1 - a))
        
        return R * c
    
    def headingBetween(first : "Positioned", second : "Positioned"):
        dltLonRad = radians(second.lon - first.lon)
        lat1rad = radians(first.lat)
        lat2rad = radians(second.lat)
        
        x = cos(lat2rad) * sin(dltLonRad)
        y = cos(lat1rad) * sin(lat2rad) - sin(lat2rad) * cos(lat2rad) * cos(dltLonRad)
        hdRad = arctan2(x,y)
        heading = degrees(hdRad)
        return int(heading)
    
    
@dataclass
class Directioned(Positioned):
    heading: int

    