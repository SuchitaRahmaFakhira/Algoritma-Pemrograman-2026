# Program Mengecek Pertidaksamaan Linear
# Bentuk pertidaksamaan: a*x + b > c

print("=== PROGRAM CEK PERTIDAKSAMAAN ===")
print("Bentuk pertidaksamaan: a*x + b > c")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
x = float(input("Masukkan nilai x yang akan diuji: "))

hasil = (a * x) + b

print("\nPertidaksamaan yang diuji:")
print(f"{a}x + {b} > {c}")

print(f"Ruas kiri = ({a} × {x}) + {b} = {hasil}")
print(f"Ruas kanan = {c}")

if hasil > c:
    print(f"\nKesimpulan: x = {x} MEMENUHI pertidaksamaan.")
else:
    print(f"\nKesimpulan: x = {x} TIDAK MEMENUHI pertidaksamaan.")