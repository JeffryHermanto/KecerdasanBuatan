#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UAS Kecerdasan Buatan - Institut Teknologi Indonesia
Dosen: Ir, Mega Bagus Herlambang S.T., M.T., Ph.D., IPM, ASEAN Eng

Program Python untuk Mendeteksi Wajah Sendiri
Menggunakan Metode Deteksi Objek Haar Cascades

Created on Wed Jul 16 16:35:03 2025
Author: Jeffry Hermanto - 1152523002
"""

import cv2
import matplotlib.pyplot as plt
from typing import Tuple, List

# ==========================
# Configuration
# ==========================

BASE_PATH = "/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan"
IMG_PATH = f"{BASE_PATH}/jeffry.jpeg"
FACE_CASCADE_PATH = f"{BASE_PATH}/haarcascades/haarcascade_frontalface_alt.xml"
EYE_CASCADE_PATH = f"{BASE_PATH}/haarcascades/haarcascade_eye.xml"

# ==========================
# Load Resources
# ==========================

image = cv2.imread(IMG_PATH)

face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)

# ==========================
# Utility Functions
# ==========================

def draw_boxes(image: cv2.Mat, boxes: List[Tuple[int, int, int, int]], color: Tuple[int, int, int], thickness: int = 2) -> cv2.Mat:
    """Draw rectangles around detected regions."""
    for (x, y, w, h) in boxes:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)
    return image

def detect_features(image: cv2.Mat, cascade: cv2.CascadeClassifier, scale: float = 1.2, neighbors: int = 5) -> List[Tuple[int, int, int, int]]:
    """Generic feature detection using a Haar cascade."""
    return cascade.detectMultiScale(image.copy(), scaleFactor=scale, minNeighbors=neighbors)

def show_image(title: str, image_bgr: cv2.Mat) -> None:
    """Display an image using matplotlib."""
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

# ==========================
# Detection Functions
# ==========================

def detect_faces(image: cv2.Mat) -> cv2.Mat:
    faces = detect_features(image, face_cascade)
    return draw_boxes(image.copy(), faces, color=(255, 255, 255), thickness=10)

def detect_eyes(image: cv2.Mat) -> cv2.Mat:
    eyes = detect_features(image, eye_cascade)
    return draw_boxes(image.copy(), eyes, color=(255, 255, 255), thickness=10)

def detect_all(image: cv2.Mat) -> cv2.Mat:
    image_copy = image.copy()
    faces = detect_features(image_copy, face_cascade)
    eyes = detect_features(image_copy, eye_cascade)

    draw_boxes(image_copy, faces, color=(255, 255, 255), thickness=4)
    draw_boxes(image_copy, eyes, color=(0, 255, 0), thickness=2)

    return image_copy

# ==========================
# Static Image Testing
# ==========================

show_image("Original", image)
show_image("Face Detection", detect_faces(image))
show_image("Eye Detection", detect_eyes(image))
show_image("Face and Eye Detection", detect_all(image))

# ==========================
# Real-Time Video Detection
# ==========================

def detect_all_video() -> None:
    """Real-time face and eye detection using webcam."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press ESC to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_frame = detect_all(frame)
        cv2.imshow('Real-Time Face and Eye Detection', detected_frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

# Uncomment to run real-time detection
# detect_all_video()
