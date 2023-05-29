from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S21", "+79123456789")
phone2 = Smartphone("Apple", "iPhone 12", "+79234567890")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79345678901")
phone4 = Smartphone("Huawei", "P40 Pro", "+79456789012")
phone5 = Smartphone("Google", "Pixel 5", "+79567890123")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")