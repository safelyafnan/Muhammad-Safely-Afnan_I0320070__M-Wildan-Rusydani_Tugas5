BOLD = '\033[1m'
END = '\033[0m'
print(BOLD + "Selamat datang di Hotel Sebelas")
print("Silakan mengisi identitas diri anda!" + END)

nama=input("Masukan nama anda: ")
jenis_kelamin=input('Jenis Kelamin(L/P): ')

if jenis_kelamin == 'L':
    print(" ")
    print("Selamat datang Tuan {}". format(nama))
    print('Selamat menikmati fasilitas hotel kami')

elif jenis_kelamin == 'P':
    print(" ")
    print("Selamat datang Nyonya {}".format(nama))
    print('Selamat menikmati fasilitas hotel kami')

else:
    print(" ")
    print("Harap mengisi jenis kelamin dengan format L/P")
    print("Terima kasih")
