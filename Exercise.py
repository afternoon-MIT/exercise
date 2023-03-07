from datetime import date
date_today=date.today().strftime("%A %d %B %Y")
print(day_today)
day= str(input(Enter Todays day))
if day == day_today:
    print(f"Today is{day_today}\nCorrect!")

elif day !=day_today:
    print("Your answer is incorrect!\n..Enter correct day\n:")