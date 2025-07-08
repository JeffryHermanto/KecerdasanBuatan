import cv2
import matplotlib.pyplot as plt

img_path = '/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/ayam.jpg'

gambar = cv2.imread(img_path)
type(gambar)

# Mengeluarkan gambar
plt.imshow(gambar)

# Konversi ke RGB
gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_RGB2BGR)
plt.imshow(gambar_rgb)

# Merubah gambar ke grayscale
gambar_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(gambar_gray)
plt.imshow(gambar_gray, cmap='gray')

# Mengecilkan gambar
# format penulisannya adalah (sumbu x, sumbu y) --> kolom, baris
gambar_baru = cv2.resize(gambar_rgb, (700,500))
plt.imshow(gambar_baru)

# Mengecilkan gambar sesuai proporsi
rasio_baris = 0.5
rasio_kolom = 0.5
gambar_baru2 = cv2.resize(gambar_rgb, (0,0), gambar_rgb, rasio_kolom, rasio_baris)
plt.imshow(gambar_baru2)
rasio_baris2 = 0.76
rasio_kolom2 = 0.86
gambar_baru3 = cv2.resize(gambar_rgb, (0,0), gambar_rgb, rasio_kolom2, rasio_baris2)
plt.imshow(gambar_baru3)

# Membalik gambar
gambar_terbalik = cv2.flip(gambar_rgb, 0) # nilai 0 membalik gambar sesuai sumbu x
plt.imshow(gambar_terbalik)
gambar_terbalik1 = cv2.flip(gambar_rgb, 1) # nilai 1 membalik gambar sesuai sumbu y
plt.imshow(gambar_terbalik1)
gambar_terbalik2 = cv2.flip(gambar_rgb, -1) # nilai -1 membalik gambar sesuai sumbu X dan y sekaligus
plt.imshow(gambar_terbalik2)

# Menyimpan file
# cv2.imwrite('gambar_simpan.jpg', gambar_rgb) # jika filenya RGB hasilnya justru BGR
# cv2.imwrite('gambar_simpan2.jpg', gambar) # jika filenya adalah BGR maka yang disimpan adalah RGB

# Memunculkan gambar langsung dari OpenCV
cv2.imshow('Ayam', gambar)
cv2.waitKey() # menunggu respon dari keyboard
