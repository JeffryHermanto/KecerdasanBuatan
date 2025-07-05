import cv2
import numpy as np

'''
Menggambar lingkaran dengan klik kiri mouse
'''

# Menyiapkan kanvas
canvas = np.zeros(shape=(1000, 1000, 3))


# Fungsi buat circle
def buat_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas, center=(x,y), radius=100,
                   color=(0,255,0), thickness=-1)
        
# namedWindow and Callback

# Memberi nama window gambar yang direferensikan
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_circle di gambarku
cv2.setMouseCallback('gambarku', buat_circle)

# Menggunakan while loop
while True:
    cv2.imshow('gambarku', canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


'''
Menggambar lingkaran dengan klik kiri dan klik kanan di mouse
'''

# Menyiapkan kanvas
canvas = np.zeros(shape=(1000, 1000, 3))


# Fungsi buat circle
def buat_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas, center=(x,y), radius=100,
                   color=(0,255,0), thickness=-1)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(canvas, center=(x,y), radius=100,
                   color=(255,0,0), thickness=-1)
        
# namedWindow and Callback

# Memberi nama window gambar yang direferensikan
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_circle di gambarku
cv2.setMouseCallback('gambarku', buat_circle)

# Menggunakan while loop
while True:
    cv2.imshow('gambarku', canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


'''
Menggambar rectangle dengan drag mouse (tahan klik kiri sampai dilepaskan klik kirinya)
'''

# Menyiapkan kanvas
canvas = np.zeros(shape=(1000, 1000, 3))

# Membuat variabel penentu apakah klik kiri masih ditahan dan penentu posisi awal
tahan = False
ix, iy = -1, -1

# Fungsi buat rectangle
def buat_rectangle(event, x, y, flags, param):
    global ix, iy, tahan
    
    if event == cv2.EVENT_LBUTTONDOWN:
        tahan = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if tahan == True:
            cv2.rectangle(canvas, pt1=(ix, iy), pt2=(x, y), 
                          color=(255, 0, 0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        tahan = False
        cv2.rectangle(canvas, pt1=(ix, iy), pt2=(x, y), 
                      color=(255, 0, 0), thickness=-1)
        
# namedWindow and Callback

# Memberi nama window gambar yang direferensikan
cv2.namedWindow(winname='gambarku')

# Menghubungkan mouse kita dengan fungsi buat_circle di gambarku
cv2.setMouseCallback('gambarku', buat_rectangle)

# Menggunakan while loop
while True:
    cv2.imshow('gambarku', canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
