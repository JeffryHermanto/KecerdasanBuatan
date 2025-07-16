#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Face and Eye Detection using Haar Cascades

Created on Wed Jul 16 16:35:03 2025
Author: Jeffry Hermanto
"""

import cv2
import matplotlib.pyplot as plt

# Paths to resources
IMG_PATH = '/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/jeffry.jpeg'
FACE_CASCADE_PATH = '/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/haarcascades/haarcascade_frontalface_alt.xml'
EYE_CASCADE_PATH = '/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/haarcascades/haarcascade_eye.xml'

# Load image
image = cv2.imread(IMG_PATH)

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)

def detect_faces(image):
    """Detect faces using Haar cascade."""
    image_copy = image.copy()
    face_boxes = face_cascade.detectMultiScale(image_copy, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in face_boxes:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 10)
    
    return image_copy

def detect_eyes(image):
    """Detect eyes using Haar cascade."""
    image_copy = image.copy()
    eye_boxes = eye_cascade.detectMultiScale(image_copy, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in eye_boxes:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 10)
    
    return image_copy

def detect_all(image):
    """Detect both faces and eyes."""
    image_copy = image.copy()
    
    face_boxes = face_cascade.detectMultiScale(image_copy, scaleFactor=1.2, minNeighbors=5)
    eye_boxes = eye_cascade.detectMultiScale(image_copy, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in face_boxes:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 4)
    
    for (x, y, w, h) in eye_boxes:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image_copy

def show_image(title, image_bgr):
    """Utility function to show an image with matplotlib."""
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Static image detections
show_image("Original", image)
show_image("Face Detection", detect_faces(image))
show_image("Eye Detection", detect_eyes(image))
show_image("Face and Eye Detection", detect_all(image))

def detect_all_video():
    """Real-time face and eye detection from webcam."""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Press ESC to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = detect_all(frame)
        cv2.imshow('Real-Time Face and Eye Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

# Uncomment to run real-time detection
# detect_all_video()
