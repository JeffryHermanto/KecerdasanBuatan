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

# ==========================
# Konfigurasi
# ==========================

BASE_PATH = "/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan"
IMG_PATH = f"{BASE_PATH}/jeffry.jpeg"
FACE_CASCADE_PATH = f"{BASE_PATH}/haarcascades/haarcascade_frontalface_alt.xml"
EYE_CASCADE_PATH = f"{BASE_PATH}/haarcascades/haarcascade_eye.xml"

# ==========================
# Memuat Sumber Daya
# ==========================

image = cv2.imread(IMG_PATH)

face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)

# ==========================
# Fungsi Utilitas
# ==========================

def draw_boxes(image, boxes, color, thickness: int = 2):
    """Menggambar kotak persegi panjang di sekitar area yang terdeteksi."""
    for (x, y, w, h) in boxes:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)
    return image

def detect_features(image, cascade, scale: float = 1.2, neighbors: int = 5):
    """Deteksi fitur secara umum menggunakan Haar cascade."""
    return cascade.detectMultiScale(image.copy(), scaleFactor=scale, minNeighbors=neighbors)

def show_image(title, image_bgr):
    """Menampilkan gambar menggunakan matplotlib."""
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

# ==========================
# Fungsi Deteksi
# ==========================

def detect_faces(image):
    faces = detect_features(image, face_cascade)
    return draw_boxes(image.copy(), faces, color=(255, 255, 255), thickness=10)

def detect_eyes(image):
    eyes = detect_features(image, eye_cascade)
    return draw_boxes(image.copy(), eyes, color=(255, 255, 255), thickness=10)

def detect_all(image):
    image_copy = image.copy()
    faces = detect_features(image_copy, face_cascade)
    eyes = detect_features(image_copy, eye_cascade)

    draw_boxes(image_copy, faces, color=(255, 255, 255), thickness=4)
    draw_boxes(image_copy, eyes, color=(0, 255, 0), thickness=2)

    return image_copy

# ==========================
# Pengujian Gambar Statis
# ==========================

show_image("Asli", image)
show_image("Deteksi Wajah", detect_faces(image))
show_image("Deteksi Mata", detect_eyes(image))
show_image("Deteksi Wajah dan Mata", detect_all(image))

# ==========================
# Deteksi Video Real-Time
# ==========================

def detect_all_video():
    """Deteksi wajah dan mata secara real-time menggunakan webcam."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kesalahan: Tidak dapat membuka webcam.")
        return

    print("Tekan ESC untuk keluar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_frame = detect_all(frame)
        cv2.imshow('Deteksi Wajah dan Mata Real-Time', detected_frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

# Hapus komentar untuk menjalankan deteksi real-time
# detect_all_video()
