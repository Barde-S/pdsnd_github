import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

VALID_CITIES = CITY_DATA.keys()
VALID_MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
VALID_DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        # Get user input for city
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
        if city in VALID_CITIES:
            break
        else:
            print('Invalid city. Please choose a valid city.')

    while True:
        # Get user input for month
        month = input('Enter the month (e.g., January, February, ...), or "all" for no month filter: ').lower()
        if month in VALID_MONTHS:
            break
        else:
            print('Invalid month. Please enter a valid month or "all".')

    while True:
        # Get user input for day of the week
        day = input('Enter the day of the week (e.g., Monday, Tuesday, ...), or "all" for no day filter: ').lower()
        if day in VALID_DAYS:
            break
        else:
            print('Invalid day. Please enter a valid day or "all".')

    print('-' * 40)
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
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time'
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month_num = VALID_MONTHS.index(month) + 1
        df = df[df['Month'] == month_num]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculate common month, day, and start hour
    common_month = df['Month'].mode()[0]
    common_day = df['Day of Week'].mode()[0]
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]

    print(f'Most common month: {VALID_MONTHS[common_month - 1].title()}')
    print(f'Most common day of week: {common_day}')
    print(f'Most common start hour: {common_hour}:00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculate common start station, end station, and station combination
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_station_combination = df['Station Combination'].mode()[0]

    print(f'Most common start station: {common_start_station}')
    print(f'Most common end station: {common_end_station}')
    print(f'Most frequent combination of start and end stations: {common_station_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time and mean travel time
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    print(f'Total travel time: {total_travel_time} seconds')
    print(f'Mean travel time: {mean_travel_time} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types:')
    for user_type, count in user_type_counts.items():
        print(f'{user_type}: {count}')

    # Display counts of gender if 'Gender' column is available
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:')
        for gender, count in gender_counts.items():
            print(f'{gender}: {count}')
    else:
        print('\nGender information is not available for this city.')

    # Display earliest, most recent, and most common year of birth if 'Birth Year' column is available
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print(f'\nEarliest birth year: {earliest_birth_year}')
        print(f'Most recent birth year: {most_recent_birth_year}')
        print(f'Most common birth year: {common_birth_year}')
    else:
        print('\nBirth year information is not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

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
