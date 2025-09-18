import random
import datetime as dt
import smtplib

import pandas as pd
import datetime as dt

# get today's month and day
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# read CSV into DataFrame
df = pd.read_csv("birthdays.csv")

# filter rows where month and day match today's
birthdays_today = df[(df["month"] == today_month) & (df["day"] == today_day)]


letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

chosen_letter = random.choice(letters)

with open(f"letter_templates/{chosen_letter}", "r") as letter_file:
    letter_contents = letter_file.read()
    letter_contents = letter_contents.replace("[NAME]", birthdays_today.iloc[0]["name"])
    
my_email = "opeola3333@gmail.com"
password = "vxkazxwoqawettts"

recipient_email = birthdays_today.iloc[0]["email"]

with smtplib.SMTP("smtp.gmail.com", 587) as connection: # Use port 587 for TLS
    connection.ehlo()
    connection.starttls()  # Secure the connection
    connection.ehlo()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,  # put your recipient email here
        msg=f"Subject:Birthday Wishes\n\n{letter_contents}"
    )

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




