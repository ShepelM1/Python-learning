txt = input("Введіть рядок: ")
new_txt = txt[::-1]

if txt == new_txt:
    print("Введений рячдок являється паліндромом.")
else:
    print("Введений рядок не паліндром.")
    