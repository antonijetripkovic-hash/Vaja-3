word=input("Vnesite besedo: ").lower()
if word==word[::-1]:
    print("Beseda je palindrom")
else:
    print("Beseda ni palindrom")