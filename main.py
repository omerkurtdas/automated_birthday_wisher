
import datetime as dt
import random
import pandas as pd
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data.iloc[index].month, data.iloc[index].day): data_row for (index, data_row) in data.iterrows()}
df = birthdays_dict[today]
print(df[1])
if today in birthdays_dict:
    random_number = random.randint(1,3)
    with open(f"letter_templates/letter_{random_number}.txt") as file:
        letter_text = file.read()
        new_letter = letter_text.replace("[NAME]",df[0])

my_email = "kurtdasomer@gmail.com"
password = "oviipvhzpkuhevms"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection :
    #the code below line makes this connection secure.
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=df[1],
                        msg=f"Subject:Happy Birthday\n\n{new_letter}"
                        )



