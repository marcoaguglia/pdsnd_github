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
    
    MONTH_CHOICES = {
    '0': 'all',    
    '1': 'january',
    '2': 'february',
    '3': 'march',
    '4': 'april',
    '5': 'may',
    '6': 'june'
        
    }
    DAY_CHOICES = {
    '0': 'all',
    '1': 'monday',
    '2': 'tuesday',
    '3': 'wednesday',
    '4': 'thursday',
    '5': 'friday',
    '6': 'saturday',
    '7': 'sunday'
    }
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_input = input('\nChoose the city: chicago, new york city, washington:\n ').strip().lower()
        if city_input in CITY_DATA:
            city = city_input
            break
        else:
            print("\nInvalid input: Accepted chicago, new york city, washington \n")
    print(f"\nYou selected: {city}") 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        print(MONTH_CHOICES)
        month_input = input('\nChoose the month:').strip()
        
        if month_input in MONTH_CHOICES:
          
            month = MONTH_CHOICES[month_input]
            break
        else:
            print("Invalid input: Accepted 0-6")
    print(f"\nYou selected: {month}") 
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:   
        print(DAY_CHOICES)
        day_input = input('\nChoose the day:')
        if day_input in DAY_CHOICES:
            day = DAY_CHOICES[day_input]
            break
        else:
            print("Invalid input: Accepted 0 - 7")
    print(f"\nYou selected: {day}") 
    

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['start hour'] = df['Start Time'].dt.hour
    df['end hour'] = df['End Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]
            
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    popular_hour = df['start hour'].mode()[0]
    popular_month = df['month'].mode()[0]
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print (f"\nMost Popular month: {popular_month}")
    print (f"\nMost Popular day: {popular_day_of_week}")
    print (f"\nMost Popular hour: {popular_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['direction'] = df['Start Station'] + " - " + df['End Station']
    popular_direction = df['direction'].mode()[0]
    
    print (f"\nMost Popular Start Station: {popular_start}")
    print (f"\nMost Popular End Station: {popular_end}")
    print (f"\nMost Popular direction: {popular_direction}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()

    
    print (f"\nTotal Time: {total_time}")
    print (f"\nMean time: {avg_time}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counts = df['User Type'].value_counts()
    print (f"\ncounts of user types: {type_counts}")
    try:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print (f"\ncounts of gender: {gender_counts}")
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min()) 
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        
        print (f"\nearliest year of birth: {earliest_year}")
        print (f"\nmost recent year of birth: {most_recent_year}")
        print (f"\nmost common year of birth: {most_common_year}")
    except KeyError:
        print("Gender & Birth Year not available for this city...")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_head(df):
    """Display 5 rows of raw data """
    row = 0
    while True:
        ans = input("\nWould you like to see 5 lines of raw data?  yes/no: ").strip().lower()
        if ans != 'yes':
            break
        print(df.iloc[row:row+5])
        row += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_head(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
