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
    city = input("Please enter a city (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        print("Invalid city. Please try again.")
        city = input("Please enter a city (chicago, new york city, washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter a month (all, january, february, ... , june): ").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        print("Invalid month. Please try again.")
        month = input("Please enter a month (all, january, february, ... , june): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day of week (all, monday, tuesday, ... sunday): ").lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        print("Invalid day. Please try again.")
        day = input("Please enter a day of week (all, monday, tuesday, ... sunday): ").lower()

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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
     return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most common month: {common_month}')

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most common day of week: {common_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'Most common start hour: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station: {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station: {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f'Most frequent combination of start station and end station trip: {common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time: {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'Counts of user types:\n{user_types}')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f'Counts of gender:\n{gender_counts}')
    else:
        print('Gender data not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print(f'Earliest year of birth: {earliest_year}')
        print(f'Most recent year of birth: {most_recent_year}')
        print(f'Most common year of birth: {most_common_year}')
    else:
        print('Birth year data not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of raw data based on user request."""
    row_index = 0
    while True:
        user_input = input("Would you like to see 5 lines of raw data? Enter yes or no: ").strip().lower()
        if user_input == 'yes':
            if row_index < len(df):
                print(df.iloc[row_index:row_index + 5])  # Display the next 5 rows
                row_index += 5  # Move to the next set of rows
            else:
                print("No more raw data to display.")
                break  # Exit the loop if no more data
        elif user_input == 'no':
            print("Exiting the data display.")
            break  # Exit the loop if the user says no
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Call the display_data function to show raw data
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
