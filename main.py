from vedingmachine import VedingMachina

B = VedingMachina()
# # ## T1 be
# a = VedingMachina()
B.add_beverage("cola", 11000)
B.add_beverage("fanta", 12000)
B.add_beverage("pepsi", 10000)
# # print(a.get_price("cola"))
# # print(a.get_price("colaaa"))
# # a.beverage_LIST()
#
#
#
# # T 2 carta
# # a = VedingMachina()
B.rechargeCard(12, 100000)
B.rechargeCard(12, 100000)
B.rechargeCard(15, 21300)
# # print(a.getCredit(15))
# a.getlistCart()
#
# # T 3
# # a = VedingMachina()
# a.refill_column(1, "cola", 10)
# a.refill_column(1, "cola", 10)
B.refill_column(1, "cola", 10)
B.refill_column(2, "fanta", 100)
B.refill_column(3, "pepsi", 10)
# a.availableCans()
#
# a.sell(12, "cola")
# a.availableCans()
# a.getlistCart()
B = VedingMachina()
while True:
    a = int(input("Admin bo'lsangiz 1 ni, foydalanuvchi bo'lsangiz 2 ni, karta bolimi 3 ni chiqmoqchi bo'lsangiz 4 ni kirting "))
    if a == 1:
        while True:
            j = input("mashinaga mahsulot qo'shmoqchimisiz(1) yoki mahsulotni ko'rmoqchimisiz?(2) ")
            if j == "1":
                n = input("ichimlik nomini kirting:")
                u = int(input("ichimlikni ustunini raqamini kirting:"))
                b = int(input("bankalar sonini kirting:"))
                s = int(input("ichimlikning narhini kirting"))
                B.add_beverage(n, s)
                B.refill_column(u, n, b)
                f = input("yana ichimlik kiritasizmi  y/h ")
                if f == "y":
                    break
            else:
                B.availableCans()
                break
    elif a == 2:
        while True:
            B.beverage_LIST()
            id = int(input("karta ID isini kirting"))
            ich = input("ichimlik nomini kirting:")
            B.sell(id, ich)
            q = input("yana ichimlik sotib olasizmi h/y ")
            if q == "y":
                break
    elif a == 3:
        l = input("kartani to'ldirasizmi(1)  yoki kartalar haqida malumot olasizmi(2)")
        if l == "1":
            r = int(input("karta id sini kirting"))
            k = int(input("to'ldirmoqchi bo'lgan sumani kirting: "))
            B.rechargeCard(r, k)
        else:
            B.getlistCart()
    else:
        break


