# soal no 1
#input
jam_1 = int(input("Masukan jam 1:"))
menit_1 = int(input("Masukan menit 1:"))
jam_2 = int(input('Masukan jam 2:'))
menit_2 = int(input("Masukan menit 2:"))

if jam_1 < jam_2:
    if menit_1 < menit_2:
        hasil = (jam_2 - jam_1)*60 + (menit_2- menit_1)
    else:
        hasil = (jam_2-1 - jam_1)*60 + (60+(menit_2 - menit_1))

else:
    if jam_1 < jam_2 :
        hasil = 24*60 + (jam_2 - jam_1)*60 + (menit_2 - menit_1)
    else:
        hasil = 24*60 + (jam_2-1 - jam_1)*60 +(60+(menit_2 - menit_1))

print("selisih antara", str(jam_1)+":"+str(menit_1), "dan", str(jam_2)+":"+str(menit_2), "adalah", hasil, "menit")   


