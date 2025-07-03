import cv2

gambar = cv2.imread('/Users/jeffryhermanto/Documents/Learnings/ITI/Kecerdasan Buatan/ayam.jpg')

while True:
    cv2.imshow('Ayam', gambar)
    
    # Jika kita tunggu sampai 1ms dan kita menekan tombol ESCAPE, maka Break
    # 0xFF adalah hexadecimal dari 11111111 (keterangan tombol keyboard), 27 adalah kode untuk tombol escape
    if cv2.waitKey(1) & 0xff == 27:
        break
    
cv2.destroyAllWindows()