nama = str(input('Masukkan Nama: '))
angka = int(input('Masukkan Nilai: '))

if angka < 60:
    print('Halo, {}! Nilai anda setelah dikonversi adalah E'.format(nama))
elif angka < 65:
    print('Halo, {}! Nilai anda setelah dikonversi adalah C'.format(nama))
elif angka < 70:
    print('Halo, {}! Nilai anda setelah dikonversi adalah C+'.format(nama))
elif angka < 75:
    print('Halo, {}! Nilai anda setelah dikonversi adalah B'.format(nama))
elif angka < 80:
    print('Halo, {}! Nilai anda setelah dikonversi adalah B+'.format(nama))
elif angka < 85:
    print('Halo, {}! Nilai anda setelah dikonversi adalah A-'.format(nama))
elif angka < 101:
    print('Halo, {}! Nilai anda setelah dikonversi adalah A'.format(nama))
else:
    print('Halo, {}! Mohon untuk mengisi nilai yang valid ya!'.format(nama))