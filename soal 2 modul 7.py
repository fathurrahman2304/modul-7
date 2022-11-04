print('Ordinal Number')
print('Ketik 0 untuk menghentikan program')
def angka(nomor):
    x == nomor
    a = nomor % 10
    if a == 1:
        return nomor,'st'
    elif a == 2:
        return nomor,'nd'
    elif a == 3:
        return nomor,'rd'
    elif a in range(4,21):
        return nomor,'th'
    elif a == 0:
        return nomor,'th'
x = ''
try:
    while x != 0:
        nomor = int(input('Masukkan angka: '))
        print(angka(nomor))
        if nomor == 0:
            print('terima kasih telah menggunakan program saya')
            quit()
        elif nomor < 0:
            print('inputan harus dalam bentuk angka dan tidak kurang dari 0')
except ValueError:
    print('inputan harus dalam bentuk angka dan tidak kurang dari 0')