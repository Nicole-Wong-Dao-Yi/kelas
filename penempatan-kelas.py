#atur cara menentukan penempatan kelas

nama=str (input("masukkan nama anda:"))
markah=float(input("masukkan markah anda:"))

#kategori kelas
if markah<=40:
    print("anda ditempatkan di kelas dedikasi")
elif markah<=60:
    print("anda ditempatkan di kelas cerdik")
elif markah<=80:
    print("anda ditempatkan di kelas bijak")
elif markah >80:
    print("anda ditempatkan di kelas amanah")   
