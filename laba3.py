from datetime import datetime
def get_day_of_year(date):
    return date.timetuple().tm_yday

date = datetime(2004, 3, 23)  
day_of_year = get_day_of_year(date)
print(day_of_year)
