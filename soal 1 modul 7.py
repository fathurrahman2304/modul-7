def prima(x = int(input('Masukkan angka: '))):
    a = 'bilangan prima'
    if x <= 1:
        a = 'bukan bilangan prima'
    for i in range(2,x):
        if x % i == 0:
            a = 'bukan bilangan prima'
    print(x,'adalah',a)
prima()