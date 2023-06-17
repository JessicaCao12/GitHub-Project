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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    
    while True:
        city = input('Please choose one of the following cities, Chicago, New York City or Washington to explore:\n').lower()
        if city not in cities:
            print('You can only entry one of the following cities, Chicago, New York City or Washington, please try it again\n')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    while True:
        month = input('Please enter a month:\n e.g. January, February, ... , June\n').lower()
        if month not in months:
            print('Invalid request. Please try again.')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'june','saturday','sunday']
    
    while True:
        day = input('Please enter a day:\n e.g. Monday, Tuesday, ... , Sunday\n').lower()
        if day not in days:
            print('Invalid request. Please try again.')
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     #-- Load Data --#
    df=pd.read_csv(CITY_DATA[city])
    
    #-- Determin start time --#
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #-- Determin month, weekday and hour from start time#
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month 
    if month != 'all':
        Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month =  Months.index(month)
        df = df[ df['month'] == month ]

    # filter by weekday 
    if day != 'all':
        df = df[ df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_commen_month = df['month'].mode()[0]
    print('The Most Common Month of Travel:',most_commen_month)
   

    # TO DO: display the most common day of week
    most_commen_weekday = df['weekday'].mode()[0]
    print('The Most Common Day Of Week of Travel:',most_commen_weekday)

    # TO DO: display the most common start hour
    most_commen_start_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour of Travel:',most_commen_start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commen_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly Used Start Station:',most_commen_start_station)
   

    # TO DO: display most commonly used end station
    most_commen_end_station = df['End Station'].mode()[0]
    print('The Most Commonly Used End Station:',most_commen_end_station)
   

    # TO DO: display most frequent combination of start station and end station trip
    most_commen_combination_trip = df[['Start Station', 'End Station']].mode().loc[0]
    print('The Most Common Month of Travel:\n',most_commen_combination_trip)
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_days = round(float(df['Trip Duration'].sum()/3600/12),2)
    print("Total Travel Time in Days:", total_travel_time_days)


    # TO DO: display mean travel time
    mean_travel_time_mins = round(float(df['Trip Duration'].mean()/60),2)
    print("Mean Travel Time in Minutes:", mean_travel_time_mins)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('\nCount by User Types:\n',counts_user_types)


    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('Sorry! Gender data unavailable for selected city')
    else:
        counts_gender = df['Gender'].value_counts()
        print('\nCount by Gender:\n',counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Sorry! Birth year data unavailable for selected city')
    else:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode())
        print('\nThe Oldest User was born in Year: ',earliest_birth_year)
        print('The Youngest User was born in Year: ',most_recent_birth_year)
        print('The Majority of Users were born in Year: ',most_common_birth_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    """Displays 5 lines of raw data upon request by user."""
    pd.set_option('display.max_columns',200)
    user_wish = ['yes','no']
    raw_date_line = 0 
    while True:
        user_answer = input('\nWould you like to view the next 5 line of raw data? Enter yes or no.\n').lower()
        if user_answer not in user_wish:
            print('Invalid request. Please try again.')
            continue
        elif user_answer == 'yes':
            print(df[raw_date_line:raw_date_line+5])
            raw_date_line += 5
            continue
        else:
            break
                
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
