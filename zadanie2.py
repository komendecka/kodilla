wynik = []
powers = []
# for i in range(0, 100):
#     if i % 5 == 0:
#         wynik.append(i)
x = [wynik.append(i) for i in range(0, 100) if i % 5 == 0]
print(wynik)

for j in wynik:
    powers.append(j ** 3)
print(powers)
