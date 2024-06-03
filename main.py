with open('recipient.txt', 'r', encoding="utf-8") as f:
    recipient_info = f.readlines()
    recipient_name = recipient_info[0].strip()
    recipient_address = recipient_info[1].strip()
    recipient_inn = recipient_info[2].strip()
    recipient_kpp = recipient_info[3].strip()

with open('buyer.txt', 'r', encoding="utf-8") as f:
    buyer_info = f.readlines()
    buyer_name = buyer_info[0].strip().split(': ')[1]
    buyer_address = buyer_info[1].strip().split(': ')[1]
    buyer_phone = buyer_info[2].strip().split(': ')[1][:2] + '******' + buyer_info[2].strip().split(': ')[1][-4:]

with open('order.txt', 'r', encoding="utf-8") as f:
    order_info = f.readlines()
    order_list = []
    for line in order_info:
        item = line.strip().split(';')
        order_list.append(item)

with open('score.txt', 'w') as f:
    f.write('Отправитель:\n')
    f.write(f'{recipient_name}\n')
    f.write(f'Адресс: {recipient_address}\n')
    f.write(f'ИНН: {recipient_inn}\n')
    f.write(f'КПП: {recipient_kpp}\n\n')
    f.write('Получатель:\n')
    f.write(f'{buyer_name}\n')
    f.write(f'Номер телефона: {buyer_phone}\n')
    f.write(f'Адрес доставки: {buyer_address}\n\n')
    f.write('№   Наименование   Кол   Цена   Сумма\n')
    f.write('-' * 65 + '\n')
    total_sum = 0
    for i in range(len(order_list)):
        item_name = order_list[i][0]
        item_count = int(order_list[i][1])
        item_price = int(order_list[i][2])
        item_sum = item_count * item_price
        total_sum += item_sum
        f.write(f'{i+1:<3}{item_name:<15}{item_count:<6}{item_price:<7}{item_sum:<6}\n')
    f.write('-' * 65 + '\n')
    f.write(f'Итого: {total_sum} рублей 00 копеек.\n')

print('Заказ оформлен!')
