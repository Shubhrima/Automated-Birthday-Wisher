from smtplib import SMTP
import datetime as dt
import pandas
import random

MY_MAIL=ENTER_MAIL
MY_PASSWORD=ENTER_PASSWORD

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.today()
content = pandas.read_csv('birthdays.csv')
today_date = now.day
today_month=now.month
birth_date = content['day']

content_dict= content.to_dict() #converting to dictionary
birthdate_day_list=birth_date.to_list()
birthdate_month_list= content['month'].to_list()


content_df = content[(content['day'] == today_date) & (content['month']== today_month)]
try:
    birthday_person=str(content_df.iloc[0]['name'])
    print(birthday_person)
except:
    print('No Birthdays Today')

letters=['letter_1.txt', 'letter_2.txt']
num=random.randint(0,len(letters)-1)

letterloc= f'letter_templates/{letters[num]}'
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if content_df.empty:
    pass
else:
    with open(letterloc,'r+') as letter:
        l = letter.read()
        replace_string = l.replace('[NAME]',birthday_person)
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs='shubhrijana@gmail.com',
                                msg=f"Subject:Happy Birthday\n\n{replace_string}")
            print('Mail Sent')





# 4. Send the letter generated in step 3 to that person's email address.




