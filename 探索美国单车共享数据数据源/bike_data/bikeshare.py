import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('请输入你想知道的城市名:chicago,new york city,washington')
    city = input("请输入城市名:")
    print('请选择要筛选数据的月份:January,February,March,April,May or June:')
    month = input("请输入月份：")
    print('请选择周几是你想要看的，1表示Sunday')
    day = input('请输入你选择的日期:')

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city = 'chicago', month='January', day='4'):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # print(CITY_DATA[city])
    data = pd.read_csv(CITY_DATA[city])
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    # print(data['Start Time'].head())
    # 将date设置为index
    # df = data.set_index('Start Time')
    data['month'] = data['Start Time'].dt.month
    data['day_of_week'] = data['Start Time'].dt.weekday_name
    data['hour'] = data['Start Time'].dt.hour

    # print('*'*80)
    # print(data.head())
    # 获取某年的数据
    # print('*'*20)
    # print(df['2017'].head())
    # 获取某月的数据
    # print('*'*20)
    # print(df['2017-01'].head())

    if month != 'all' :
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        data = data[data['month'] == month]
        # print('*'*80)
        # print(data.head())

    if day != 'all' : 
        weeks = {'1':'Monday',
                 '2':'Tuesday',
                 '3':'Wednesday',
                 '4':'Thursday',
                 '5':'Friday',
                 '6':'Saturday',
                 '7':'Sunday',}
        data = data[data['day_of_week'] == weeks[day]]
        # print('*'*80)
        # print(data.head())

    print('*'*80)
    print(data.head())
    return data

#众数
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('-'*40)
    print('the most common month is :', df['month'].mode()['index'])

    # TO DO: display the most common day of week
    print('-'*40)
    print('the most common day of week is :',df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print('-'*40)
    print('the most common start hour is :' ,df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('-'*40)
    print('the most commonly used start station is :',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('-'*40)
    print('the most commonly used End station is :',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('-'*40)
    print('the most frequent combination of start station and end station trip is :',df['Trip Duration'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    # df = load_data()
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
