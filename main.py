def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    return a / b

if __name__ == "__main__":
    print("5 + 3 =", tambah(5, 3))
    print("5 - 3 =", kurang(5, 3))
    print("5 * 3 =", kali(5, 3))
    print("5 / 0 =", bagi(5, 0))
# B
