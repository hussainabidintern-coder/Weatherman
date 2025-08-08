import pandas as pd
import os


def humanized_date(date_str):
    parts = date_str.split("-")
    
    if len(parts) == 3:
      year, month, day = parts
      month_of_year = int(month) -1
      return f"{months [month_of_year]} {int(day) }, {year}"
    return date_str

class MonthData:
    def __init__(self, filepath):
        self.filepath = filepath
        print('self path', self.filepath)
        self.df = pd.read_csv(filepath)

        self.df.columns = self.df.columns.str.strip()
        print("Cleaned columns:", self.df.columns.tolist())
    
    def get_max_temperature(self):
       
        row = self.df.loc[self.df['Max TemperatureC'].idxmax()]
        print('row ', row["PKT"], row["Max TemperatureC"])
        return row["PKT"], row["Max TemperatureC"]

    def get_min_temperature(self):
        row = self.df.loc[self.df['Min TemperatureC'].idxmin()]
        return row["PKT"], row["Min TemperatureC"]

    def get_max_humidity(self):
        row = self.df.loc[self.df['Max Humidity'].idxmax()]
        return row["PKT"], row["Max Humidity"]
    
    def get_min_humidity(self):
        print()
        row = self.df.loc[self.df['Min Humidity'].idxmin()]
        return row["PKT"], row["Min Humidity"]
    
    def get_avg_temperature(self):
        if 'Mean TemperatureC' in self.df.columns:
            return self.df['Mean TemperatureC'].mean()
        else:
            return 0

    def get_avg_humidity(self):
        if 'Mean Humidity' in self.df.columns:
            return self.df['Mean Humidity'].mean()
        else:
            return 0
    

    def show_summary(self):
        print('1234567876543')
        date_max_temp, max_temp = self.get_max_temperature()
        date_min_temp, min_temp = self.get_min_temperature()
        date_max_humid, max_humid = self.get_max_humidity()
        date_min_humid, min_humid = self.get_min_humidity()
        # date_mean_temp , mean_temp = self.get_avg_temperature()
        # date_mean_humid , mean_humid = self.get_avg_humidity()

        print(f"Summary for file: {self.filepath}")
        print(f"->Hottest Day: {date_max_temp}, {max_temp}C")
        print(f"-> Coldest Day: {date_min_temp}, {min_temp}C")
        print(f"-> Most Humid Day: {date_max_humid}, {max_humid}%")
        print(f"-> Min Humid Day: {date_min_humid}, {min_humid}%")
        # print(f"-> Mean Temperature: {date_mean_temp}, {mean_temp}C")
        # print(f"-> Mean Humidity: {date_mean_humid}, {mean_humid}%")
        print("-" * 50)


class YearData:
  

    def __init__(self, year):
        self.year = year
        self.months = []
        self.yearly_max_temp = 0
        self.yearly_max_temp_date = 0
        self.yearly_min_temp = 0
        self.yearly_min_temp_date = 0
        self.yearly_max_humid = 0
        self.yearly_max_humid_date = 0
    
    def compare_and_set_max_temp(self,month):
        date_max_temp, max_temp = month.get_max_temperature()
        if self.yearly_max_temp < max_temp:
            self.yearly_max_temp = max_temp
            self.yearly_max_temp_date = date_max_temp

    def compare_and_set_min_temp(self,month):
        date_min_temp, min_temp = month.get_min_temperature()
        if self.yearly_min_temp < min_temp:
            self.yearly_min_temp = min_temp
            self.yearly_min_temp_date = date_min_temp

    def compare_and_set_humidity(self,month):
        date_max_humidity, max_humid = month.get_max_humidity()
        if self.yearly_max_humid < max_humid:
            self.yearly_max_humid= max_humid
            self.yearly_max_humid_date = date_max_humidity

    def add_month(self, month_data):
        self.months.append(month_data)
    def print_summery(self):
        print(f"Summary for Year: {self.year}")
        print(f"-> Hottest Day: {self.yearly_max_temp}C at {humanized_date(self.yearly_max_temp_date)}")
        print(f"-> Coldest Day: {self.yearly_min_temp}C at {humanized_date(self.yearly_min_temp_date)}")
        print(f"-> Most Humid Day: {self.yearly_max_humid}% at {humanized_date(self.yearly_max_humid_date)}")


    # def humanized_date(self, date):
    #     self.date_format = date
    #     parts = self.date_format.split("-")
    #     if len(parts) == 3:
    #         year, month, day = parts
    #         month_index = int(month) - 1
    #         return f"{int(day)} {months[month_index]} {year}"
    #     return self.date_format
    
    



    def show_year_summary(self):
        print(f"===== Weather Summary for Year {self.year} =====")
        for month in self.months:
            self.compare_and_set_max_temp(month)
            self.compare_and_set_min_temp(month)
            self.compare_and_set_humidity(month)
        self.print_summery()
            



weather_folder = r"G:\Devsinc Internship\WeatherMan\lahore_weather\lahore_weather"

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']



year = 2004
year_data = YearData(year)


for month in months:
    filename = f"lahore_weather_{year}_{month}.txt"
    filepath = os.path.join(weather_folder, filename)
    
  
    if os.path.exists(filepath):
        month_data = MonthData(filepath)
        year_data.add_month(month_data)
    else:
        print(f"File not found: {filepath}")


year_data.show_year_summary()



aug_data = MonthData(r"G:\Devsinc Internship\WeatherMan\lahore_weather\lahore_weather\lahore_weather_1998_Aug.txt")
aug_data.show_summary()







