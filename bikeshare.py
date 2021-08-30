import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
    selected_city = ''
    while selected_city.lower() not in CITY_DATA:
        selected_city = input("\n We have three datasets New York, Chicago and Washington. Please input one of them. \n")
        if selected_city.lower() in CITY_DATA:
           city = CITY_DATA[selected_city.lower()]
        else:
            print("\n Sorry you have to input New York, Chicago or Washington. \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    selected_month = ''
    while selected_month.lower() not in MONTH_DATA:
        selected_month = input("\n which month you need to filter data on it? (January - June) \n")
        if selected_month.lower() in MONTH_DATA:
           month = selected_month.lower()
        else:
            print("Sorry you have to input a month from January to June.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    selected_day = ''
    while selected_day.lower() not in DAY_DATA:
        selected_day = input("\n Which day you need to filter data on it? \n")
        if selected_day.lower() in DAY_DATA:
            day = selected_day.lower()
        else:
            print("Sorry you have to input a day.\n")

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

    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month)

        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[most_common_month].title())

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination is : " + str(most_frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(count_user_types))
    
    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        count_gender = df['Gender'].value_counts()
        print("The count of user gender is: \n" + str(count_gender))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_year_birth = df['Birth Year'].mode()[0]
        print('Earliest birth is: {}\n'.format(earliest_birth))
        print('Most recent birth is: {}\n'.format(most_recent_birth))
        print('Most common year birth is: {}\n'.format(most_common_year_birth))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    print(df.head())
    next = 0
    while True:
        display_5raws_data = input('\n Do you want to see 5 rows of data? Enter yes or no.\n')
        if display_5raws_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        while True:
            display_5raws_data = input('\n Do you want to see 5 rows of data? Enter yes or no.\n')
            if display_5raws_data.lower() != 'yes':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
