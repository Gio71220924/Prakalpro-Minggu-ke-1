# soal no 1

jam_awal = int(input("Masukan jam awal:"))
menit_awal = int(input("Masukan menit awal:"))
jam_akhir = int(input('Masukan jam akhir:'))
menit_akhir = int(input("Masukan menit akhir:"))

selisih_jam = (jam_akhir - jam_awal)*60
selisih_menit = (menit_akhir - menit_awal)

selisih_waktu = print(selisih_jam + selisih_menit)

print("Selisih waktunya adalah", selisih_waktu, "menit")