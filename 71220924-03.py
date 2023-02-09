#Soal nomor 3
nhari_kerja = int(input("Hari kerja = "))
upah_total = (hari_kerja* 80000)
pajak = 5/100 * upah_total
upah_bruto = (upah_total)
upah_netto = (upah_bruto - pajak)



print("Upah karyawan sebelum pajak:", upah_bruto)
print("Pajak yang harus dibayar:", pajak)
print("Upah karyawan setelah pajak:", upah_netto)