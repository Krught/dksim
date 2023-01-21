#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:50:08 2022

@author: Andrew
"""
import pandas as pd
from datetime import datetime, timedelta
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'
import dash
from dash import dcc, html, dash_table
import numpy as np
import plotly.graph_objects as go
import ast

#Paste Raw Data From local_testing below##
#r_results = """3689.118*&*438182.01804400753*&*125.0*&*['Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Icy Touch', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Claw', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Meteorite Whetstone', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Death Chill', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Blood Tap', 'Unbreakable Armor', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Mirror of Truth', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Wandering Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Meteorite Whetstone', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Desolation', 'Sudden Doom', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Unholy Blight', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'Desolation', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Unholy Blight', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Unholy Blight', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Blood Plague', 'Crypt Fever', 'Desolation', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Crypt Fever', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Crypt Fever', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Crypt Fever', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Crypt Fever', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Crypt Fever', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Crypt Fever', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'Unbreakable Armor', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'Desolation', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Mirror of Truth', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Meteorite Whetstone', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Crypt Fever', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Crypt Fever', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Crypt Fever', 'Crypt Fever', 'Main hand', 'Necrosis', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Ghoul - Main hand', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Blood Plague', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Crypt Fever', 'Ghoul - Main hand', 'Crypt Fever', 'Frost Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Ghoul - Claw', 'Ghoul - Main hand', 'Crypt Fever', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Bloody Vengeance', 'Main hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Desolation', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Desolation', 'OH - Blood Strike', 'Desolation', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Frost Fever', 'Wandering Plague', 'Blood Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Main hand', 'Necrosis', 'Blood Plague', 'Wandering Plague', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Frost Fever', 'Crypt Fever', 'Crypt Fever', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Ghoul - Main hand', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Crypt Fever', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Necrosis', 'Off hand', 'Necrosis', 'Blood-Caked Blades', 'Bloody Vengeance', 'Frost Fever', 'Blood Plague', 'Crypt Fever', 'OH - Frost Strike', 'Frost Strike']*&*[0, 0.0, 0, 0.0, 0.0, 0, 0, 0, 0, 0.8, 0.8, 2.0, 2.0, 2.08, 2.08, 2.08, 0, 2.4, 2.4, 1.6, 1.6, 2.4000000000000004, 3.2, 3.666666666666667, 3.666666666666667, 4.8, 4.8, 4.16, 4.16, 4.16, 3, 3, 2.4, 0, 4.8, 4.8, 4.0, 4.8, 5.6, 5.333333333333334, 5.333333333333334, 6.24, 6.24, 6.24, 7.199999999999999, 6, 5.4, 5.4, 0, 7.199999999999999, 7.199999999999999, 6.3999999999999995, 6.3999999999999995, 7.199999999999999, 7.999999999999999, 8.799999999999999, 7.000000000000001, 7.000000000000001, 7.000000000000001, 8.32, 8.32, 9, 9, 8.4, 8.4, 0, 9.6, 9.6, 9.6, 9.6, 10.4, 11.200000000000001, 12.0, 8.666666666666668, 8.666666666666668, 8.666666666666668, 10.4, 10.4, 12.0, 12, 11.4, 0, 12.0, 12.0, 12.000000000000002, 12.800000000000002, 14.4, 14.4, 10.333333333333334, 10.333333333333334, 12.48, 12.48, 14.4, 14.4, 0, 14.4, 14.4, 13.600000000000003, 13.600000000000003, 14.400000000000004, 15.200000000000005, 16.8, 12.0, 12.0, 12.0, 16.8, 14.56, 14.56, 14.56, 16.8, 15, 15, 0, 16.8, 16.8, 16.000000000000004, 16.940896469654902, 17.8817929393098, 19.2, 13.666666666666666, 13.666666666666666, 16.64, 16.64, 18, 17.4, 0, 19.2, 19.2, 18.8226894089647, 18.8226894089647, 19.763585878619597, 20.704482348274496, 15.689616433959236, 15.689616433959234, 19.16464130958113, 19.16464130958113, 19.16464130958113, 21, 20.4, 20.4, 0, 22.1130476649013, 22.1130476649013, 21.645378817929394, 21.645378817929394, 22.586275287584293, 23.52717175723919, 25.026095329802597, 17.712566201251803, 17.712566201251803, 17.712566201251803, 21.689282619162256, 21.689282619162256, 24, 24, 23.4, 0, 25.026095329802597, 24.46806822689409, 25.40896469654899, 26.349861166203887, 19.735515968544373, 19.735515968544373, 27.939142994703897, 24.213923928743384, 24.213923928743384, 24.213923928743384, 27.939142994703897, 27, 27, 26.4, 0, 27.939142994703897, 27.939142994703897, 27.290757635858785, 27.290757635858785, 28.231654105513684, 29.172550575168582, 30.852190659605196, 21.758465735836943, 21.758465735836943, 26.73856523832451, 26.73856523832451, 26.73856523832451, 30.852190659605196, 30, 29.4, 0, 30.852190659605196, 30.852190659605196, 30.11344704482348, 30.11344704482348, 31.05434351447838, 31.995239984133278, 23.781415503129512, 23.781415503129512, 23.781415503129512, 33.7652383245065, 29.26320654790564, 29.26320654790564, 33.7652383245065, 33, 32.4, 0, 33.7652383245065, 33.7652383245065, 32.93613645378818, 32.93613645378818, 33.87703292344308, 34.817929393097984, 36.6782859894078, 25.804365270422082, 25.804365270422082, 25.804365270422082, 31.787847857486767, 36, 36, 35.4, 35.4, 0, 36.6782859894078, 36.6782859894078, 35.758825862752886, 36.69972233240779, 37.64061880206269, 38.58151527171759, 39.591333654309096, 27.82731503771465, 27.82731503771465, 34.312489167067895, 34.312489167067895, 34.312489167067895, 39, 38.4, 38.4, 0, 39.591333654309096, 39.591333654309096, 39.522411741372494, 39.522411741372494, 40.463308211027396, 41.4042046806823, 42.504381319210395, 29.85026480500722, 29.85026480500722, 42.504381319210395, 36.83713047664902, 36.83713047664902, 36.83713047664902, 42.504381319210395, 42, 41.4, 0, 42.504381319210395, 42.504381319210395, 42.3451011503372, 42.3451011503372, 43.2859976199921, 44.226894089647004, 31.87321457229979, 31.87321457229979, 31.87321457229979, 39.36177178623015, 39.36177178623015, 45.417428984111694, 45, 44.4, 44.4, 0, 45.417428984111694, 45.167790559301906, 45.167790559301906, 46.10868702895681, 47.04958349861171, 33.89616433959236, 33.89616433959236, 41.88641309581128, 41.88641309581128, 48, 48, 47.4, 0, 48.330476649012994, 48.330476649012994, 47.99047996826661, 48.931376437921514, 49.872272907576416, 51.24352431391429, 35.91911410688493, 35.91911410688493, 51.24352431391429, 44.411054405392406, 44.411054405392406, 51, 50.4, 50.4, 0, 51.24352431391429, 51.24352431391429, 51.24352431391429, 51.24352431391429, 51.24352431391429, 50.81316937723132, 50.81316937723132, 51.75406584688622, 52.69496231654112, 54.15657197881559, 37.94206387417751, 37.94206387417751, 37.94206387417751, 54.15657197881559, 46.935695714973534, 46.935695714973534, 54.15657197881559, 54, 53.4, 0, 54.15657197881559, 54.15657197881559, 54.15657197881559, 54.15657197881559, 53.635858786196025, 53.635858786196025, 54.57675525585093, 55.51765172550583, 57.06961964371689, 57.06961964371689, 39.96501364147008, 39.96501364147008, 49.46033702455466, 49.46033702455466, 49.46033702455466, 57.06961964371689, 57, 56.4, 56.4, 0, 57.06961964371689, 57.06961964371689, 56.45854819516073, 57.39944466481563, 58.340341134470535, 59.98266730861819, 41.98796340876265, 41.98796340876265, 41.98796340876265, 51.98497833413579, 51.98497833413579, 59.4, 0, 59.98266730861819, 59.98266730861819, 59.98266730861819, 59.98266730861819, 59.28123760412544, 59.28123760412544, 60.22213407378034, 61.16303054343524, 62.89571497351949, 44.010913176055226, 44.010913176055226, 44.010913176055226, 54.50961964371692, 54.50961964371692, 62.89571497351949, 60, 60, 62.4, 0, 46.0338629433478, 46.0338629433478, 57.034260953298045, 57.034260953298045, 57.034260953298045, 0, 48.60683701968991, 48.60683701968991, 60.245332600573, 60.245332600573, 60.245332600573, 63, 0, 62.10392701309014, 51.179811096032026, 51.179811096032026, 51.179811096032026, 0, 53.75278517237414, 53.75278517237414, 53.75278517237414, 0, 56.32575924871625, 56.32575924871625, 56.32575924871625, 0, 58.898733325058366, 58.898733325058366, 63.4957149735195, 63.456404247847956, 63.45640424784795, 0, 63.4957149735195, 63.18571995239994, 63.18571995239994, 64.26751289170974, 65.34930583101954, 61.47170740140048, 61.47170740140047, 66.6674758951229, 66.6674758951229, 67.20079764345213, 66, 65.4, 0, 67.20079764345213, 66.43109877032933, 66.43109877032933, 67.51289170963912, 68.59468464894891, 69.6764775882587, 64.04468147774259, 64.04468147774259, 69.87854754239785, 69.87854754239785, 69, 68.4, 0, 70.90588031338477, 70.90588031338477, 70.90588031338477, 70.90588031338477, 70.7582705275685, 70.7582705275685, 71.84006346687829, 72.92185640618808, 66.61765555408469, 66.61765555408469, 66.61765555408469, 74.6109629833174, 73.0896191896728, 73.0896191896728, 72, 72, 71.4, 0, 74.6109629833174, 74.6109629833174, 74.00364934549788, 74.00364934549788, 75.08544228480767, 76.16723522411746, 69.1906296304268, 69.1906296304268, 69.1906296304268, 76.30069083694775, 76.30069083694775, 76.30069083694775, 75, 74.4, 0, 78.31604565325004, 78.31604565325004, 77.24902816342725, 77.24902816342725, 78.33082110273705, 79.41261404204684, 80.49440698135663, 71.7636037067689, 71.7636037067689, 71.7636037067689, 79.5117624842227, 79.5117624842227, 79.5117624842227, 82.02112832318268, 78, 77.4, 0, 82.02112832318268, 81.57619992066643, 81.57619992066643, 82.65799285997622, 83.73978579928601, 74.33657778311101, 74.33657778311101, 82.72283413149765, 82.72283413149765, 82.72283413149765, 85.72621099311532, 81, 80.4, 80.4, 0, 85.72621099311532, 85.72621099311532, 84.8215787385958, 84.8215787385958, 85.9033716779056, 86.98516461721539, 88.06695755652518, 89.43129366304795, 76.90955185945312, 76.90955185945312, 85.9339057787726, 85.9339057787726, 85.9339057787726, 84, 83.4, 0, 89.43129366304795, 89.43129366304795, 89.14875049583497, 89.14875049583497, 90.23054343514477, 91.31233637445456, 93.13637633298059, 79.48252593579522, 79.48252593579522, 93.13637633298059, 93.13637633298059, 89.14497742604755, 89.14497742604755, 87, 86.4, 0, 93.13637633298059, 93.13637633298059, 92.39412931376435, 92.39412931376435, 93.47592225307415, 94.55771519238394, 95.63950813169373, 82.05550001213733, 82.05550001213733, 96.84145900291323, 92.3560490733225, 92.3560490733225, 90, 90, 89.4, 0, 84.62847408847944, 84.62847408847944, 84.62847408847944, 95.56712072059744, 95.56712072059744, 93, 92.4, 0, 87.20144816482154, 87.20144816482154, 96, 96, 95.4, 0, 89.77442224116365, 89.77442224116365, 97.14145900291321, 0, 92.34739631750575, 92.34739631750575, 92.34739631750575, 0, 94.92037039384786, 94.92037039384786, 97.3414590029132, 0, 0, 97.49334447018997, 97.49334447018997, 0, 0, 0, 96.72130107100352, 0, 0, 0, 0, 0, 0, 98.4, 0, 0, 0, 0, 98.77819236787239, 98.77819236787239, 98.77819236787239, 98.84145900291311, 0, 97.80309401031332, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98.88488694962311, 98.88488694962311, 0, 100.04145900291304, 99.9666798889329, 101.0484728282427, 102.13026576755249, 100.06631854653207, 100.06631854653207, 100.06631854653207, 101.98926401514734, 101.98926401514734, 101.98926401514734, 102, 101.4, 0, 103.74654167284568, 103.74654167284568, 103.21205870686228, 103.21205870686228, 104.29385164617207, 105.37564458548187, 107.45162434277832, 102.63929262287418, 102.63929262287418, 102.63929262287418, 107.45162434277832, 105.20033566242229, 105.20033566242229, 105.20033566242229, 105, 104.4, 104.4, 0, 107.45162434277832, 107.45162434277832, 107.45162434277832, 107.45162434277832, 106.45743752479166, 106.45743752479166, 107.68012693375636, 108.90281634272105, 105.21226669921629, 105.21226669921629, 108.41140730969724, 108.41140730969724, 108, 107.4, 107.4, 0, 111.15670701271095, 111.15670701271095, 111.15670701271095, 111.15670701271095, 110.12550575168575, 110.12550575168575, 111.34819516065045, 111.34819516065045, 112.57088456961515, 113.79357397857984, 115.01626338754454, 108.74604858875932, 108.74604858875932, 112.82156710784695, 112.82156710784695, 111, 111, 110.4, 0, 112.27983047830236, 112.27983047830236, 116.34535293365292, 114, 113.4, 113.4, 0, 115.8136123678454, 115.8136123678454, 116.4, 116.4, 0, 0, 0, 0, 0, 0, 117, 0, 0, 117.23172690599665, 117.23172690599665, 117.23172690599665, 117.24535293365287, 0, 0, 0, 116.23895279650924, 0, 0, 0, 0, 0, 0, 118.04535293365282, 117.46164220547394, 117.46164220547394, 118.68433161443863, 119.90702102340333, 121.12971043236803, 119.34739425738843, 119.34739425738843, 121.64188670414636, 121.64188670414636, 121.64188670414636, 123.1339988545948, 120, 119.4, 0, 123.1339988545948, 123.1339988545948]*&*[818.3175687865012, 163.66351375730025, 1244.84626878034, 163.66351375730025, 64.18938324885181, 0, 1418.2995628896306, 430.5264968996448, 567.7499806528385, 1123.0669059369263, 481.3336602520486, 869.7681354553474, 173.9536270910695, 679.241719249322, 173.9536270910695, 75.43983370271452, 418.7069897308591, 1622.6469945531403, 929.4301872980525, 455.252761633409, 300.1786747979977, 197.92793014628796, 130.50715730674935, 1631.5734866783655, 326.31469733567315, 0, 0, 437.79164162214386, 326.31469733567315, 111.74211137600264, 418.7069897308591, 418.7069897308591, 697.9007193877694, 0, 0, 129.90626550000002, 296.2488034337018, 195.33670242033543, 128.7985871004194, 859.4346899086424, 171.8869379817285, 1457.880257831479, 171.8869379817285, 73.09248697065584, 0, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 0, 0, 890.7245114798068, 587.3144020187327, 0, 0.0, 0.0, 662.2315114513007, 132.44630229026015, 91.97531719121321, 662.5205377153375, 132.44630229026015, 418.7069897308591, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 1961.9260346778399, 6351.14870391389, 492.23523359485813, 324.5636985907391, 214.00661158198025, 91.72079163436607, 0, 1094.8031452551163, 218.96062905102326, 89.00837147536764, 1677.1410291777056, 218.96062905102326, 0, 495.4664654622527, 774.7285573304126, 0, 5099.468725154787, 6602.738735025068, 320.90378474133456, 211.59338494882968, 0, 0, 1119.1664284225888, 223.83328568451776, 752.6222656369357, 223.83328568451776, 774.7285573304126, 774.7285573304126, 0, 4978.068405483975, 6783.875719930721, 510.0381442031684, 336.30235141027555, 0, 0.0, 0, 2287.832860740995, 457.566572148199, 74.44336523394382, 0, 1959.0590201156015, 457.566572148199, 122.45394136308153, 0, 617.8419329622527, 617.8419329622527, 0, 5332.359134319196, 6917.113258979867, 344.6409988857482, 147.70919932700428, 97.39458043124934, 0, 772.8718539238922, 154.57437078477847, 646.3718190179832, 154.57437078477847, 617.8419329622527, 897.2130127759574, 0, 5589.612192669248, 3141.0681209118156, 498.16953713096154, 656.9531657278358, 281.562630153496, 185.65312352827402, 1243.1742506824228, 248.63485013648457, 907.1164184211461, 248.63485013648457, 99.7972649875334, 617.8419329622527, 897.2130127759574, 897.2130127759574, 0, 5416.183164568091, 7414.276472869852, 498.16953713096154, 328.4765828639179, 216.5866385796123, 92.82656176413701, 0, 1227.8344057251252, 245.56688114502504, 119.21727330943177, 644.6122485669989, 245.56688114502504, 617.8419329622527, 617.8419329622527, 897.2130127759574, 0, 275.558745, 336.72859417094367, 144.31803295691594, 95.15855703330155, 1890.0281419324222, 378.00562838648443, 0, 1736.69572136486, 378.00562838648443, 101.95504368996654, 0, 495.4664654622527, 495.4664654622527, 774.7285573304126, 0, 1944.5602465955976, 6857.101309573435, 0, 0, 0.0, 0.0, 0, 970.9934874111505, 194.1986974822301, 1331.8086540883062, 194.1986974822301, 103.03393304118312, 0, 418.7069897308591, 697.9007193877694, 0, 1944.2291950756805, 2335.898050754072, 453.27466045470794, 298.8743800402715, 128.09414874560025, 84.46106220613011, 1927.549473686021, 385.5098947372042, 69.85808549127337, 0, 1311.5059181154127, 385.5098947372042, 0, 418.7069897308591, 697.9007193877694, 0, 1779.0586921221977, 6027.414518125061, 465.1432675269147, 306.7001485866291, 131.4481838425219, 86.67260246567201, 0, 627.6266259152794, 125.52532518305588, 93.86337355584222, 0.0, 418.7069897308591, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 820.4884280228015, 2698.129046568686, 294.27070225500074, 194.03240766260922, 127.93857810120879, 84.35848404778275, 0, 995.356770578623, 199.0713541157246, 724.7822613655451, 199.0713541157246, 100.33670966314166, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 815.0189846470253, 2930.3980752599796, 462.17611575886303, 304.74370645003967, 200.93796164352534, 132.49187292428695, 0, 1893.2604084873556, 378.65208169747115, 0, 1559.1992969847165, 378.65208169747115, 80.9167013412433, 0, 418.7069897308591, 697.9007193877694, 0, 827.3252322425213, 1161.4410389983072, 440.4170027931506, 188.75770167478294, 124.46061072393509, 53.3423975012238, 887.0755120565225, 177.4151024113045, 117.05949460699864, 1542.9571082064012, 177.4151024113045, 0, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 149.589033, 461.18706516951244, 608.1831181423531, 401.01591428784, 171.87084475831605, 587.1565055426445, 117.4313011085289, 452.19308753952487, 117.4313011085289, 418.7069897308591, 418.7069897308591, 697.9007193877694, 0, 2100.6475684827615, 1186.9651080852627, 287.0176645997632, 189.24999355094616, 81.11038765100022, 0, 1803.0260263856053, 360.60520527712106, 0, 709.8935883187562, 360.60520527712106, 418.7069897308591, 697.9007193877694, 697.9007193877694, 0, 0, 1249.6476799999998, 1249.6476799999998, 0, 2104.444873654663, 449.31845809730567, 296.2657905248189, 126.97613704662633, 54.42052337775047, 12.496476799999998, 1984.0922542697997, 396.81845085396, 115.79474616586658, 0, 1659.971525998624, 396.81845085396, 0, 435.72759906951194, 726.2706673303617, 0, 0, 1500.076881704857, 0, 7779.74629048861, 470.0885204736676, 309.96088548094474, 132.84569846623924, 87.59407757381445, 0, 12.496476799999998, 1056.5022629217096, 211.30045258434194, 1716.635065879264, 211.30045258434194, 83.03821485540026, 0, 452.7482084081647, 754.6406152729539, 754.6406152729539, 0, 2237.225529346744, 1287.6982518956142, 300.2050057911041, 128.6644397582622, 169.67418662849306, 12.496476799999998, 1038.8951843300906, 207.77903686601815, 84.79254333826084, 496.86852395981543, 207.77903686601815, 754.6406152729539, 0, 0, 5764.9986803936035, 0, 8050.898813601684, 439.4279522038, 289.74431673618756, 382.095716305205, 251.9413289333268, 0, 669.093289953293, 133.8186579906586, 98.10186743562163, 1770.9782930772872, 133.8186579906586, 0, 469.76881774681755, 469.76881774681755, 783.0105632155462, 0, 1152.3205335297662, 230.46410670595324, 771.179624674452, 230.46410670595324, 82.00465698952891, 0, 693.5301255162601, 138.70602510325202, 771.9416881535464, 138.70602510325202, 127.25907880967637, 469.76881774681755, 0, 285.6989304806291, 1040.5512232625563, 208.11024465251126, 138.19303307494687, 0, 661.8282847859241, 132.36565695718483, 95.368378869304, 0, 618.2382537817124, 123.64765075634249, 102.3539607610046, 0, 2166.453556183709, 433.29071123674186, 0, 839.0032743138722, 433.29071123674186, 0, 317.99671199999995, 468.1104192949664, 308.65659072321847, 203.5179886411574, 87.22548753055747, 973.4896371022303, 194.69792742044606, 1496.6354406032267, 194.69792742044606, 0, 469.76881774681755, 783.0105632155462, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 657.2050996794169, 131.4410199358834, 582.0073816484678, 131.4410199358834, 469.76881774681755, 783.0105632155462, 0, 0, 6000.8797087871935, 0, 2313.8423504766024, 510.0381442031684, 336.30235141027555, 221.74669257487642, 95.03810202367893, 2502.7994390135113, 500.5598878027023, 125.39142161345269, 0, 632.5687849389012, 500.5598878027023, 576.0301183829441, 576.0301183829441, 900.7006804735692, 0, 2223.1445319256677, 3188.3592869921395, 1022.0543895850378, 0, 0.0, 0.0, 805.873730229658, 161.1747460459316, 82.54410166513722, 903.6188619084651, 161.1747460459316, 134.52798248478467, 576.0301183829441, 900.7006804735692, 0, 2509.7837625013653, 3190.19671795737, 480.36662652265136, 633.4758600887629, 417.6931151734324, 275.41308115330514, 118.03890376613057, 1292.5056510507545, 258.5011302101509, 141.14411277092162, 1772.455781741239, 258.5011302101509, 107.11829987078875, 0, 576.0301183829441, 900.7006804735692, 0, 153.31755725, 0, 0.0, 0, 0.0, 1285.1276633377292, 257.02553266754586, 1824.628694854776, 257.02553266754586, 142.08927424036978, 0, 576.0301183829441, 900.7006804735692, 900.7006804735692, 0, 1178.2894331421735, 4223.063480856484, 976.5580624749117, 643.910218150573, 849.1463743342354, 363.9344461914083, 155.9781506792534, 0, 1255.6157124856272, 251.12314249712546, 1022.1936644392313, 251.12314249712546, 109.63873045598376, 576.0301183829441, 900.7006804735692, 0, 3257.1415831205322, 3799.4089764878854, 868.9653985140942, 1145.9343193674872, 755.591342618303, 498.212041816546, 0, 2310.5312701273706, 462.10625402547413, 0, 0, 766.7540390954812, 462.10625402547413, 486.7894270854704, 811.3805111581383, 0, 5895.050139034032, 3337.839680761802, 896.6588150159101, 591.2272862919115, 389.83579729810106, 167.07917419597524, 71.60822747291868, 1300.1151081234912, 260.02302162469823, 0, 955.9090812278937, 260.02302162469823, 629.0633445854704, 629.0633445854704, 953.7811382208446, 0, 1209.47125907775, 241.89425181554998, 127.91185219864774, 938.5181101900481, 241.89425181554998, 629.0633445854704, 953.7811382208446, 0, 1342.275037912208, 268.4550075824416, 629.0633445854704, 629.0633445854704, 953.7811382208446, 0, 2614.9861916730333, 522.9972383346067, 0, 0, 1188.3912941833914, 237.6782588366783, 83.80431695773473, 0, 2777.3019213595935, 555.4603842719188, 0, 0, 0, 1187.3372959386734, 237.46745918773468, 0, 0, 0, 290.97386695716546, 0, 0, 0, 0, 0, 0, 953.7811382208446, 0, 0, 0, 0, 1933.9521255948644, 237.46745918773468, 96.72152370685923, 0, 0, 290.97386695716546, 0, 629.0633445854704, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 460.19801458016184, 303.43941169231334, 0, 164.759166, 583.2664680334651, 249.98135238133307, 164.8294692662729, 897.8274324284013, 179.56548648568025, 84.43442460403347, 636.2418029828307, 179.56548648568025, 114.36453780322444, 629.0633445854704, 953.7811382208446, 0, 2953.1858957699633, 4370.000964336176, 459.2089639908113, 302.78726431345024, 199.6479481447093, 85.56683233590104, 0, 2093.4076317154786, 418.68152634309575, 146.18497394131168, 0, 832.3654298291716, 418.68152634309575, 109.95378427913315, 486.7894270854704, 811.3805111581383, 811.3805111581383, 0, 0, 6160.316491496222, 0, 2438.857461557048, 450.3075086866562, 593.8358758073641, 254.51127994273966, 167.81635428248927, 728.2522801623678, 145.65045603247356, 968.7680377787073, 145.65045603247356, 503.81003642412315, 839.7504591007306, 839.7504591007306, 0, 0, 1849.825865235847, 0, 2422.3720232024402, 463.1651663482136, 305.3958538289028, 302.05194921469604, 199.16310559018848, 85.35903434970825, 56.282935486649514, 37.111113675633774, 798.3363970209319, 159.6672794041864, 941.3952422135667, 159.6672794041864, 520.8306457627759, 520.8306457627759, 868.1204070433229, 0, 2185.261573564977, 437.05231471299544, 0, 520.8306457627759, 868.1204070433229, 868.1204070433229, 0, 1224.8203652009604, 244.9640730401921, 868.1204070433229, 868.1204070433229, 0, 0, 0, 0, 0, 0, 520.8306457627759, 0, 0, 1672.6429495054608, 244.9640730401921, 106.38166323392869, 0, 0, 0, 0, 307.4580434463416, 0, 0, 0, 0, 0, 0, 176.28078599999998, 460.19801458016184, 303.43941169231334, 400.15590528862924, 263.8496226385524, 113.08293740058684, 812.2897414095485, 162.4579482819097, 1698.064022278244, 162.4579482819097, 123.60536109085047, 0, 520.8306457627759, 868.1204070433229, 0, 1281.9646515681147, 4031.153524194894]*&*['Hit', 'Active', 'Crit', 'Active', 'Hit', 'Active', 'Hit', 'Hit', 'Crit', 'Crit', 'Glance', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Crit', 'Active', 'Active', 'Proc', 'Glance', 'Active', 'Hit', 'DOT', 'Proc', 'DOT', 'DOT', 'Active', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Active', 'DOT', 'DOT', 'Proc', 'DOT', 'Active', 'Active', 'Crit', 'Hit', 'Miss', 'Hit', 'Hit', 'Glance', 'Active', 'Hit', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'Proc', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Refresh', 'Hit', 'Active', 'Hit', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Refresh', 'Proc', 'Hit', 'Active', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Dodge', 'Hit', 'Refresh', 'Crit', 'Active', 'Hit', 'Refresh', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'Proc', 'DOT', 'Crit', 'Crit', 'Hit', 'Glance', 'Hit', 'Refresh', 'Glance', 'Active', 'Glance', 'Active', 'DOT', 'DOT', 'DOT', 'Crit', 'Hit', 'Hit', 'Crit', 'Glance', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'Proc', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Refresh', 'Hit', 'Active', 'Hit', 'Glance', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Crit', 'Hit', 'Glance', 'Hit', 'Crit', 'Active', 'Refresh', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'Proc', 'DOT', 'DOT', 'Hit', 'Crit', 'Miss', 'Dodge', 'Hit', 'Crit', 'Refresh', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Crit', 'Active', 'Hit', 'Refresh', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Glance', 'Hit', 'Refresh', 'Glance', 'Active', 'Hit', 'Miss', 'DOT', 'Proc', 'DOT', 'Proc', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'Hit', 'Refresh', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'Proc', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'Hit', 'Refresh', 'Crit', 'Active', 'Refresh', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Glance', 'Hit', 'Active', 'Hit', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'Proc', 'DOT', 'Hit', 'Hit', 'Crit', 'Hit', 'Glance', 'Glance', 'Active', 'Glance', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Proc', 'Crit', 'Active', 'Refresh', 'Hit', 'Active', 'DOT', 'DOT', 'Proc', 'DOT', 'Applied', 'Hit', 'Hit', 'Refresh', 'Hit', 'Hit', 'Hit', 'Glance', 'Glance', 'DOT', 'Crit', 'Active', 'Hit', 'Refresh', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'DOT', 'Applied', 'Hit', 'Refresh', 'Crit', 'Hit', 'Hit', 'Glance', 'Hit', 'Refresh', 'DOT', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'Proc', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'Crit', 'DOT', 'Hit', 'Active', 'Hit', 'Glance', 'Active', 'DOT', 'DOT', 'Applied', 'Crit', 'Refresh', 'Crit', 'Hit', 'Hit', 'Crit', 'Hit', 'Refresh', 'Glance', 'Active', 'Hit', 'Crit', 'Active', 'Refresh', 'DOT', 'Proc', 'DOT', 'DOT', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Glance', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Active', 'Hit', 'DOT', 'Glance', 'Active', 'Hit', 'DOT', 'Glance', 'Active', 'Hit', 'DOT', 'Crit', 'Active', 'Refresh', 'Hit', 'Active', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'DOT', 'Active', 'Dodge', 'Glance', 'Glance', 'Crit', 'Hit', 'Glance', 'Active', 'Glance', 'Active', 'DOT', 'DOT', 'DOT', 'Applied', 'Crit', 'Refresh', 'Hit', 'Hit', 'Hit', 'Hit', 'Glance', 'Crit', 'Active', 'Hit', 'Refresh', 'Glance', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Hit', 'Hit', 'Crit', 'Dodge', 'Glance', 'Hit', 'Glance', 'Active', 'Hit', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Hit', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'Dodge', 'Hit', 'Dodge', 'Glance', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'Proc', 'DOT', 'Hit', 'Crit', 'Crit', 'Hit', 'Crit', 'Glance', 'Glance', 'Refresh', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'DOT', 'Crit', 'Crit', 'Crit', 'Crit', 'Hit', 'Hit', 'Refresh', 'Crit', 'Active', 'Refresh', 'Proc', 'Hit', 'Active', 'DOT', 'DOT', 'DOT', 'Crit', 'Hit', 'Crit', 'Hit', 'Hit', 'Glance', 'Glance', 'Hit', 'Active', 'Proc', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Hit', 'Active', 'Hit', 'Hit', 'Active', 'DOT', 'DOT', 'DOT', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Crit', 'Active', 'Refresh', 'DOT', 'Hit', 'Active', 'Hit', 'DOT', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'Hit', 'Active', 'DOT', 'DOT', 'DOT', 'Hit', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'Hit', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Hit', 'Glance', 'Active', 'Hit', 'Glance', 'Active', 'Hit', 'DOT', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Refresh', 'Crit', 'Active', 'Hit', 'Refresh', 'Hit', 'Active', 'Hit', 'DOT', 'DOT', 'Proc', 'DOT', 'Applied', 'Crit', 'Refresh', 'Hit', 'Hit', 'Crit', 'Glance', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'DOT', 'DOT', 'Proc', 'DOT', 'Applied', 'Hit', 'Refresh', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'Crit', 'Active', 'Refresh', 'DOT', 'DOT', 'Proc', 'DOT', 'Hit', 'Active', 'DOT', 'Proc', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'Hit', 'Glance', 'Glance', 'Active', 'Crit', 'Active', 'Hit', 'Refresh', 'DOT', 'DOT', 'DOT', 'Hit', 'Crit']*&*[0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 10000, 10000, 37.9391429947039, 37.9391429947039, 37.9391429947039, 37.9391429947039, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 100.63637633298059, 10000, 10000, 10000, 10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 10000]*&*[0, 0, 0, 0, 0, 0, 0, 0, 0, 17.1, 17.1, 17.1, 17.1, 10000, 10000, 10000, 10000, 10000, 10000, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 37.9391429947039, 37.9391429947039, 37.9391429947039, 37.9391429947039, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 41.2652383245065, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 100.63637633298059, 100.63637633298059, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 0, 0, 0, 0, 0, 0, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 10000, 10000, 10000, 10000, 10000, 10000, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 32.1130476649013, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 74.70079764345213, 74.70079764345213, 74.70079764345213, 74.70079764345213, 84.6109629833174, 84.6109629833174, 88.31604565325004, 88.31604565325004, 88.31604565325004, 88.31604565325004, 88.31604565325004, 88.31604565325004, 88.31604565325004, 88.31604565325004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*&*[0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[10000, 10000, 10000, 10000, 10000, 12.3, 12.3, 7.199999999999999, 7.199999999999999, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 32.5260953298026, 32.5260953298026, 32.5260953298026, 32.5260953298026, 32.5260953298026, 32.5260953298026, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 52.917428984111694, 52.917428984111694, 52.917428984111694, 52.917428984111694, 52.917428984111694, 52.917428984111694, 61.65657197881559, 61.65657197881559, 61.65657197881559, 61.65657197881559, 61.65657197881559, 61.65657197881559, 10000, 10000, 10000, 10000, 10000, 10000, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 70.9957149735195, 89.52112832318268, 89.52112832318268, 89.52112832318268, 89.52112832318268, 89.52112832318268, 89.52112832318268, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 114.95162434277832, 114.95162434277832, 114.95162434277832, 114.95162434277832, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 125.54535293365282, 125.54535293365282]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 24.4, 24.4, 26.8, 26.8, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 58.74352431391429, 58.74352431391429, 58.74352431391429, 58.74352431391429, 58.74352431391429, 58.74352431391429, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 67.48266730861819, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 78.40588031338477, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 107.54145900291304, 107.54145900291304, 107.54145900291304, 107.54145900291304, 107.54145900291304, 107.54145900291304, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095, 118.65670701271095]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 10000, 10000, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 24.4, 24.4, 26.8, 26.8, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 29.2, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052, 38.3521906596052]*&*[0, 0.0, 2.4, 2.4, 4.8, 4.799999999999999, 7.199999999999999, 7.199999999999999, 9.6, 9.6, 12.0, 12.0, 14.4, 14.4, 16.8, 16.8, 19.2, 19.2, 22.1130476649013, 22.1130476649013, 25.026095329802597, 25.026095329802597, 27.939142994703897, 27.939142994703897, 30.852190659605196, 30.8521906596052, 33.7652383245065, 33.7652383245065, 36.6782859894078, 36.6782859894078, 39.591333654309096, 39.591333654309096, 42.504381319210395, 42.504381319210395, 45.417428984111694, 45.417428984111694, 48.330476649012994, 48.330476649012994, 51.24352431391429, 51.24352431391429, 54.15657197881559, 54.15657197881559, 57.06961964371689, 57.06961964371689, 59.98266730861819, 59.98266730861819, 62.89571497351949, 62.99571497351949, 63.09571497351949, 63.19571497351949, 63.295714973519495, 63.395714973519496, 63.4957149735195, 63.4957149735195, 67.20079764345213, 67.20079764345213, 70.90588031338477, 70.90588031338477, 74.6109629833174, 74.6109629833174, 78.31604565325004, 78.31604565325004, 82.02112832318268, 82.02112832318268, 85.72621099311532, 85.72621099311532, 89.43129366304795, 89.43129366304795, 93.13637633298059, 93.13637633298059, 96.84145900291323, 96.94145900291322, 97.04145900291321, 97.14145900291321, 97.2414590029132, 97.3414590029132, 97.44145900291319, 97.54145900291319, 97.64145900291318, 97.74145900291317, 97.84145900291317, 97.94145900291316, 98.04145900291316, 98.14145900291315, 98.24145900291315, 98.34145900291314, 98.44145900291313, 98.54145900291313, 98.64145900291312, 98.74145900291312, 98.84145900291311, 98.9414590029131, 99.0414590029131, 99.1414590029131, 99.24145900291309, 99.34145900291308, 99.44145900291308, 99.54145900291307, 99.64145900291307, 99.74145900291306, 99.84145900291306, 99.94145900291305, 100.04145900291304, 100.04145900291304, 103.74654167284568, 103.74654167284568, 107.45162434277832, 107.45162434277832, 111.15670701271095, 111.15670701271095, 116.24535293365292, 116.34535293365292, 116.44535293365291, 116.54535293365291, 116.6453529336529, 116.7453529336529, 116.84535293365289, 116.94535293365288, 117.04535293365288, 117.14535293365287, 117.24535293365287, 117.34535293365286, 117.44535293365286, 117.54535293365285, 117.64535293365284, 117.74535293365284, 117.84535293365283, 117.94535293365283, 118.04535293365282, 118.04535293365282, 123.1339988545948]*&*[10, 25, 25, 40.0, 40.0, 50.0, 50.0, 40.0, 40.0, 60.0, 60.0, 80.0, 80.0, 100.0, 100.0, 120.0, 120.0, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 98, 98, 66, 66, 34, 34, 44, 44, 12, 12, 22, 22, 32, 32, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 10, 10, 20, 20, 40, 40, 60, 60, 70, 70, 38, 38, 6, 6, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 36, 36, 4, 4, 14, 14, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 34, 34]*&*360.367*^*10.99*^*31.15*^*934.4*^*1301.3697277900799*^*1090.5228000000002*^*18846.228000000003*^*15394.7*^*472.26*^*3763.643956693731*^*28.0*^*24.0*^*26*^*210.10000000000002*^*0.0*^*0.0*^*False*&*250*[3629, 3479, 3551, 3531, 3563, 3947, 3612, 3615, 3537, 3739, 3697, 3444, 3515, 3703, 3530, 3559, 3644, 3498, 3820, 3369, 3946, 4171, 3572, 3581, 3669, 3624, 3906, 3928, 3792, 3666, 3525, 3707, 3565, 3514, 3736, 3686, 3338, 3601, 3953, 3488, 3997, 3707, 4283, 3933, 3237, 3856, 3547, 3872, 3682, 3754, 3834, 3734, 3444, 3543, 3486, 4302, 4360, 3648, 3579, 3397, 3529, 3539, 3513, 3569, 3622, 3683, 3802, 3678, 3642, 3753, 3550, 3502, 3574, 3958, 3626, 3919, 3476, 3721, 3621, 3675, 3638, 3900, 3385, 3727, 3763, 3964, 3582, 3592, 3737, 3730, 3879, 3811, 3508, 4038, 4086, 3805, 3659, 3691, 3679, 3614, 3956, 3948, 3554, 3517, 3581, 3592, 3599, 3395, 3393, 3613, 3519, 3825, 3495, 4118, 3716, 3859, 3340, 3641, 3603, 3808, 3921, 3715, 3859, 3957, 3695, 3491, 3407, 3694, 3505, 3653, 3704, 3952, 3802, 3750, 3501, 3679, 3299, 3712, 4044, 3757, 3427, 3647, 3710, 3839, 3503, 3980, 3466, 3611, 3470, 3864, 3829, 3523, 3878, 3654, 3690, 3931, 3695, 3810, 3443, 3674, 4033, 3489, 3709, 3455, 3433, 3668, 3689, 3936, 3665, 3597, 3811, 3635, 3503, 3929, 3755, 3442, 3736, 3681, 3311, 3807, 3778, 3544, 4001, 3595, 3621, 3912, 3930, 3554, 3612, 3673, 3861, 3963, 3651, 3592, 3618, 3693, 4091, 3618, 3541, 3705, 3933, 3783, 3480, 3451, 3808, 3276, 3784, 3642, 3914, 3620, 3662, 3532, 3392, 3608, 3588, 3794, 3850, 3671, 3735, 3681, 3457, 3521, 3752, 3477, 3531, 3754, 3613, 3627, 3848, 3954, 3944, 3628, 3500, 3799, 3711, 3410, 3967, 3688, 4261, 3680, 3610, 3693, 3874, 3730, 3928, 3764, 3775, 4128, 3413, 3505]"""
r_results = """1500.243*&*192012.03125990916*&*124.25*&*['Main hand', 'Off hand', 'Icy Touch', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Death Chill', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Blood Tap', 'Unbreakable Armor', 'Main hand', 'Mirror of Truth', 'Off hand', 'Meteorite Whetstone', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Meteorite Whetstone', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Unbreakable Armor', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Meteorite Whetstone', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Mirror of Truth', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate']*&*[0, 0, 0, 2.0, 2.08, 0, 2.4, 2.4, 3.666666666666667, 4.16, 3, 2.4, 4.8, 4.8, 5.333333333333334, 6.24, 6, 5.4, 7.199999999999999, 7.199999999999999, 7.000000000000001, 9.6, 8.32, 9.6, 9, 8.4, 9.6, 9.6, 8.666666666666668, 10.4, 12, 11.4, 12.0, 12.0, 10.333333333333334, 12.48, 14.4, 14.4, 14.4, 12.0, 14.56, 15, 16.8, 16.8, 13.666666666666666, 16.64, 18, 17.4, 19.2, 15.333333333333332, 18.72, 21, 20.4, 21.599999999999998, 21.599999999999998, 17.0, 20.799999999999997, 23.4, 23.999999999999996, 23.999999999999996, 19.02294976729257, 23.324641309581125, 24, 26.4, 26.913047664901296, 26.913047664901296, 21.04589953458514, 25.849282619162253, 27, 29.4, 29.826095329802595, 29.826095329802595, 23.06884930187771, 28.37392392874338, 30, 32.4, 32.7391429947039, 25.09179906917028, 30.898565238324508, 33, 35.4, 35.652190659605196, 35.652190659605196, 27.114748836462848, 33.423206547905636, 36, 38.4, 38.565238324506495, 38.565238324506495, 29.137698603755418, 35.947847857486764, 39, 41.4, 41.478285989407794, 41.478285989407794, 31.160648371047987, 38.47248916706789, 42, 44.39133365430909, 44.39133365430909, 33.18359813834056, 40.99713047664902, 45, 44.4, 47.30438131921039, 35.20654790563313, 43.52177178623015, 48, 47.4, 50.21742898411169, 50.21742898411169, 37.2294976729257, 46.046413095811275, 51, 50.4, 53.13047664901299, 53.13047664901299, 56.04352431391429, 39.252447440218276, 48.5710544053924, 54, 53.4, 56.04352431391429, 56.04352431391429, 41.27539720751085, 51.09569571497353, 57, 56.4, 58.95657197881559, 58.95657197881559, 43.29834697480342, 53.62033702455466, 60, 59.4, 61.86961964371689, 45.321296742095996, 56.144978334135786, 63, 62.4, 64.78266730861819, 64.78266730861819, 47.34424650938857, 58.66961964371691, 66, 65.4, 67.69571497351949, 49.36719627668114, 61.19426095329804, 69, 68.4, 70.60876263842079, 70.60876263842079, 51.940170353023255, 64.40533260057299, 72, 71.4, 74.31384530835342, 54.51314442936537, 67.61640424784794, 75, 74.4, 78.01892797828606, 78.01892797828606, 57.08611850570748, 70.82747589512289, 78, 77.4, 81.7240106482187, 81.7240106482187, 59.659092582049595, 74.03854754239784, 81, 80.4, 85.42909331815133, 85.42909331815133, 62.23206665839171, 77.24961918967279, 84, 83.4, 89.13417598808397, 64.80504073473382, 80.46069083694773, 87, 86.4, 92.8392586580166, 92.8392586580166, 67.37801481107593, 83.67176248422268, 90, 89.4, 96.54434132794924, 96.54434132794924, 69.95098888741803, 86.88283413149763, 93, 92.4, 100.24942399788188, 100.24942399788188, 72.52396296376014, 90.09390577877258, 96, 95.4, 103.95450666781451, 75.09693704010225, 107.65958933774715, 93.30497742604753, 99, 98.4, 107.65958933774715, 107.65958933774715, 77.66991111644435, 96.51604907332248, 102, 101.4, 111.36467200767979, 111.36467200767979, 80.24288519278646, 99.72712072059743, 105, 104.4, 115.06975467761242, 115.06975467761242, 118.77483734754506, 82.81585926912857, 102.93819236787238, 108, 107.4, 118.77483734754506, 85.38883334547067, 106.14926401514732, 111, 110.4, 122.4799200174777, 122.4799200174777]*&*[598.7359760814339, 889.8212651477767, 1781.0003816000003, 676.8683473516825, 523.7732129214289, 189.33639559999997, 349.07381438784705, 1010.6388467284146, 1391.7075667225508, 0.0, 189.33639559999997, 363.8770191419142, 0, 98.92300000000002, 673.9475110425143, 941.3010050968658, 189.33639559999997, 363.8770191419142, 0, 0, 1231.0615697183018, 0, 325.50155754137427, 0, 189.33639559999997, 363.8770191419142, 1068.1142112947741, 3481.4437818162355, 569.7204007707893, 641.5168129836504, 292.73376153049594, 467.3664710657689, 3456.987673475344, 4251.192274814757, 515.1372722432092, 0.0, 467.3664710657689, 686.6380602059644, 2188.7983019726244, 818.0761980793893, 585.1081617628404, 292.73376153049594, 1354.2286212387169, 1749.9030125484787, 1687.2670315692217, 1226.0773179385217, 292.73376153049594, 467.3664710657689, 113.4705, 545.5139698585581, 378.89639744512675, 292.73376153049594, 467.3664710657689, 3188.394206111068, 4434.1192405976235, 0.0, 485.59109608618223, 397.72950736939936, 608.4633117734933, 2064.8683331340894, 699.3650652281976, 1120.1448439399405, 223.158761530496, 397.72950736939936, 3083.2204023435565, 1645.3432719129316, 1213.2570248242168, 366.5389127567398, 223.158761530496, 397.72950736939936, 555.1492829712013, 705.3269748079011, 586.3224217674692, 542.3935443923758, 189.33639559999997, 363.8770191419142, 96.01350000000001, 1133.2135533611684, 430.67155556669354, 189.33639559999997, 363.8770191419142, 1179.3216078543478, 1552.4482853222812, 392.97547165485076, 989.4948041981404, 189.33639559999997, 363.8770191419142, 1063.3819816539412, 3478.8673456784477, 406.2652768615659, 315.89018056151775, 189.33639559999997, 363.8770191419142, 550.4534969711829, 652.1227567932798, 403.4174614601269, 339.3846576233891, 189.33639559999997, 1180.8990177346259, 3795.7689906262276, 444.23614888075195, 467.91221850858767, 189.33639559999997, 363.8770191419142, 96.01350000000001, 554.9234314439115, 454.76845511733103, 189.33639559999997, 363.8770191419142, 1039.7208334497766, 1440.9779871159935, 365.4465894409407, 849.2946613580684, 189.33639559999997, 363.8770191419142, 509.21056902978694, 753.3858806819097, 0, 605.3078577770624, 534.7263490808094, 189.33639559999997, 363.8770191419142, 2926.0521542066163, 1554.5514984959843, 692.9329470521072, 495.84271571500824, 189.33639559999997, 363.8770191419142, 1196.6731165374024, 3870.485638622045, 427.1492564721183, 332.2651191197917, 189.33639559999997, 363.8770191419142, 110.561, 671.0266747333461, 493.104431675163, 189.33639559999997, 363.8770191419142, 1134.3654262664352, 1394.7072972945161, 692.9329470521072, 307.70271128238073, 189.33639559999997, 363.8770191419142, 0, 679.7891836608505, 447.10125980576447, 189.33639559999997, 363.8770191419142, 2533.7897522285716, 3857.603457933112, 437.97503588993453, 501.4731435172841, 223.158761530496, 397.72950736939936, 197.84600000000003, 1487.8156378860244, 591.8365168321741, 223.158761530496, 397.72950736939936, 2826.22089759932, 0, 1460.0676929489268, 586.3599487524839, 223.158761530496, 397.72950736939936, 1397.9886400000612, 4301.286911029314, 434.65258458825576, 535.427865611364, 223.158761530496, 397.72950736939936, 3089.6201828603057, 4442.681726271054, 654.0921024360911, 1041.2822635924003, 223.158761530496, 397.72950736939936, 107.6515, 567.3369857578762, 918.2994191621665, 189.33639559999997, 363.8770191419142, 1163.6039839307941, 1646.8737281335843, 1093.782263187398, 503.5099110265746, 189.33639559999997, 363.8770191419142, 1325.2569484616472, 1731.67528329731, 553.4630132893274, 1005.9245084372113, 189.33639559999997, 363.8770191419142, 612.0013722863232, 1966.0813820396907, 605.3078577770624, 352.5558038550443, 189.33639559999997, 363.8770191419142, 114.92524999999999, 1384.4054759496305, 0, 459.14970958108324, 189.33639559999997, 363.8770191419142, 2887.6212686780423, 4340.715132205334, 1112.767699196991, 298.0913343025243, 189.33639559999997, 363.8770191419142, 1281.089471813873, 1550.2941791971182, 694.3933652066913, 433.40983960653875, 189.33639559999997, 363.8770191419142, 0, 2170.3405034072034, 0, 1209.1552973995406, 0.0, 189.33639559999997, 363.8770191419142, 194.9365, 467.2898926066864, 1092.1413373489074, 258.9113956, 433.5139828382838, 3301.912199634163, 1742.7802488544658]*&*['Hit', 'Crit', 'Crit', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Crit', 'Miss', 'DOT', 'DOT', 'Active', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Active', 'Active', 'Crit', 'Proc', 'Glance', 'Proc', 'DOT', 'DOT', 'Hit', 'Crit', 'Glance', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Glance', 'Miss', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Crit', 'Crit', 'DOT', 'DOT', 'Hit', 'Glance', 'Glance', 'DOT', 'DOT', 'Crit', 'Crit', 'Dodge', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'Crit', 'DOT', 'DOT', 'Crit', 'Hit', 'Crit', 'Glance', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Hit', 'Crit', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Glance', 'Crit', 'DOT', 'DOT', 'Hit', 'Crit', 'Glance', 'Glance', 'DOT', 'DOT', 'Hit', 'Hit', 'Glance', 'Glance', 'DOT', 'Hit', 'Crit', 'Glance', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Glance', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'Proc', 'Hit', 'Hit', 'DOT', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Hit', 'Crit', 'Glance', 'Glance', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Glance', 'DOT', 'DOT', 'Active', 'Hit', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Glance', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'DOT', 'DOT', 'Crit', 'Dodge', 'Crit', 'Hit', 'DOT', 'DOT', 'Hit', 'Crit', 'Glance', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'Crit', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Hit', 'Crit', 'Hit', 'Glance', 'DOT', 'DOT', 'Hit', 'Crit', 'Proc', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Crit', 'Glance', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Dodge', 'Crit', 'Proc', 'Crit', 'Dodge', 'DOT', 'DOT', 'Crit', 'Glance', 'Crit', 'DOT', 'DOT', 'Crit', 'Hit']*&*[0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 0, 0, 0, 0, 0, 0, 0, 0, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 75.19571497351949, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 79.01892797828606, 79.01892797828606, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715]*&*[0, 0, 0, 0, 0, 0, 0, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 14.7, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979]*&*[0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 43.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 53.152190659605196, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 63.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 73.54352431391429, 79.01892797828606, 79.01892797828606, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 89.2240106482187, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 100.3392586580166, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715, 115.15958933774715]*&*[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 24.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 34.7, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 46.065238324506495, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 57.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 67.71742898411169, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 78.10876263842079, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 92.92909331815133, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 104.04434132794924, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979, 118.86467200767979]*&*[10000, 10000, 10000, 10000, 10000, 12.3, 12.3, 7.199999999999999, 7.199999999999999, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 27.1, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 54.80438131921039, 69.36961964371689, 69.36961964371689, 69.36961964371689, 69.36961964371689, 69.36961964371689, 69.36961964371689, 69.36961964371689, 69.36961964371689, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 81.81384530835342, 111.45450666781451, 111.45450666781451, 111.45450666781451, 111.45450666781451, 111.45450666781451, 111.45450666781451, 111.45450666781451, 111.45450666781451, 126.27483734754506, 126.27483734754506]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 40.2391429947039, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397, 96.63417598808397]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]*&*[0, 0.0, 2.4, 2.4, 4.8, 4.799999999999999, 7.199999999999999, 7.199999999999999, 9.6, 9.6, 12.0, 12.0, 14.4, 14.4, 16.8, 16.8, 19.2, 19.2, 21.599999999999998, 21.599999999999998, 23.999999999999996, 23.999999999999996, 26.913047664901296, 26.913047664901296, 29.826095329802595, 29.826095329802598, 32.7391429947039, 32.7391429947039, 35.652190659605196, 35.652190659605196, 38.565238324506495, 38.565238324506495, 41.478285989407794, 41.478285989407794, 44.39133365430909, 44.39133365430909, 47.30438131921039, 47.30438131921039, 50.21742898411169, 50.21742898411169, 53.13047664901299, 53.13047664901299, 56.04352431391429, 56.04352431391429, 58.95657197881559, 58.95657197881559, 61.86961964371689, 61.86961964371689, 64.78266730861819, 64.78266730861819, 67.69571497351949, 67.69571497351949, 70.60876263842079, 70.60876263842079, 74.31384530835342, 74.31384530835342, 78.01892797828606, 78.01892797828606, 81.7240106482187, 81.7240106482187, 85.42909331815133, 85.42909331815133, 89.13417598808397, 89.13417598808397, 92.8392586580166, 92.8392586580166, 96.54434132794924, 96.54434132794924, 100.24942399788188, 100.24942399788188, 103.95450666781451, 103.95450666781451, 107.65958933774715, 107.65958933774715, 111.36467200767979, 111.36467200767979, 115.06975467761242, 115.06975467761242, 118.77483734754506, 118.77483734754506, 122.4799200174777]*&*[10, 25, 25, 35, 35, 45, 45, 35, 35, 55, 55, 75, 75, 43, 43, 63, 63, 73, 73, 93, 93, 61, 61, 81, 81, 49, 49, 59, 59, 79, 79, 99, 99, 67, 67, 87, 87, 97, 97, 117, 117, 85, 85, 105, 105, 125, 125, 130, 130, 130, 130, 120, 120, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 98, 98, 108, 108, 128, 128, 130, 130, 98, 98, 108, 108]*&*360.367*^*10.99*^*23.15*^*568.0*^*1145.664*^*1058.76*^*18528.6*^*15394.7*^*472.26*^*2721.328*^*28.0*^*14.0*^*15*^*123.2*^*0.0*^*0.0*^*False*&*250*[1538, 1550, 1295, 1326, 1545, 1503, 1391, 1511, 1511, 1546, 1484, 1546, 1482, 1326, 1542, 1409, 1328, 1678, 1394, 1496, 1583, 1489, 1394, 1574, 1481, 1584, 1344, 1441, 1535, 1630, 1468, 1404, 1654, 1636, 1598, 1570, 1550, 1498, 1569, 1464, 1443, 1558, 1583, 1642, 1604, 1562, 1438, 1482, 1458, 1592, 1540, 1598, 1573, 1541, 1483, 1509, 1579, 1549, 1425, 1558, 1505, 1417, 1493, 1446, 1485, 1654, 1553, 1440, 1555, 1538, 1415, 1578, 1563, 1433, 1476, 1540, 1610, 1566, 1501, 1440, 1528, 1456, 1485, 1537, 1483, 1442, 1439, 1491, 1563, 1411, 1624, 1478, 1573, 1496, 1343, 1477, 1595, 1487, 1631, 1523, 1526, 1510, 1466, 1497, 1382, 1476, 1528, 1518, 1463, 1585, 1546, 1413, 1558, 1492, 1429, 1629, 1667, 1510, 1549, 1396, 1440, 1521, 1469, 1451, 1553, 1639, 1391, 1510, 1496, 1592, 1503, 1483, 1545, 1408, 1491, 1431, 1408, 1469, 1583, 1456, 1641, 1490, 1461, 1386, 1460, 1408, 1503, 1351, 1375, 1580, 1514, 1524, 1641, 1535, 1545, 1529, 1476, 1573, 1520, 1480, 1637, 1647, 1593, 1563, 1451, 1382, 1533, 1453, 1402, 1532, 1418, 1420, 1504, 1557, 1464, 1316, 1408, 1481, 1495, 1484, 1386, 1542, 1458, 1525, 1459, 1461, 1404, 1471, 1437, 1519, 1435, 1456, 1580, 1369, 1477, 1360, 1436, 1463, 1454, 1505, 1483, 1521, 1500, 1416, 1394, 1392, 1536, 1518, 1444, 1658, 1444, 1429, 1645, 1395, 1470, 1438, 1389, 1470, 1517, 1588, 1384, 1522, 1364, 1506, 1630, 1502, 1614, 1567, 1547, 1580, 1480, 1589, 1513, 1526, 1629, 1492, 1559, 1478, 1515, 1498, 1448, 1506, 1560, 1538, 1520, 1453, 1437, 1638, 1517, 1545]"""

import_from_clipboard = True

if import_from_clipboard == True:
    import pyperclip as pc
    r_results = pc.paste()





#Type in number of targets if you want correct showing
num_targ = 1

#Type in gear added else just use this data as a 'default'
gear_currently_worn = "Conqueror's Darkruned Helmet*&*Might of the Leviathan*&*Valorous Darkruned Shoulderplates*&*Aged Winter Cloak*&*Conqueror's Darkruned Battleplate*&*Bracers of the Tyrant*&*Valorous Darkruned Gauntlets*&*Girdle of Razuvious*&*Legplates of the Violet Champion*&*Greaves of Iron Intensity*&*Ruthlessness*&*Greatring of Collision*&*Darkmoon Card: Greatness*&*Grim Toll*&*Sigil of Awareness*&*Serilas Blood Blade of Invar One-Arm*&*Serilas Blood Blade of Invar One-Arm"



r_results_find = r_results.find("*&*")+3
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
total_dam = r_results[:r_results_find-3]
total_dam = float(total_dam)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
fight_length_input = r_results[:r_results_find-3]
fight_length_input = float(fight_length_input)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
ability_order = r_results[:r_results_find-3]
ability_order = ability_order[1:-1]
ability_order = ability_order.replace("\\", "")
ability_order = ast.literal_eval(ability_order)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
timeline_order = r_results[:r_results_find-3]
timeline_order = timeline_order[1:-1]
timeline_order = timeline_order.replace("\\", "")
timeline_order = ast.literal_eval(timeline_order)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
damage_order = r_results[:r_results_find-3]
damage_order = damage_order[1:-1]
damage_order = damage_order.replace("\\", "")
damage_order = ast.literal_eval(damage_order)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
status_order = r_results[:r_results_find-3]
status_order = status_order[1:-1]
status_order = status_order.replace("\\", "")
status_order = ast.literal_eval(status_order)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_0_tracker_i = r_results[:r_results_find-3]
# rune_0_tracker_i = rune_0_tracker_i[1:-1]
# rune_0_tracker_i = rune_0_tracker_i.replace("\\", "")
rune_0_tracker_i = ast.literal_eval(rune_0_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_1_tracker_i = r_results[:r_results_find-3]
# rune_1_tracker_i = rune_1_tracker_i[1:-1]
# rune_1_tracker_i = rune_1_tracker_i.replace("\\", "")
rune_1_tracker_i = ast.literal_eval(rune_1_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_2_tracker_i = r_results[:r_results_find-3]
# rune_2_tracker_i = rune_2_tracker_i[1:-1]
# rune_2_tracker_i = rune_2_tracker_i.replace("\\", "")
rune_2_tracker_i = ast.literal_eval(rune_2_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_3_tracker_i = r_results[:r_results_find-3]
# rune_3_tracker_i = rune_3_tracker_i[1:-1]
# rune_3_tracker_i = rune_3_tracker_i.replace("\\", "")
rune_3_tracker_i = ast.literal_eval(rune_3_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_4_tracker_i = r_results[:r_results_find-3]
# rune_4_tracker_i = rune_4_tracker_i[1:-1]
# rune_4_tracker_i = rune_4_tracker_i.replace("\\", "")
rune_4_tracker_i = ast.literal_eval(rune_4_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_5_tracker_i = r_results[:r_results_find-3]
# rune_5_tracker_i = rune_5_tracker_i[1:-1]
# rune_5_tracker_i = rune_5_tracker_i.replace("\\", "")
rune_5_tracker_i = ast.literal_eval(rune_5_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_6_tracker_i = r_results[:r_results_find-3]
# rune_6_tracker_i = rune_6_tracker_i[1:-1]
# rune_6_tracker_i = rune_6_tracker_i.replace("\\", "")
rune_6_tracker_i = ast.literal_eval(rune_6_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_7_tracker_i = r_results[:r_results_find-3]
# rune_7_tracker_i = rune_7_tracker_i[1:-1]
# rune_7_tracker_i = rune_7_tracker_i.replace("\\", "")
rune_7_tracker_i = ast.literal_eval(rune_7_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_8_tracker_i = r_results[:r_results_find-3]
# rune_8_tracker_i = rune_8_tracker_i[1:-1]
# rune_8_tracker_i = rune_8_tracker_i.replace("\\", "")
rune_8_tracker_i = ast.literal_eval(rune_8_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_9_tracker_i = r_results[:r_results_find-3]
# rune_9_tracker_i = rune_9_tracker_i[1:-1]
# rune_9_tracker_i = rune_9_tracker_i.replace("\\", "")
rune_9_tracker_i = ast.literal_eval(rune_9_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_10_tracker_i = r_results[:r_results_find-3]
# rune_10_tracker_i = rune_10_tracker_i[1:-1]
# rune_10_tracker_i = rune_10_tracker_i.replace("\\", "")
rune_10_tracker_i = ast.literal_eval(rune_10_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_11_tracker_i = r_results[:r_results_find-3]
# rune_11_tracker_i = rune_11_tracker_i[1:-1]
# rune_11_tracker_i = rune_11_tracker_i.replace("\\", "")
rune_11_tracker_i = ast.literal_eval(rune_11_tracker_i)
r_results = r_results[r_results_find:]
r_results_find = r_results.find("*&*")+3
rune_time_tracker_i = r_results[:r_results_find-3]
# rune_time_tracker_i = rune_time_tracker_i[1:-1]
# rune_time_tracker_i = rune_time_tracker_i.replace("\\", "")
rune_time_tracker_i = ast.literal_eval(rune_time_tracker_i)
r_results = r_results[r_results_find:]

r_results_find = r_results.find("*&*")+3
rune_power_tracker_i = r_results[:r_results_find-3]
# rune_power_tracker_i = rune_power_tracker_i[1:-1]
# rune_power_tracker_i = rune_power_tracker_i.replace("\\", "")
rune_power_tracker_i = ast.literal_eval(rune_power_tracker_i)
r_results = r_results[r_results_find:]


r_results_find = r_results.find("*&*")+3
extra_sim_stats_info = r_results[:r_results_find-3]
r_results = r_results[r_results_find:]

r_results_find = r_results.find("*")+1
num_sims = r_results[:r_results_find-1]
r_results = r_results[r_results_find:]

results_extra_sims = r_results
results_extra_sims = ast.literal_eval(results_extra_sims)


#print(r_results)


#ability_order = ['Main hand', 'Off hand', 'Icy Touch', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Unbreakable Armor', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Off hand', 'Blood Plague', 'Empowered Rune Weapon', 'OH - Obliterate', 'Obliterate', 'Meteorite Whetstone', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Mirror of Truth', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Frost Fever', 'Horn of Winter', 'Main hand', 'Off hand', 'Blood Plague', 'Main hand', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Tap', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'Horn of Winter', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'Frost Fever', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Howling Blast', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Meteorite Whetstone', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'Off hand', 'Main hand', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Main hand', 'Horn of Winter', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Mirror of Truth', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Frost Fever', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Off hand', 'Main hand', 'Blood Plague', 'Frost Fever', 'Main hand', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Blood Plague', 'Off hand', 'Pestilence', 'Main hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'Blood Tap', 'Horn of Winter', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Frost Fever', 'Off hand', 'Main hand', 'Blood Plague', 'Off hand', 'Frost Fever', 'Main hand', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Off hand', 'Main hand', 'Main hand', 'Off hand', 'Icy Touch', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Meteorite Whetstone', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Off hand', 'Howling Blast', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Horn of Winter', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Frost Fever', 'Off hand', 'Main hand', 'Blood Plague', 'Horn of Winter', 'Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'Unbreakable Armor', 'Main hand', 'Off hand', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Blood Plague', 'Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'Off hand', 'Blood Plague', 'Main hand', 'Horn of Winter', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Mirror of Truth', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Blood Plague', 'Howling Blast', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Off hand', 'Blood Plague', 'Main hand', 'Frost Fever', 'Off hand', 'Blood Plague', 'Main hand', 'Blood Tap', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'Frost Fever', 'Main hand', 'Blood Plague', 'Off hand', 'Main hand', 'Frost Fever', 'Off hand', 'Main hand', 'Blood Plague', 'Horn of Winter', 'Main hand', 'Off hand', 'Meteorite Whetstone', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Frost Fever', 'Howling Blast', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'Pestilence', 'Main hand', 'Off hand', 'Blood Plague', 'Pestilence', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Blood Plague', 'Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'Blood Plague', 'Off hand', 'Main hand', 'Frost Fever', 'Off hand', 'Horn of Winter', 'Main hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Main hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Main hand', 'Off hand', 'Blood Plague', 'Frost Fever', 'Off hand', 'Main hand', 'Blood Plague', 'Off hand', 'Main hand', 'Frost Fever', 'Main hand', 'Off hand', 'Blood Plague', 'Pestilence', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate']
#timeline_order = [0, 0, 0, 0, 1.5, 1.5, 2.0, 2.08, 3, 1.5, 3.0, 3.666666666666667, 4.16, 4.5, 4.5, 4.5, 5.333333333333334, 6, 6.0, 6.0, 7.000000000000001, 6.24, 7.5, 7.5, 7.5, 7.5, 9.0, 8.666666666666668, 8.32, 9, 9.0, 9.0, 10.083754918493536, 10.088526138279933, 10.275379426644182, 10.275379426644182, 11.500843170320405, 10.5, 11.550758853288364, 11.550758853288364, 11.857052276559866, 12, 12.826138279932547, 12.826138279932547, 14.101517706576729, 12.917931422147273, 13.625578414839799, 13.5, 14.101517706576729, 14.101517706576729, 14.335019673974141, 15, 15.376897133220911, 15.75210792580101, 15.394104553119732, 16.5, 17.169196177627878, 17.162630691399663, 17.252276559865102, 17.252276559865102, 18, 18.527655986509284, 18.527655986509284, 18.586284429454746, 18.931156829679594, 19.5, 19.803035413153466, 20.252951096121414, 21.011156829679592, 21, 21.303035413153466, 21.303035413153466, 21.303035413153466, 21.919617762788082, 22.5, 22.803035413153466, 22.803035413153466, 23.58628442945475, 23.09115682967959, 24, 24.303035413153466, 24.303035413153466, 25.252951096121418, 25.17115682967959, 25.5, 26.80303541315348, 26.80303541315348, 26.919617762788086, 27.251156829679587, 27, 28.5, 28.586284429454754, 29.331156829679585, 30, 30.25295109612142, 30.803035413153516, 30.803035413153516, 31.91961776278809, 31.411156829679584, 31.5, 32.303035413153516, 32.303035413153516, 33.58628442945476, 33.49115682967958, 33, 33.803035413153516, 33.803035413153516, 35.25295109612142, 34.5, 35.303035413153516, 35.303035413153516, 35.57115682967958, 36, 36.803035413153516, 36.803035413153516, 36.919617762788086, 37.65115682967958, 37.5, 38.303035413153516, 38.58628442945475, 39.73115682967958, 39, 39.803035413153516, 39.803035413153516, 40.252951096121414, 40.5, 41.303035413153516, 41.91961776278808, 41.811156829679575, 42, 42.803035413153516, 42.803035413153516, 43.58628442945474, 43.89115682967957, 43.5, 45, 45.25295109612141, 45.97115682967957, 46.5, 46.80303541315355, 46.80303541315355, 46.91961776278807, 48.05115682967957, 48, 48.30303541315355, 48.30303541315355, 48.586284429454736, 49.5, 49.80303541315355, 49.80303541315355, 50.2529510961214, 50.13115682967957, 51, 51.30303541315355, 51.919617762788064, 52.21115682967957, 52.5, 52.80303541315355, 52.80303541315355, 53.58628442945473, 54.30303541315355, 54.291156829679565, 54, 54.30303541315355, 54.30303541315355, 55.25295109612139, 55.5, 56.059682967959496, 56.67003934794826, 56.87841483979775, 56.87841483979775, 58.08712759977513, 57.82820910623943, 57, 58.153794266441935, 58.153794266441935, 59.42917369308611, 59.504215851602, 59.59673524451936, 60, 58.5, 60.92130410342887, 61.3045531197303, 62.338392355255735, 61.36526138279929, 61.5, 62.879932546374484, 62.879932546374484, 64.15531197301867, 63.7554806070826, 63.13378752107922, 63, 64.15531197301867, 64.15531197301867, 65.17256885890947, 64.90231365935915, 64.5, 65.43069139966285, 65.43069139966285, 66.83923552557614, 66, 66.98231365935915, 67.5, 67.7306913996628, 67.7306913996628, 68.50590219224281, 69.06231365935915, 69, 69.2306913996628, 69.2306913996628, 70.17256885890949, 70.5, 71.13069139966278, 71.13069139966278, 71.83923552557616, 71.14231365935915, 72, 73.22231365935914, 73.50590219224283, 73.5, 75, 75.1725688589095, 75.30231365935914, 75.53069139966262, 75.53069139966262, 76.83923552557617, 76.5, 77.38231365935914, 77.83069139966257, 78.50590219224284, 78, 79.33069139966257, 79.33069139966257, 80.17256885890951, 79.46231365935914, 79.5, 81, 81.23069139966255, 81.23069139966255, 81.83923552557619, 81.54231365935914, 82.5, 82.73069139966255, 82.73069139966255, 83.50590219224286, 83.62231365935914, 84, 84.23069139966255, 84.23069139966255, 85.17256885890953, 85.70231365935913, 85.5, 85.73069139966255, 85.73069139966255, 86.8392355255762, 87, 87.78231365935913, 88.50590219224287, 88.5, 89.86231365935913, 90, 90.17256885890954, 91.33069139966231, 91.33069139966231, 91.83923552557621, 91.94231365935913, 91.5, 92.83069139966231, 92.83069139966231, 93.50590219224289, 94.02231365935913, 93, 94.33069139966231, 94.33069139966231, 95.17256885890956, 94.5, 95.83069139966231, 95.83069139966231, 96.83923552557623, 96.10231365935913, 96, 97.5, 98.18231365935912, 98.5059021922429, 100.17256885890957, 100.26231365935912, 101.43069139966208, 102.17256885890957, 102.34231365935912, 101.43069139966208, 102.93069139966208, 102.93069139966208, 103.83923552557624, 104.42231365935912, 104.43069139966208, 102.93069139966208, 104.43069139966208, 104.43069139966208, 105.50590219224291, 105.93069139966208, 105.93069139966208, 105.93069139966208, 107.17256885890959, 107.43069139966208, 106.50231365935912, 107.43069139966208, 107.43069139966208, 107.43069139966208, 108.27083979763906, 108.70607082630626, 108.83923552557626, 108.93069139966208, 109.98145025295044, 109.98145025295044, 110.25632377740313, 110.039365935919, 110.43069139966208, 111.25682967959462, 111.67341202923, 111.80789207419893, 111.93069139966208, 112.5322091062388, 112.5322091062388, 113.09050028105686, 113.57641821247887, 113.43069139966208, 113.80758853288297, 113.80758853288297, 114.50758853288373, 114.93069139966208, 115.34494435075881, 115.68296795952712, 115.68296795952712, 115.9246767847106, 116.43069139966208, 117.11347048903875, 117.34176503653747, 117.93069139966208, 118.05834738617123, 118.75885328836434, 118.88199662731869, 119.43069139966208, 120.425519955031, 120.83372681281533, 122.09218662169768, 120.96199662731868, 120.93069139966208, 122.33372681281533, 123.75885328836435, 123.04199662731868, 122.43069139966208, 123.93069139966208, 123.93372681281532, 123.93372681281532, 125.42551995503102, 125.12199662731868, 125.43069139966208, 125.43372681281532, 125.43372681281532, 126.93069139966208, 127.09218662169769, 127.20199662731868, 128.43069139966207, 128.75885328836435, 129.28199662731868, 129.93069139966207, 130.425519955031, 131.3337268128151, 132.09218662169766, 131.3619966273187, 131.43069139966207, 132.8337268128151, 132.8337268128151, 133.75885328836432, 133.4419966273187, 132.93069139966207, 134.3337268128151, 134.3337268128151, 135.42551995503098, 135.5219966273187, 135.8337268128151, 134.43069139966207, 135.8337268128151, 135.8337268128151, 137.09218662169764, 135.93069139966207, 137.3337268128151, 138.7588532883643, 137.60199662731873, 137.43069139966207, 138.8337268128151, 138.8337268128151, 139.68199662731874, 138.93069139966207, 140.42551995503095, 140.43069139966207, 141.76199662731875, 141.93069139966207, 142.0921866216976, 142.73372681281495, 142.93372681281494, 143.75885328836426, 143.84199662731876, 143.43069139966207, 144.43372681281494, 144.43372681281494, 145.42551995503092, 145.92199662731878, 144.93069139966207, 146.43069139966207, 147.09218662169758, 147.93069139966207, 148.0019966273188, 148.75885328836424, 149.43069139966207, 150.0819966273188, 150.4255199550309, 150.93069139966207, 151.43372681281463, 152.09218662169755, 152.1619966273188, 152.93372681281463, 152.43069139966207, 152.93372681281463, 152.93372681281463, 153.7588532883642, 153.93069139966207, 154.2091062394588, 154.2091062394588, 155.17594154019108, 154.24199662731883, 155.43069139966207, 155.48448566610298, 155.48448566610298, 156.59302979201794, 156.01052276559875, 156.75986509274716, 156.75986509274716, 158.0101180438448, 157.77904890387867, 156.93069139966207, 158.03524451939134, 158.03524451939134, 158.43069139966207, 159.31062394603552, 159.42720629567168, 159.5475750421586, 159.93069139966207, 160.5860033726797, 160.5860033726797, 160.84429454749855, 161.31610118043852, 161.43069139966207, 162.26138279932542, 162.46138279932384, 163.6784710511523, 163.08462731871845, 162.93069139966207, 163.73676222596802, 165.16462731871846, 164.43069139966207, 165.23676222596802, 165.23676222596802, 165.34513771781894, 165.93069139966207, 167.0118043844856, 167.24462731871847, 167.43069139966207, 168.67847105115226, 168.93069139966207, 169.32462731871848, 170.34513771781891, 170.43069139966207, 171.4046273187185, 171.43676222596775, 172.01180438448557, 171.93069139966207, 172.93676222596775, 172.93676222596775, 173.67847105115223, 173.4846273187185, 173.43069139966207, 174.43676222596775, 174.43676222596775, 175.3451377178189, 175.56462731871852, 174.93069139966207, 175.93676222596775, 175.93676222596775, 177.01180438448554, 176.43069139966207, 177.43676222596775, 177.43676222596775, 178.6784710511522, 177.64462731871853, 177.93069139966207, 179.43069139966207, 179.72462731871855, 180.34513771781886, 180.93069139966207, 181.80462731871856, 182.01180438448552, 182.43069139966207, 183.67847105115217, 183.88462731871857, 183.93069139966207, 184.53676222596744, 185.34513771781883, 185.96462731871858, 185.43069139966207, 186.03676222596744, 186.03676222596744]
#damage_order = [342.3590456926457, 1537.5139379166085, 717.242534, 179.439238, 699.3566770459237, 514.9070219043451, 461.1784058875584, 0.0, 179.439238, 347.63024710471046, 0, 313.85401193919427, 0.0, 347.63024710471046, 2760.104104643702, 1832.6241411315025, 691.1416953148283, 360.17110360000004, 1831.602810216085, 1424.3519756127869, 686.2475843080804, 2019.0613008815299, 528.5230730273028, 0, 7036.139850929025, 1944.4138531935246, 0, 382.54281562144365, 994.2201668206984, 360.17110360000004, 6991.726100461139, 1926.2857917780616, 688.5071049290806, 874.4892368341887, 1827.6228492295263, 1420.372014626228, 590.6248847941238, 528.5230730273028, 1496.6139670997998, 2270.632068341019, 944.405108359158, 360.17110360000004, 1455.7763834089167, 2170.5799882983556, 0, 722.2209502738973, 0.0, 595.6277834983498, 1750.2135939594189, 1074.3165802321378, 1401.0940602023138, 427.2161036, 0, 735.5049658636415, 0.0, 595.6277834983498, 471.2614303376825, 707.7779390775203, 3122.5214594496665, 0, 427.2161036, 3254.453461973314, 2154.325294504324, 715.6455436207223, 0.0, 595.6277834983498, 109.3443, 526.9752337815422, 796.8319468566783, 427.2161036, 0, 7946.269245437579, 5250.955235138553, 794.6504784439373, 595.6277834983498, 0, 1055.754042190827, 754.7651384025501, 1031.3793602923179, 360.17110360000004, 982.2874059170047, 698.3972526954988, 1091.5532208655418, 387.21487150710357, 347.6302471047104, 1896.7721568056616, 1434.696503735705, 1027.2306190625704, 656.8915745183535, 179.43923799999996, 347.6302471047104, 294.31252584796533, 1336.505807282322, 179.43923799999996, 489.84391321279566, 3349.568774847385, 1164.2763078534008, 502.4287700872901, 745.1603623186271, 347.6302471047104, 1935.04250868275, 1472.9668556127933, 480.75484991454965, 0.0, 179.43923799999996, 1376.8997220318365, 0, 533.8909122735262, 347.6302471047104, 1004.5624515665776, 1765.647130945425, 767.8830205642421, 179.43923799999996, 1778.9397576051513, 1316.8641045351947, 508.7211985245373, 705.8326845858321, 347.6302471047104, 107.94245, 547.8740865785201, 673.4965940055338, 179.43923799999996, 904.3247461435005, 620.4345929219944, 796.5082430301723, 347.6302471047104, 0, 333.8499511953354, 1259.5983486048563, 179.43923799999996, 4790.20275790372, 3658.1174078823274, 1077.570046560548, 1250.858864664235, 347.6302471047104, 179.43923799999996, 301.12932332164985, 726.8074460433228, 347.6302471047104, 4395.413864855856, 1331.9708223814137, 300.22041699182523, 0.0, 179.43923799999996, 4713.712409875697, 3581.627059854305, 536.687547134525, 347.6302471047104, 2397.50850085642, 694.6847450872366, 473.0641040468031, 705.8326845858321, 179.43923799999996, 4477.036756920001, 514.3144682465348, 579.9841158408876, 347.6302471047104, 4484.241365791628, 1368.226945212341, 508.7211985245373, 0, 1249.9064302724735, 179.43923799999996, 964.3436191437379, 1667.110991509468, 415.23510513771424, 347.6302471047104, 1146.780519773144, 826.2752579839303, 0, 3337.3514322809383, 0.0, 642.432183017479, 179.43923799999996, 1010.1312129789708, 1779.2905964057884, 92.52210000000001, 501.23162711342627, 1078.612545036299, 179.43923799999996, 347.6302471047104, 824.876940553431, 0, 313.530322171095, 0.0, 347.6302471047104, 4484.241365791628, 3352.1560157702356, 0, 354.07690140663016, 744.9666887856785, 246.48423799999992, 2877.8451102387335, 784.6688580684469, 1227.2565981682915, 0.0, 414.73495757575756, 2307.531008719527, 4098.3775216473105, 1165.7306312263188, 246.48423799999992, 0.0, 414.73495757575756, 3878.1297047567723, 3195.306371444139, 508.0553330814424, 817.3235297140417, 246.48423799999992, 1151.118109054639, 761.1563098827867, 631.107266965388, 414.73495757575756, 5692.929860667628, 1688.9209840620802, 409.3108171976777, 1444.1263095225427, 246.48423799999992, 1479.084245285027, 631.107266965388, 414.73495757575756, 179.43923799999996, 518.509420538033, 618.4378451796206, 4772.930743832877, 3640.8453938114835, 1024.4339842015715, 347.6302471047104, 647.2781421836703, 96.72764999999998, 817.483004487663, 179.43923799999996, 1011.3687155150582, 1782.3224776192026, 330.6687790409493, 0.0, 347.6302471047104, 179.43923799999996, 1785.9895592667206, 3243.5890701820717, 908.3736374701228, 487.7626342439499, 347.6302471047104, 0, 0, 457.6826123113098, 575.614373870577, 179.43923799999996, 889.4747157104521, 1483.6821780979174, 302.03822965147435, 465.60804245447525, 347.6302471047104, 1775.9184140359075, 1313.8427609659511, 546.4757691480206, 179.43923799999996, 735.5469299839439, 415.0339306810787, 347.6302471047104, 1493.8165182135028, 179.43923799999996, 487.74643706704654, 1768.8686123743382, 3201.642750295735, 943.3315732326073, 1352.2368783754403, 347.6302471047104, 3349.568774847385, 1164.2763078534008, 463.27588203330737, 761.7653818058074, 179.43923799999996, 2311.099886274119, 1615.5690108814288, 1052.400332811559, 347.6302471047104, 1949.142112005888, 1487.0664589359321, 504.52624623303916, 688.3537167045897, 179.43923799999996, 347.6302471047104, 383.23840631412105, 926.5517640666147, 312.81958997334624, 0.0, 1395.233268, 453.4876600198117, 1500.8081053659996, 179.43923799999996, 626.1897174950433, 441.7400623534648, 406.64402609808235, 1346.9931880110676, 179.43923799999996, 347.6302471047104, 1003.3249490304902, 1762.6152497320106, 482.1531673450491, 347.6302471047104, 1852.4591177900852, 0, 470.966627901054, 0, 379.52046639995626, 179.43923799999996, 4735.91928510964, 1470.9526265666314, 368.1591372771488, 1771.8486816, 272.17508416407577, 347.6302471047104, 2424.7954317771464, 705.8222679120229, 428.5191207274584, 677.3901187799636, 179.43923799999996, 0, 996.8699845048551, 347.70874485609534, 347.6302471047104, 4716.179840457246, 1462.8957103819807, 449.49388218494914, 525.3230982131558, 179.43923799999996, 995.2811825459221, 1742.9080218448191, 767.5459259029562, 347.6302471047104, 0.0, 1885.6938970517672, 1423.6182439818112, 443.9006124629516, 179.43923799999996, 1106.5788936462868, 947.9288744373766, 347.6302471047104, 0, 282.4967435602456, 705.8326845858321, 179.43923799999996, 947.5265255241054, 0, 440.2036444300676, 0.0, 347.6302471047104, 95.3258, 1527.708403401592, 1880.9774546197154, 360.17110360000004, 528.5230730273028, 3073.2691049473297, 2034.491545813666, 649.8913311150964, 2026.0528880340266, 360.17110360000004, 1653.3385962848809, 2487.0787517180493, 528.5230730273028, 663.1753467048406, 2195.598876482077, 360.17110360000004, 675.7602035793351, 933.497140157361, 528.5230730273028, 1508.1319593746011, 0, 623.3232999356082, 935.2450369454853, 360.17110360000004, 7891.530722045849, 5346.525702168372, 752.6676622568011, 1011.2785472288891, 528.5230730273028, 3100.3403433277535, 2061.5627841940914, 405.16014495814534, 2192.103082905828, 0, 427.2161036, 4746.556937000754, 1180.3655229930996, 491.07343375347045, 595.6277834983498, 3401.5597319423996, 749.904320667957, 775.8134879794845, 427.2161036, 1861.833023564881, 2706.829502066301, 2478.00905753472, 595.6277834983498, 546.9711730376832, 427.2161036, 812.953787743731, 414.73495757575756, 349.32299942925414, 0, 185.04420000000002, 592.653537626655, 854.9033106587126, 246.48423799999992, 6326.338043423712, 1871.2880733642112, 466.7716756095558, 664.7571100649127, 347.6302471047104, 179.43923799999996, 511.5178333855361, 347.6302471047104, 0.0, 289.31354103393005, 179.43923799999996, 404.8249316474553, 415.0339306810787, 347.6302471047104, 0, 483.55148477554843, 407.6652639281571, 0, 179.43923799999996, 5403.716400370858, 1688.0737993252646, 829.0718928449292, 347.6302471047104, 5030.640896440626, 1535.7980834353746, 457.1846280526957, 399.40279236486936, 179.43923799999996, 2096.185608976065, 1578.6608775377135, 511.71900784217166, 443.1439094876782, 1109.1709130897614, 1938.4741566301036, 436.9090253104547, 363.61460562802586, 347.6302471047104, 1073.134839238897, 755.1778676308102, 179.43923799999996, 2054.181720192, 450.1930409001988, 670.3985316274668, 347.6302471047104, 1012.8437156807205, 694.8867440726337, 416.63342256821363, 453.93717215434526, 179.43923799999996, 973.0985881863655, 0, 487.74643706704654, 386.6468050509633, 347.6302471047104, 215.8849, 0.0, 179.43923799999996, 4956.025795654582, 1505.3429402573965, 535.9883884192753, 347.6302471047104, 824.4745916401599, 0.0, 179.43923799999996, 466.7716756095558, 347.6302471047104, 0.0, 354.75479678130114, 179.43923799999996, 378.1258082088576, 0, 510.8186746702864, 347.6302471047104, 1084.915863382449, 1879.0492848471877, 312.9451056093696, 1427.396440264782, 179.43923799999996, 2160.479800129574, 1642.955068691223, 503.1279288025398, 0.0, 347.6302471047104, 2014.97189383479, 3668.7455478712754, 317.9440904234048, 179.43923799999996, 1128.5749528556116, 810.6179812475245, 523.4035315447809, 1399.4300916547945, 347.6302471047104, 179.43923799999996, 655.1436777302295, 501.7296113720404, 347.6302471047104, 388.91907087552477, 1083.1633162825458, 179.43923799999996, 348.39245247252893, 628.925225908366, 347.6302471047104, 96.72764999999998, 292.9491663532284, 620.1857419677448, 179.43923799999996, 1977.7489410617056, 1460.224209623355]
#status_order = ['Glance', 'Crit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Miss', 'DOT', 'DOT', 'Active', 'Glance', 'Miss', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'DOT', 'Active', 'Crit', 'Hit', 'Proc', 'Glance', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'DOT', 'Hit', 'Crit', 'Proc', 'Hit', 'Miss', 'DOT', 'Hit', 'Hit', 'Crit', 'DOT', 'Active', 'Hit', 'Miss', 'DOT', 'Glance', 'Glance', 'Hit', 'Dodge', 'DOT', 'Hit', 'Hit', 'Hit', 'Miss', 'DOT', 'Hit', 'Glance', 'Glance', 'DOT', 'Active', 'Crit', 'Crit', 'Hit', 'DOT', 'Dodge', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Crit', 'Glance', 'DOT', 'Hit', 'Hit', 'Crit', 'Hit', 'DOT', 'DOT', 'Glance', 'Crit', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Miss', 'DOT', 'Hit', 'Dodge', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Crit', 'DOT', 'Active', 'Glance', 'Crit', 'DOT', 'Crit', 'Crit', 'Crit', 'Crit', 'DOT', 'DOT', 'Glance', 'Hit', 'DOT', 'Crit', 'Hit', 'Glance', 'Miss', 'DOT', 'Crit', 'Crit', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Proc', 'Crit', 'DOT', 'Hit', 'Crit', 'Hit', 'DOT', 'Crit', 'Crit', 'Dodge', 'Crit', 'Dodge', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Crit', 'Active', 'Glance', 'Miss', 'DOT', 'Crit', 'Crit', 'Proc', 'Glance', 'Hit', 'DOT', 'Crit', 'Hit', 'Crit', 'Miss', 'DOT', 'Hit', 'Crit', 'Crit', 'DOT', 'Miss', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'Crit', 'Hit', 'Glance', 'Crit', 'DOT', 'Crit', 'Hit', 'DOT', 'DOT', 'Hit', 'Hit', 'Crit', 'Crit', 'Crit', 'DOT', 'Hit', 'Hit', 'Crit', 'DOT', 'Hit', 'Crit', 'Glance', 'Dodge', 'DOT', 'DOT', 'Hit', 'Crit', 'Crit', 'Glance', 'DOT', 'Active', 'Active', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Glance', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'DOT', 'Crit', 'DOT', 'Hit', 'Hit', 'Crit', 'Crit', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'Crit', 'Crit', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Glance', 'Crit', 'Glance', 'Dodge', 'Crit', 'Hit', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Hit', 'Crit', 'Hit', 'DOT', 'Hit', 'Dodge', 'Hit', 'Proc', 'Glance', 'DOT', 'Crit', 'Hit', 'Glance', 'Hit', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'Active', 'Crit', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Crit', 'DOT', 'Miss', 'Hit', 'Hit', 'Hit', 'DOT', 'Crit', 'Crit', 'DOT', 'Active', 'Glance', 'Hit', 'DOT', 'Crit', 'Active', 'Hit', 'Miss', 'DOT', 'Hit', 'Crit', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'DOT', 'Hit', 'Crit', 'DOT', 'Hit', 'Crit', 'DOT', 'Hit', 'Hit', 'DOT', 'Crit', 'Active', 'Hit', 'Hit', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Glance', 'Crit', 'Proc', 'DOT', 'Crit', 'Hit', 'Glance', 'DOT', 'Hit', 'Hit', 'Glance', 'DOT', 'Hit', 'Crit', 'Crit', 'DOT', 'Glance', 'DOT', 'Hit', 'DOT', 'Glance', 'Active', 'Crit', 'Hit', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'DOT', 'DOT', 'Hit', 'DOT', 'Miss', 'Glance', 'DOT', 'Glance', 'Hit', 'DOT', 'Active', 'Hit', 'Glance', 'Proc', 'DOT', 'Crit', 'Hit', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'DOT', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Crit', 'Hit', 'Glance', 'DOT', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Glance', 'DOT', 'Crit', 'Miss', 'Hit', 'Glance', 'DOT', 'Crit', 'Miss', 'DOT', 'Crit', 'Hit', 'Hit', 'DOT', 'Crit', 'Dodge', 'DOT', 'Hit', 'DOT', 'Miss', 'Glance', 'DOT', 'Glance', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Miss', 'DOT', 'Hit', 'Crit', 'Glance', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'DOT', 'Glance', 'Crit', 'DOT', 'Glance', 'Hit', 'DOT', 'Hit', 'Glance', 'Hit', 'DOT', 'Hit', 'Hit']
#total_dam = 127
#fight_length_input = 53
#num_sims = 300
#results_extra_sims = [7884, 7918, 7640, 7558, 8508, 8429, 7966, 7592, 8345, 7774, 8053, 7918, 8898, 8210, 7525, 7802, 8134, 7945, 7992, 7798, 7863, 7890, 8145, 8479, 8806, 8496, 7803, 8860, 8349, 8258, 8219, 8583, 7923, 7572, 8100, 8144, 8496, 8176, 8226, 7775, 7908, 7995, 7689, 7806, 8139, 7839, 8090, 8145, 7911, 7584, 8145, 8187, 7741, 7858, 8213, 8502, 7838, 8028, 8205, 7845, 7821, 8507, 7983, 7702, 8337, 8255, 8153, 7544, 7993, 8144, 8038, 7921, 8471, 8057, 8361, 8298, 8454, 8402, 8204, 7989, 8241, 8519, 8850, 8029, 8153, 8158, 8439, 7998, 8334, 8544, 7579, 8202, 8299, 7778, 7816, 8087, 7858, 7800, 8333, 8063, 8293, 7806, 7999, 8375, 7746, 8193, 7930, 7902, 7865, 8850, 8368, 8524, 7842, 7935, 7917, 8472, 7933, 8066, 8266, 8377, 8227, 8131, 8240, 8720, 7297, 7323, 7728, 8240, 7880, 8157, 8252, 8179, 8076, 8199, 8505, 8201, 7825, 8142, 7763, 8155, 8359, 7733, 8147, 8338, 8225, 8186, 7466, 7881, 7986, 7879, 7692, 8076, 7757, 7762, 7948, 8299, 8155, 7564, 7855, 8142, 7901, 8200, 8507, 8420, 8366, 8142, 7573, 8308, 8660, 7751, 8196, 8049, 7771, 8330, 8246, 7882, 8184, 8048, 8237, 8098, 8268, 9049, 7987, 8527, 8309, 8381, 8391, 8367, 8217, 8139, 7776, 8294, 8058, 8549, 8343, 7653, 8653, 8214, 8422, 8000, 8349, 8422, 7786, 8311, 8198, 8490, 7956, 8045, 7308, 7743, 7770, 7955, 8231, 8007, 7983, 7754, 8194, 7918, 8199, 8087, 8050, 8397, 7720, 8194, 7837, 8356, 8022, 8063, 8058, 8245, 7962, 8200, 8793, 7982, 8117, 7775, 8331, 8619, 8360, 8423, 8364, 7876, 7938, 8406, 7462, 8078, 8473, 8286, 7857, 8374, 8481, 8337, 8293, 7620, 8016, 7802, 8206, 8294, 8073, 8024, 8379, 8178, 8307, 7924, 7762, 8006, 8239, 8265, 8068, 8066, 7741, 7852, 8416, 7474, 7877, 7851, 7728, 8237, 8499, 7949, 7971, 7829, 7835, 8111, 8084, 8105, 8200, 7869, 8494, 7906, 7968, 7756, 8000, 8084, 7643, 7592, 8121, 7515, 8262, 8159]
# rune_0_tracker_i = [0, 1, 2, 5, 1]
# rune_1_tracker_i = [0, 1, 2, 5, 1]
# rune_2_tracker_i = [0, 1, 2, 5, 1]
# rune_3_tracker_i = [0, 1, 2, 5, 1]
# rune_4_tracker_i = [0, 1, 2, 5, 1]
# rune_5_tracker_i = [0, 1, 2, 5, 1]
# rune_6_tracker_i = [0, 1, 2, 5, 1]
# rune_7_tracker_i = [0, 1, 2, 5, 1]
# rune_8_tracker_i = [0, 1, 2, 5, 1]
# rune_9_tracker_i = [0, 1, 2, 5, 1]
# rune_10_tracker_i = [0, 1, 2, 5, 1]
# rune_11_tracker_i = [0, 1, 2, 5, 1]
#rune_time_tracker_i = [0, 1, 2, 5, 1]
#rune_power_tracker_i = [0, 1, 2, 5, 1]



dash_username = "Internal Testing"
t_damage = total_dam
fight_length = fight_length_input

rotation = ability_order
rotation_time = timeline_order
rotation_damage = damage_order
rotation_status = status_order


rune_0_tracker = rune_0_tracker_i
rune_1_tracker = rune_1_tracker_i
rune_2_tracker = rune_2_tracker_i
rune_3_tracker = rune_3_tracker_i
rune_4_tracker = rune_4_tracker_i
rune_5_tracker = rune_5_tracker_i
rune_6_tracker = rune_6_tracker_i
rune_7_tracker = rune_7_tracker_i
rune_8_tracker = rune_8_tracker_i
rune_9_tracker = rune_9_tracker_i
rune_10_tracker = rune_10_tracker_i
rune_11_tracker = rune_11_tracker_i
rune_time_tracker = rune_time_tracker_i
runic_power_tracker = rune_power_tracker_i

number_of_targets_in_fight = num_targ

#Unadded Stuff
#gear_currently_worn = "Conqueror's Darkruned Helmet*&*Might of the Leviathan*&*Valorous Darkruned Shoulderplates*&*Aged Winter Cloak*&*Conqueror's Darkruned Battleplate*&*Bracers of the Tyrant*&*Valorous Darkruned Gauntlets*&*Girdle of Razuvious*&*Legplates of the Violet Champion*&*Greaves of Iron Intensity*&*Ruthlessness*&*Greatring of Collision*&*Darkmoon Card: Greatness*&*Grim Toll*&*Sigil of Awareness*&*Serilas Blood Blade of Invar One-Arm*&*Serilas Blood Blade of Invar One-Arm"
current_gear_split_list = gear_currently_worn.replace("*&*",", ")
current_gear_split_list = current_gear_split_list.split(", ")



#extra_sim_stats_info = "479.156*^*14.61*^*24.62*^*530.0*^*1831.6748736*^*1495.6260000000002*^*22897.260000000002*^*15111.0*^*615.9780000000001*^*5564.18472192*^*157.0*^*78.5*^*32*^*257.5*^*7.18*^*181.0*^*False"
extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
extra_stats_split_list = extra_stats_split_list.split(", ")


extra_future_stats_info = results_extra_sims
# extra_future_stats_info = extra_future_stats_info.to_list() #database 1 (version 2)
# extra_future_stats_info = str(extra_future_stats_info)
# extra_future_stats_info = extra_future_stats_info[2:-2]
# extra_future_stats_info_loc = extra_future_stats_info.find("*") + 1
total_amount_of_simss = num_sims
# total_amount_of_simss = extra_future_stats_info[:extra_future_stats_info_loc-1]
# extra_future_stats_info = extra_future_stats_info[extra_future_stats_info_loc:]
# extra_future_stats_info = ast.literal_eval(extra_future_stats_info)
extra_all_dps_results = extra_future_stats_info




#extra_all_dps_results = []
#for i in extra_future_stats_info:
    #i = round(i)
    #extra_all_dps_results.append(i)
extra_all_dps_results_min = int(min(extra_all_dps_results))
extra_all_dps_results_max = int(max(extra_all_dps_results))
counts1, bins1 = np.histogram(extra_all_dps_results, bins=range(extra_all_dps_results_min, extra_all_dps_results_max, 50))
bins1 = 0.5 * (bins1[:-1] + bins1[1:])
fig_250_title = str("DPS Breakdown for All ") + str(total_amount_of_simss) + str(" Simulations")
fig250 = px.bar(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", color=counts1, color_continuous_scale="sunset")
fig250.update_layout(coloraxis_showscale=False)

data_251 = pd.DataFrame(dict(DPSValue=extra_all_dps_results))
fig251  = px.box(data_251, x="DPSValue", template="plotly_dark")
fig251.update_layout(xaxis=dict(
                        title=None,
                        showgrid=False, ),
                        yaxis=dict(
                        title=None,
                        showgrid=False,))
#fig251.update_traces(orientation='h') 
#fig250 = px.histogram(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", marginal="box")
#extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
#extra_stats_split_list = extra_stats_split_list.split(", ")


# extra_stats_split_list = extra_sim_stats_info.split("*^*")
# current_gear_split_list = gear_currently_worn.split("*&*")



e_stats_hit = extra_stats_split_list[0]
e_stats_hit_perc = extra_stats_split_list[1] + "%"
e_stats_crit = extra_stats_split_list[2] + "%"
e_stats_crit_rating = extra_stats_split_list[3]
e_stats_strength = extra_stats_split_list[4]
e_stats_stamina = extra_stats_split_list[5]
e_stats_hp = extra_stats_split_list[6]
e_stats_armor = extra_stats_split_list[7]
e_stats_agi = extra_stats_split_list[8]
e_stats_ap = extra_stats_split_list[9]
e_stats_armor_pen = extra_stats_split_list[10]
e_stats_armor_pen_perc = extra_stats_split_list[11] + "%"
e_stats_expertise = extra_stats_split_list[12]
e_stats_expertise_rating = extra_stats_split_list[13]
e_stats_expertise_dodge_parry_reduc = str(float(e_stats_expertise) * .25) + "%"
e_stats_haste = extra_stats_split_list[14] + "%"
e_stats_haste_rating = extra_stats_split_list[15]
c_g_head = current_gear_split_list[0]
c_g_neck = current_gear_split_list[1]
c_g_shoulders = current_gear_split_list[2]
c_g_back = current_gear_split_list[3]
c_g_chest = current_gear_split_list[4]
c_g_wrist = current_gear_split_list[5]
c_g_gloves = current_gear_split_list[6]
c_g_waist = current_gear_split_list[7]
c_g_legs = current_gear_split_list[8]
c_g_boots = current_gear_split_list[9]
c_g_ring1 = current_gear_split_list[10]
c_g_ring2 = current_gear_split_list[11]
c_g_trinket1 = current_gear_split_list[12]
c_g_trinket2 = current_gear_split_list[13]
c_g_sigil = current_gear_split_list[14]
c_g_mh = current_gear_split_list[15]
c_g_oh = current_gear_split_list[16]
c_g_2h = extra_stats_split_list[16]
#c_g_2h = ast.literal_eval(c_g_2h)



#Extra future stuff
#future_extra_sim_stats_info = dash_all_data["content_extra_future_stats_area"] #database 1 (version 2)
#future_extra_sim_stats_info = future_extra_sim_stats_info.to_string(index = False) #database 1 (version 2)



all_data = pd.DataFrame()
all_data2 = pd.DataFrame()
ability_order = rotation
timeline_order = rotation_time
damage_order = rotation_damage
status_order = rotation_status
timeline_order_data = []
timeline_order_data_end = []
for i in timeline_order:
    if i < 1:
        i = .000001
    i = round(i, 6)
    iz = i + 0.5
    if type(i) == int or i.is_integer() == True:
        i += .000001
    if type(iz) == int or iz.is_integer() == True:
        iz += .000001
    i = timedelta(seconds=i)
    iz = timedelta(seconds=iz)
    total = "1970-01-01 " + str(i)
    total_end = "1970-01-01 " + str(iz)
    finished_converted_time = datetime.strptime(total, '%Y-%m-%d %H:%M:%S.%f')
    finished_converted_time_end = datetime.strptime(total_end, '%Y-%m-%d %H:%M:%S.%f')
    timeline_order_data.append(finished_converted_time)
    timeline_order_data_end.append(finished_converted_time_end)
x = 0
for i in ability_order:
    if damage_order[x] == 0:
        damage_scale = 0
    elif damage_order[x] < 150:
        damage_scale = "Under 150"
    elif damage_order[x] < 300:
        damage_scale = "Under 300"
    elif damage_order[x] < 500:
        damage_scale = "Under 500"
    elif damage_order[x] < 750:
        damage_scale = "Under 750"
    elif damage_order[x] < 1000:
        damage_scale = "Under 1000"
    elif damage_order[x] < 2000:
        damage_scale = "Under 2000"
    elif damage_order[x] >= 2000:
        damage_scale = "Over 2000"
    data = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x]))
    all_data = pd.concat([all_data, data])
    data2 = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x], DamageScale=damage_scale))
    all_data2 = pd.concat([all_data2, data2])
    x += 1
unique_ability_df_table = []
unique_miss_count_df_table = []
unique_dodge_count_df_table = []
unique_parry_count_df_table = []
unique_glance_count_df_table = []
unique_block_count_df_table = []
unique_crit_count_df_table = []
unique_hit_count_df_table = []
unique_dot_count_df_table = []
unique_active_count_df_table = []
unique_proc_count_df_table = []
unique_damage_per_cast_df_table = []
unique_damage_df_table = []
for i in np.unique(np.array(ability_order)):
    search_data = all_data.loc[all_data['Ability'] == i]
    miss_search = search_data.loc[search_data['Status'] == "Miss"]
    dodge_search = search_data.loc[search_data['Status'] == "Dodge"]
    parry_search = search_data.loc[search_data['Status'] == "Parry"]
    glance_search = search_data.loc[search_data['Status'] == "Glance"]
    block_search = search_data.loc[search_data['Status'] == "Block"]
    crit_search = search_data.loc[search_data['Status'] == "Crit"]
    hit_search = search_data.loc[search_data['Status'] == "Hit"]
    dot_search = search_data.loc[search_data['Status'] == "DOT"]
    active_search = search_data.loc[search_data['Status'] == "Active"]
    proc_search = search_data.loc[search_data['Status'] == "Proc"]
    if miss_search.empty:
        unique_miss_count_df_table.append(0)
    else:
        unique_miss_count_df_table.append(len(miss_search.index))

    if dodge_search.empty:
        unique_dodge_count_df_table.append(0)
    else:
        unique_dodge_count_df_table.append(len(dodge_search.index))
    if parry_search.empty:
        unique_parry_count_df_table.append(0)
    else:
        unique_parry_count_df_table.append(len(parry_search.index))
    if glance_search.empty:
        unique_glance_count_df_table.append(0)
    else:
        unique_glance_count_df_table.append(len(glance_search.index))
    if block_search.empty:
        unique_block_count_df_table.append(0)
    else:
        unique_block_count_df_table.append(len(block_search.index))
    if crit_search.empty:
        unique_crit_count_df_table.append(0)
    else:
        unique_crit_count_df_table.append(len(crit_search.index))
    if hit_search.empty:
        unique_hit_count_df_table.append(0)
    else:
        unique_hit_count_df_table.append(len(hit_search.index))
    if dot_search.empty:
        unique_dot_count_df_table.append(0)
    else:
        unique_dot_count_df_table.append(len(dot_search.index))
    if active_search.empty:
        unique_active_count_df_table.append(0)
    else:
        unique_active_count_df_table.append(len(active_search.index))
    if proc_search.empty:
        unique_proc_count_df_table.append(0)
    else:
        unique_proc_count_df_table.append(len(proc_search.index))
    unique_damage_per_cast_df_table.append(round((sum(search_data['Damage'])) / len(search_data['Damage']), 4))
    unique_damage_df_table.append(round(sum(search_data['Damage']), 4))
    unique_ability_df_table.append(i)
status_table_data = pd.DataFrame(dict(Ability=unique_ability_df_table, Miss=unique_miss_count_df_table, Dodge=unique_dodge_count_df_table, Parry=unique_parry_count_df_table, Glance=unique_glance_count_df_table, Block=unique_block_count_df_table, Crit=unique_crit_count_df_table, Hit=unique_hit_count_df_table, DOT=unique_dot_count_df_table, Active=unique_active_count_df_table, Proc=unique_proc_count_df_table, Avg_Damage=unique_damage_per_cast_df_table, All_Damage=unique_damage_df_table))


statuss_sum_list = ["Miss", "Dodge", "Parry", "Glance", "Block", "Crit", "Hit", "DOT", "Active", "Proc"]
status_table_data['Sum'] = status_table_data[statuss_sum_list].sum(axis=1)
status_table_data['MissP'] = status_table_data["Miss"]/status_table_data["Sum"]
status_table_data['DodgeP'] = status_table_data["Dodge"]/status_table_data["Sum"]
status_table_data['ParryP'] = status_table_data["Parry"]/status_table_data["Sum"]
status_table_data['GlanceP'] = status_table_data["Glance"]/status_table_data["Sum"]
status_table_data['BlockP'] = status_table_data["Block"]/status_table_data["Sum"]
status_table_data['CritP'] = status_table_data["Crit"]/status_table_data["Sum"]
status_table_data['HitP'] = status_table_data["Hit"]/status_table_data["Sum"]
status_table_data['DOTP'] = status_table_data["DOT"]/status_table_data["Sum"]
status_table_data['ActiveP'] = status_table_data["Active"]/status_table_data["Sum"]
status_table_data['ProcP'] = status_table_data["Proc"]/status_table_data["Sum"]
status_table_data['MissP'] = status_table_data['MissP'].apply(lambda x: x * 100)
status_table_data['DodgeP'] = status_table_data['DodgeP'].apply(lambda x: x * 100)
status_table_data['ParryP'] = status_table_data['ParryP'].apply(lambda x: x * 100)
status_table_data['GlanceP'] = status_table_data['GlanceP'].apply(lambda x: x * 100)
status_table_data['BlockP'] = status_table_data['BlockP'].apply(lambda x: x * 100)
status_table_data['CritP'] = status_table_data['CritP'].apply(lambda x: x * 100)
status_table_data['HitP'] = status_table_data['HitP'].apply(lambda x: x * 100)
status_table_data['DOTP'] = status_table_data['DOTP'].apply(lambda x: x * 100)
status_table_data['ActiveP'] = status_table_data['ActiveP'].apply(lambda x: x * 100)
status_table_data['ProcP'] = status_table_data['ProcP'].apply(lambda x: x * 100)
status_table_data = status_table_data.round({'MissP': 2, 'DodgeP': 2, 'ParryP': 2, 'GlanceP': 2, 'BlockP': 2, 'CritP': 2, 'HitP': 2, 'DOTP': 2, 'ActiveP': 2, 'ProcP': 2})
status_table_data['MissP'] = status_table_data['MissP'].astype(str) + '%'
status_table_data['DodgeP'] = status_table_data['DodgeP'].astype(str) + '%'
status_table_data['ParryP'] = status_table_data['ParryP'].astype(str) + '%'
status_table_data['GlanceP'] = status_table_data['GlanceP'].astype(str) + '%'
status_table_data['BlockP'] = status_table_data['BlockP'].astype(str) + '%'
status_table_data['CritP'] = status_table_data['CritP'].astype(str) + '%'
status_table_data['HitP'] = status_table_data['HitP'].astype(str) + '%'
status_table_data['DOTP'] = status_table_data['DOTP'].astype(str) + '%'
status_table_data['ActiveP'] = status_table_data['ActiveP'].astype(str) + '%'
status_table_data['ProcP'] = status_table_data['ProcP'].astype(str) + '%'
status_table_data['DPSPA'] = status_table_data["All_Damage"].apply(lambda x: x / fight_length)
status_table_data = status_table_data.round({'DPSPA': 3})

dps_timeline_breaks = int(fight_length / 3)
time_each_break = fight_length / dps_timeline_breaks
time_breaks = []
timeline_dps_list = []
for times in range(0, dps_timeline_breaks):
    times += 1
    timeline_current_time = times * time_each_break
    time_breaks.append(times * time_each_break)
    timeline_dps_num = []
    for timeline_time_position, timeline_time in enumerate(timeline_order):
        if timeline_time < timeline_current_time:
            timeline_dps_num.append(timeline_time_position)
    timeline_damage_list = []
    for timeline_damage in timeline_dps_num:
        timeline_damage_list.append(damage_order[timeline_damage])
    timeline_damage = sum(timeline_damage_list)
    timeline_dps = timeline_damage / timeline_current_time
    timeline_dps_list.append(timeline_dps)
dps_table_data = pd.DataFrame(dict(DPS=timeline_dps_list, Time=time_breaks))

stats_columns_names = ["Hit", "Hit Percentage", "Crit", "Crit Rating", "Strength", "Stamina", "Health", "Armor", "Agility", "Attack Power", "Armor Penetration", "Armor Penetration Percentage", "Expertise", "Expertise Rating", "Dodge & Parry Reduction", "Haste", "Haste Rating"]
stats_columns_stats = [e_stats_hit, e_stats_hit_perc, e_stats_crit, e_stats_crit_rating, e_stats_strength, e_stats_stamina, e_stats_hp, e_stats_armor, e_stats_agi, e_stats_ap, e_stats_armor_pen, e_stats_armor_pen_perc, e_stats_expertise, e_stats_expertise_rating, e_stats_expertise_dodge_parry_reduc, e_stats_haste, e_stats_haste_rating]
stats_table_data = pd.DataFrame(dict(Names=stats_columns_names, Data=stats_columns_stats))
if c_g_2h == False:
    gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand", "Off hand"]
    gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh, c_g_oh]
    gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))
else:
    gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand"]
    gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh]
    gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))



colors = {'Main hand': '#45515E',
            'Off hand': '#576778',
            'Icy Touch': '#ACFDFC',
            'Obliterate': '#6AAEF7',
            'OH - Obliterate': '#55BDE0',
            'Frost Strike': '#2087f5',
            'OH - Frost Strike': '#12AADE',
            'Howling Blast': '#60FCFA',
            'Frost Fever': '#9AE3E2',
            'Blood Plague': '#E67F63',
            'Blood Strike': '#F2463D',
            'OH - Blood Strike': '#E6443A',
            'Blood Boil': '#FF3320',
            'Pestilence': '#D7F507',
            'Plague Strike': '#36C219',
            'OH - Plague Strike': '#2EA816',
            'Unbreakable Armor': '#F5A720',
            'Horn of Winter': '#CDD1C9',
            'Empowered Rune Weapon': '#7C9FC4',
            'Blood Tap': '#F54638',
            'Bloody Vengeance': '#DB7F8E',
            'Dancing Rune Weapon': '#FF3864',
            'Heart Strike': '#BC4B51',
            'Bone Shield': '#79B473',
            'Wandering Plague': '#98E02B',
            'Crypt Fever': '#8CB369',
            'Desolation': '#EFF7F6',
            'Scourge Strike': '#5C0029',
            'Blood-Caked Blades': '#91AEC1',
            'Necrosis': '#EAF2EF',
            'Death Coil': '#E2F89C',
            'Unholy Blight': '#0A8754',
            'Death and Decay': '#912F56',
            'Death Strike': '#A0A4B8',
            'Sudden Doom': '#D5E1A3',
            }
colors_status = {'Hit': '#39CCCC',
            'Crit': '#FFDC00',
            'DOT': '#01FF70',
            'Proc': '#723BFF',
            'Active': '#381D7F',
            'Miss': '#FF4136',
            'Dodge': '#85144b',
            'Parry': '#FF283E',
            'Glance': '#80201B',
            'Block': '#40100D',
            }
fig = px.timeline(all_data,x_start="Start", x_end="Finish", y="Ability", color="Ability",opacity=1, color_discrete_map=colors, hover_data=["Status", "Damage"], template="plotly_dark")
fig.update_layout(xaxis=dict(
                        title='Timeline',
                        linecolor = "#BCCCDC",
                        showgrid=False,
                        tickformat = '%H:%M:%S',
                                    ),
                        yaxis=dict(
                        title=None,
                        linecolor="#BCCCDC",
                        showgrid=False,
                        ))
t_dps = fight_length
#t_dps = round(max(timeline_order),0)
total_damage = round(sum(damage_order), 3)
total_damage = t_damage
total_dps = round((t_damage / t_dps), 3)
#t_damage = "Damage Status Map.                  Total Damage Done - " + str(t_damage) + "                  DPS - " + str(t_dps)
total_damage = "Total Damage Done - " + str(total_damage) + "                  DPS - " + str(total_dps) + "                  Fight Length - " + str(fight_length) + "                  Number of Targets - " + str(number_of_targets_in_fight)
fig.update_layout(
    hoverlabel=dict(
        font_size=12,
        font_family="Rockwell",
    )
)
all_data_no_zero = all_data.copy()
all_data_no_zero = all_data_no_zero[all_data_no_zero.Damage != 0]
fig2 = px.pie(all_data_no_zero, values='Damage', names='Ability', title='Damage by attack',color="Ability",color_discrete_map=colors, template="plotly_dark")
fig3 = px.treemap(all_data, path=[px.Constant("All Damage"),'Ability', 'Status'], values='Damage',title=total_damage ,color="Ability",color_discrete_map=colors, template="plotly_dark")
fig4 = px.pie(all_data, names='Status', title='Status Percentage',color="Status",color_discrete_map=colors_status, template="plotly_dark")
fig5 = px.parallel_categories(all_data2, dimensions=['Ability', 'Status', 'DamageScale'],labels={'Ability':'Ability Name', 'Status':'Damage Status', 'DamageScale':'Damage Sclae'},color="Damage", color_continuous_scale=px.colors.sequential.Plotly3,range_color=(0,2000), template="plotly_dark")
fig601 = px.line(dps_table_data, x='Time', y="DPS", template="plotly_dark")
fig602 = px.scatter(dps_table_data,x='Time', y='DPS',color='DPS',template="plotly_dark")
fig6 = go.Figure(data=fig601.data + fig602.data)
rune_time_loop_num = 0
for rune_time in rune_time_tracker:
    rune_0_tracker[rune_time_loop_num] -= rune_time
    if rune_0_tracker[rune_time_loop_num] < 0:
        rune_0_tracker[rune_time_loop_num] = 0
    rune_1_tracker[rune_time_loop_num] -= rune_time
    if rune_1_tracker[rune_time_loop_num] < 0:
        rune_1_tracker[rune_time_loop_num] = 0
    rune_2_tracker[rune_time_loop_num] -= rune_time
    if rune_2_tracker[rune_time_loop_num] < 0:
        rune_2_tracker[rune_time_loop_num] = 0
    rune_3_tracker[rune_time_loop_num] -= rune_time
    if rune_3_tracker[rune_time_loop_num] < 0:
        rune_3_tracker[rune_time_loop_num] = 0
    rune_4_tracker[rune_time_loop_num] -= rune_time
    if rune_4_tracker[rune_time_loop_num] < 0:
        rune_4_tracker[rune_time_loop_num] = 0
    rune_5_tracker[rune_time_loop_num] -= rune_time
    if rune_5_tracker[rune_time_loop_num] < 0:
        rune_5_tracker[rune_time_loop_num] = 0
    rune_6_tracker[rune_time_loop_num] -= rune_time
    if rune_6_tracker[rune_time_loop_num] < 0:
        rune_6_tracker[rune_time_loop_num] = 0
    rune_7_tracker[rune_time_loop_num] -= rune_time
    if rune_7_tracker[rune_time_loop_num] < 0:
        rune_7_tracker[rune_time_loop_num] = 0
    rune_8_tracker[rune_time_loop_num] -= rune_time
    if rune_8_tracker[rune_time_loop_num] < 0:
        rune_8_tracker[rune_time_loop_num] = 0
    rune_9_tracker[rune_time_loop_num] -= rune_time
    if rune_9_tracker[rune_time_loop_num] < 0:
        rune_9_tracker[rune_time_loop_num] = 0
    rune_10_tracker[rune_time_loop_num] -= rune_time
    if rune_10_tracker[rune_time_loop_num] < 0:
        rune_10_tracker[rune_time_loop_num] = 0
    rune_11_tracker[rune_time_loop_num] -= rune_time
    if rune_11_tracker[rune_time_loop_num] < 0:
        rune_11_tracker[rune_time_loop_num] = 0
    rune_time_loop_num += 1

rune_table_data = pd.DataFrame(dict(Rune0=rune_0_tracker,
Rune1=rune_1_tracker,
Rune2=rune_2_tracker,
Rune3=rune_3_tracker,
Rune4=rune_4_tracker,
Rune5=rune_5_tracker,
Rune6=rune_6_tracker,
Rune7=rune_7_tracker,
Rune8=rune_8_tracker,
Rune9=rune_9_tracker,
Rune10=rune_10_tracker,
Rune11=rune_11_tracker,
RuneTime=rune_time_tracker))
runic_power_data = pd.DataFrame(dict(Runicpower=runic_power_tracker, Time=rune_time_tracker))
fig7 = go.Figure()
# fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["RuneTime"], mode="lines", name="Time", line_color='#ffffff'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune0"], mode="lines", name="Blood1", line_color='#FF4136'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune1"], mode="lines", name="Blood2", line_color='#FF4136'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune2"], mode="lines", name="Frost1", line_color='#39CCCC'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune3"], mode="lines", name="Frost2", line_color='#39CCCC'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune4"], mode="lines", name="Unholy1", line_color='#2ECC40'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune5"], mode="lines", name="Unholy2", line_color='#2ECC40'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune6"], mode="lines", name="Death_Blood1", line_color='#80201B'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune7"], mode="lines", name="Death_Blood2", line_color='#80201B'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune8"], mode="lines", name="Death_Frost1", line_color='#154D4D'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune9"], mode="lines", name="Death_Frost2", line_color='#154D4D'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune10"], mode="lines", name="Death_Unholy1", line_color='#124D18'))
fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune11"], mode="lines", name="Death_Unholy2", line_color='#124D18'))
fig7.update_layout(yaxis_range=[0, 10])
# fig7.update_layout(yaxis_range=[0,int(fight_length+1)])
fig7.update_layout(title="Rune Usage Cooldowns", template="plotly_dark")
fig7.update_traces(mode="lines", hovertemplate=None)
fig7.update_layout(hovermode="x")
fig7.update_layout(xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
            )
fig8 = px.line(runic_power_data, x="Time", y="Runicpower", title='Runic Power Usage', template="plotly_dark")
fig8.update_layout(xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
            )
fig2.update_layout(
    hoverlabel=dict(
        font_size=12,
        font_family="Rockwell",
    )
)
fig3.update_layout(
    hoverlabel=dict(
        font_size=12,
        font_family="Rockwell",
    )
)
fig4.update_layout(
    hoverlabel=dict(
        font_size=12,
        font_family="Rockwell",
    )
)
fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig6.update_layout(title="Damage Over Time", template="plotly_dark")
fig6.update_traces(line_color='#ffffff', line_width=1)
fig6.update_layout(xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
            )


last_sim_title = str(dash_username) + "'s Last Simulation"

#Stylesheet Pulled from currently active dash style sheet on website
external_stylesheets = ['https://www.remourtech.com/dash/assets/css/dash_css.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__)
app.layout = html.Div(children=[
        html.Div([
            html.H1(children=last_sim_title, style={'color': '#ffffff'}),
            dcc.Graph(
                id='graph1',
                figure=fig
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph250',
                figure=fig250
            ),
        ]),
         html.Div([
            dcc.Graph(
                id='graph251',
                figure=fig251
            ),
        ]),
        html.Div(children=[
            dcc.Graph(id="graph2",figure=fig2, style={'display': 'inline-block'}),
            dcc.Graph(id="graph4",figure=fig4, style={'display': 'inline-block'})
        ]),
        html.Div([
            dash_table.DataTable(id='table',
                #columns=[{"name": i, "id": i} for i in status_table_data.columns],
                columns=[{"name": "Ability", "id":"Ability"},{"name": "Miss", "id":"Miss"},
                      {"name": "Dodge", "id":"Dodge"},{"name": "Parry", "id":"Parry"},
                      {"name": "Glance", "id":"Glance"},{"name": "Block", "id":"Block"},
                      {"name": "Crit", "id":"Crit"},{"name": "Hit", "id":"Hit"},
                      {"name": "DOT", "id":"DOT"},{"name": "Active", "id":"Active"},
                      {"name": "Proc", "id":"Proc"},{"name": "Average Damage", "id":"Avg_Damage"},
                      {"name": "Total Damage", "id":"All_Damage"},
                      {"name": "Average DPS", "id":"DPSPA"},
                      


                    #  {"name": "Sum - DELETE", "id":"Sum"},{"name": "MissPercentage - DELETE", "id":"MissP"},
                         ],
                data=status_table_data.to_dict('records'),
                tooltip_data=[{
                    'Miss': {'value': '{}'.format(str(row['MissP']) + " Miss Rate"), 'type': 'markdown'},
                    'Dodge': {'value': '{}'.format(str(row['DodgeP']) + " Dodge Rate"), 'type': 'markdown'},
                    'Parry': {'value': '{}'.format(str(row['ParryP']) + " Parry Rate"), 'type': 'markdown'},
                    'Glance': {'value': '{}'.format(str(row['GlanceP']) + " Glance Rate"), 'type': 'markdown'},
                    'Block': {'value': '{}'.format(str(row['BlockP']) + " Block Rate"), 'type': 'markdown'},
                    'Crit': {'value': '{}'.format(str(row['CritP']) + " Crit Rate"), 'type': 'markdown'},
                    'Hit': {'value': '{}'.format(str(row['HitP']) + " Hit Rate"), 'type': 'markdown'},
                    'DOT': {'value': '{}'.format(str(row['DOTP']) + " DOT Rate"), 'type': 'markdown'},
                    'Active': {'value': '{}'.format(str(row['ActiveP']) + " Active Rate"), 'type': 'markdown'},
                    'Proc': {'value': '{}'.format(str(row['ProcP']) + " Proc Rate"), 'type': 'markdown'},
                    'Avg_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'All_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'DPSPA': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                 } for row in status_table_data.to_dict('records')],
                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: grey !important; font-family: monospace; color: white !important; textAlign: center'
                }],
                tooltip_delay=0,
                tooltip_duration=None,
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },
            {
            "if": {"state": "selected"},
            # "backgroundColor": "#94E66C",
            "backgroundColor": "inherit !important",
            "border": "inherit !important",
            # 'fontWeight': 'bold'
            },
            {
                'if': {
                    'filter_query': '{Miss} > 0',
                    'column_id': 'Miss'
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            },
            {
                'if': {
                    'column_id': 'Dodge',
                    'filter_query': '{Dodge} > 0'
                },
                'backgroundColor': '#85144b',
            },
            {
                'if': {
                    'column_id': 'Parry',
                    'filter_query': '{Parry} > 0'
                },
                'backgroundColor': '#FF283E',
            },
            {
                'if': {
                    'column_id': 'Glance',
                    'filter_query': '{Glance} > 0'
                },
                'backgroundColor': '#80201B',
            },
            {
                'if': {
                    'column_id': 'Block',
                    'filter_query': '{Block} > 0'
                },
                'backgroundColor': '#40100D',
            },
            {
                'if': {
                    'column_id': 'Crit',
                    'filter_query': '{Crit} > 0'
                },
                'backgroundColor': '#FFDC00',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Hit',
                    'filter_query': '{Hit} > 0'
                },
                'backgroundColor': '#39CCCC',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'DOT',
                    'filter_query': '{DOT} > 0'
                },
                'backgroundColor': '#01FF70',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Active',
                    'filter_query': '{Active} > 0'
                },
                'backgroundColor': '#381D7F',
            },
            {
                'if': {
                    'column_id': 'Proc',
                    'filter_query': '{Proc} > 0'
                },
                'backgroundColor': '#723BFF',
            }
        ],
                style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
            )
        ]),
        html.Div([

            dcc.Graph(
                id='graph6',
                figure=fig6
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph5',
                figure=fig5
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph7',
                figure=fig7
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph8',
                figure=fig8
            ),
        ]),
        html.Div(children=[
    html.Div(children=[
    html.Div([
            dash_table.DataTable(id='table2',
                columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                          ],
                data=stats_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'right'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'right'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'left', 'padding-left': '250px'}),
    html.Div([
            dash_table.DataTable(id='table3',
                #columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                #          ],
                columns=[{"name": "D", "id":"Data"},{"name": "N", "id":"Names"},
                          ],
                data=gear_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'left'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'left'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'right', 'padding-right': '250px'}),
    ])
        ]),
        html.Div(
        [   html.H1(
            html.I("Buff'd Stats & Gear", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
        html.Div(
        [   html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
            html.H1(
            html.I("", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
    


#fig.show()
