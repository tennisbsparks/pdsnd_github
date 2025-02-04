import time
import pandas as pd

# this code analyzes bikeshare data
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
    print('Hello! Let\'s explore some US bikeshare data for Chicago, New York City, or Washington!')
    # Data is only available for Chicago, New York City, or Washington
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Since the cities have different first letters, have the user enter the first letter of the city to reduce input errors
    city_selection = input(str("Please choose a city, \n1: Chicago (enter 1)\n2: New York City (enter 2) \n3: Washington D.C.(enter 3)\n "))

    while city_selection not in {"1", "2", "3"}:
        print("Check your input - You must choose 1, 2, or 3")
        city_selection = input(str("Please choose a city, \n1: Chicago (enter 1)\n2: New York City (enter 2) \n3: Washington D.C.(enter 3)\n "))
    # take the user's input number and assign to the correct city
    if city_selection == "1":
        city = 'chicago'
    elif city_selection == "2":
        city = 'new york city'
    elif city_selection == "3":
        city = 'washington'
<<<<<<< HEAD

    # ask the user if want to analyze by month or date or both or neither month nor date
||||||| e0d4786
        
    # ask the user if want to analyze by month or date or both or not at all
=======

    # ask the user if want to analyze by month or date or both or not at all
>>>>>>> documentation
    time_selection = input('\n\nWould you like to analyze {}\'s data by month, day, both, or none? \nType month or day or both or none: \n '.format(city.title())).lower()

    while time_selection not in {'month','day','both','none'}:
        print("Invalid input")
        time_selection = input('\n\nWould you like to filter {}\'s data by month, day, both, or none? \nType month or day or both or none: \n '.format(city.title())).lower()
<<<<<<< HEAD

    # call two different functions to handle time_choice -- get_month, get_day
    # use these functions for all calls
||||||| e0d4786
   
    # call two different functions to handle time_choice -- get_month, get_day, and use both functions for all
=======

    # call two different functions to handle time_choice -- get_month, get_day, and use both functions for all
>>>>>>> documentation
    if time_selection == 'none':
        month, day = 'all', 'all'
    elif time_selection == 'month':
        month = get_month()
        day = 'all'
    elif time_selection == 'day':
        day = get_day()
        month = 'all'
    elif time_selection == 'both':
        month = get_month()
        day = get_day()

    print('-'*40)
    return city, month, day

# define function that gets the month -- call function get_month
def get_month():
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by

    """
    print("\nThe months of data available are January to June\n")
    month = input("Please enter a value from 1 to 6 to specify the month. i.e. For January enter 1. \n ")

    while month not in {'1','2','3','4','5','6'}:
        print("You did not choose a number based on January to June (1 to 6)")
        month = input("Please enter a value from 1 to 6 to specify the month, \n For example if you want January enter: 1 \n For June, enter 6:\n")

    return month

# define function that gets the day -- call function get_day
def get_day():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day to filter by

    """
    print("There are seven days in a week. Sunday is 1, Monday is 2, etc.\n")
    day = input("Please enter a value from 1 to 7 for the day of the week beginning with Sunday. \n Sunday is 1, Monday is 2, Tuesday is 3... \n ")

    while day not in {'1','2','3','4','5','6','7'}:
        print("Invalid Input - You must enter a number from 1 to 7 for the day of the week.")
        day = input("Please enter a value from 1 to 7 for the day of the week, \n Sunday is 1, Monday is 2, Tuesday is 3... \n ")

    return day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour



    # filter by month if applicable
    if month != 'all':


        # filter by month to create the new dataframe
        df = df[df['month'] == int(month)]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
        day = days[int(day)-1]
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nMost Common Month: ' + str(df['month'].mode()[0]))


    # display the most common day of week
    print('\nMost Common Day of Week: ' + str(df['day_of_week'].mode()[0]))


    # display the most common start hour
    print('\nMost Common Start hour: ' + str(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost Commonly Used Start Station: ' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('\nMost Commonly Used End Station: ' + str(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trip: ' + str(df.groupby(['Start Station','End Station']).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal Travel Time in Seconds: ' + str(df['Trip Duration'].sum()))

    # display mean travel time
    print('\nMean Travel Time in Seconds: ' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCounts of User Types: \n' + str(df['User Type'].value_counts()))

    # display gender counts if the city is not Washington
    if city != 'washington':
        print('\nGender Counts: \n' + str(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nEarliest Birth Year: ' + str(int(df['Birth Year'].min())))
        print('\nMost Recent Birth Year: ' + str(int(df['Birth Year'].max())))
        print('\nMost Common Birth Year: ' + str(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(city):
    """
    Asks the user if they want to see 5 rows of data
    if yes then it prints 5 rows and then asks the user again
    """
    show_raw_5 = input("Would you like to see 5 rows of raw data? \n Type: yes or no \n ").lower()

    while show_raw_5 not in {'yes','no'}:
        print("Invalid input -- You must answer yes or no.")
        show_raw_5 = input("Would you like to see 5 rows of data? \n Type: yes or no \n ").lower()

    if show_raw_5 == 'no':
        return

    for show5 in pd.read_csv((CITY_DATA[city]), chunksize=5):
        pd.set_option('display.max_columns', 200)
        print(show5)
        show5 = input("Would you like to see 5 more rows of data? \n Type: yes or no \n ").lower()

        while show5 not in {'yes','no'}:
            print("Invalid input -- You must answer yes or no.")
            show5 = input("Would you like to see 5 more rows of data? \n Type: yes or no \n ").lower()

        if show5 == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
