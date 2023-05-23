def bank(X, Y):
    interest_rate = 0.1  
    for _ in range(Y):
        X += X * interest_rate

    return X

X = float(input("Введите сумму вклада: "))
Y = int(input("Введите количество лет: "))

total_amount = bank(X, Y)
print("Сумма на счету спустя", Y, "лет:", total_amount)