# Mengimpor library
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Menyiapkan gambar
gambar = Image.open('/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/ayam.jpg')
type(gambar)

# Merubah gambar menjadi array
gambar_ar = np.asarray(gambar)
type(gambar_ar)

# Memunculkan gambar
plt.imshow(gambar_ar)

# Memunculkan gambar 1 channel
# RGB - Red, Green, Blue
plt.imshow(gambar_ar[:,:,0])
gambar_ar[:,:,0].shape
gambar_ar.shape
plt.imshow(gambar_ar[:,:,0], cmap='viridis')
plt.imshow(gambar_ar[:,:,0], cmap=None)
plt.imshow(gambar_ar[:,:,0], cmap='gray')
plt.imshow(gambar_ar[:,:,0]) # Red
plt.imshow(gambar_ar[:,:,1]) # Green
plt.imshow(gambar_ar[:,:,2]) # Blue
plt.imshow(gambar_ar)

# Menyisakan channel Green
gambar_hijau = gambar_ar.copy()
gambar_hijau[:,:,0] = 0
gambar_hijau[:,:,2] = 0
plt.imshow(gambar_hijau)

# Menyisakan channel Red
gambar_merah = gambar_ar.copy()
gambar_merah[:,:,1] = 0
gambar_merah[:,:,2] = 0
plt.imshow(gambar_merah)

# Menyisakan channel Blue
gambar_biru = gambar_ar.copy()
gambar_biru[:,:,0] = 0
gambar_biru[:,:,1] = 0
plt.imshow(gambar_biru)

# Memulai OpenCV --> bahasa C++
import cv2

# Membuka file dengan OpenCV
ayam = cv2.imread('/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/ayam.jpg')
# Pillow RGB - Red Green Blue
# OpenCV BGR - Blue Green Red
type(ayam)

# Konversi ke RGB
ayam_rgb = cv2.cvtColor(ayam, cv2.COLOR_BGR2RGB)
plt.imshow(ayam_rgb)

ayam_rgb == gambar_ar