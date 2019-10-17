def age_to_time(age): 
    age = input("How old are you?")
    months = 
    print("months : " + str(months) + "days : " + str(days) + "hours : " + str(hours) + ", and minutes : " + str(minutes))


def birthday_to_time(birthday):
    birthday = ("When were you born?")
    birthday_list = birthday.split()
    string_month = birthday[0] + birthday[1]
    string_day = birthday[3] + birthday[4]
    string_year = birthday[6] + birthday[7] + birthday[8] + birthday[9]
    month = int(string_month)
    day = int(string_day)
    year = int(string_year)
    
    month_29 = [2]
    month_30 = [9, 4, 6, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month_28:
        month_count = 

        # calculate years they were alive in terms of months



