shopping_dict = {
    'piekarnia':('chleb', 'bulki', 'paczek'),
    'warzywniak':('marchew', 'seler', 'rukola')
}
suma = 0
for shop, products in shopping_dict.items():
    capitalize_products = [product.capitalize() for product in products]
    print('Ide do {}, kupuje tu nastepujace rzeczy: {}'.format(shop.capitalize(),capitalize_products))
    suma = suma + len(shopping_dict[shop])
print(f'W sumie kupuje {suma} produktow')
print("Zadanie zakonczone pomyslnie")
print("Pozdrowionka dla Patryka")