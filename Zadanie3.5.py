shopping_dict = {
    'piekarnia':('chleb', 'bulki', 'paczek'),
    'warzywniak':('marchew', 'seler', 'rukola')
}
for shop, products in shopping_dict.items():
    print('Ide do {}, kupuje tu nastepujace rzeczy: '.format(shop.capitalize()))