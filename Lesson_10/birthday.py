import random
import datetime

while True:
    number = input("Cколько др генерируем?(от 2 до 70):")
    if not number.isdigit() or int(number) < 2 or int(number) > 70:
        print("!!!Введи число ОТ 2 ДО 70!!!")
        print("-" * 10)
    else:
        number = int(number)
        break

birthdays = []
start_of_year = datetime.date(2010,1,1)
for _ in range(number):
    sdwig = random.randint(0,364)
    random_day = datetime.timedelta(sdwig)
    birthday = start_of_year + random_day
    birthdays.append(birthday)

for i in range(number):
    print(f"{i + 1}) {birthdays[i].strftime('%d.%m.%y')}")

print("="*10)
for q in set(birthdays):
    if birthdays.count(q) > 1:
        print(f"- {q.strftime('%d.%m.%y')} Встречается {birthdays.count(q)}раза")
