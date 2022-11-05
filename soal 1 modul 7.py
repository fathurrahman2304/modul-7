def prima(x):
    x == angka
    a = 'bilangan prima'
    if x <= 1:
        a = 'bukan bilangan prima'
    for i in range(2,x):
        if x % i == 0:
            a = 'bukan bilangan prima'
    return f'{x} adalah {a}'
angka = int(input('Masukkan angka: '))
print(prima(angka))