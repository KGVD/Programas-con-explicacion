# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:55:04 2023

@author: LoboM
"""

"""En este código utilizamos la biblioteca DeepFace para realizar el seguimiento de caras en 
tiempo real utilizando una base de datos de caras almacenada en la ubicación"""

from deepface import DeepFace

DeepFace.stream(db_path= "./Deepbase")