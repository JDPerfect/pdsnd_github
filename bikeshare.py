import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Lists of the cities using bikeshare
Name_of_City = ['chicago','new york city','washington']
Name_of_Month =['january','february','march','april','may','june','july','august','september','october','november','december','all']
Name_of_days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']


def get_cityfilters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:


        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    try:
        city=input("Enter the name of city to view the bikeshare data 'chicago or new_york_city or washington':").lower()
        while (city not in Name_of_City):
            print ("The user has entered invalid Input, kindly enter city name among chicago, new york city or washington")
            city=input("Enter the name of city to view the bikeshare data:").lower()

            break
        print("User has entered",city)
    except:
        print("error")


    # TO DO: get user input for month (all, january, february, ... , june)


    try:
        month=input("Enter the month of selected city to view the bikeshare data 'January - December':").lower()
        while (month not in Name_of_Month):
            print ("The user has entered invalid Input, kindly enter correct month")
            month=input("Enter the correct month of selected city to view the bikeshare data:").lower()

            break
        print("User has entered",month)
    except:
        print("error")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    try:
        day=input("Enter the day of selected city to view the bikeshare data 'Monday - Sunday':").lower()
        while (day not in Name_of_days):
           print ("The user has entered invalid Input, kindly enter correct day")
           day=input("Enter the correct day of selected city to view the bikeshare data:").lower()
           break
        print("User has entered",day)
    except:
        print("error")


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

    # extract the data file for the selected city
    df = pd.read_csv(CITY_DATA[city])


    #convert start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time']) #Practice Solution
    #print(df['Start Time'])

    #month, day , hour
    df['month'] = df['Start Time'].dt.month # Practice Solution
    #print(df['month'])

    df['day_of_week'] = df['Start Time'].dt.day_name() # Practice Solution
    #print(df['day_of_week'])

    df['hour'] = df['Start Time'].dt.hour # Practice Solution
    #print(df['hour'])

    #Name_of_Month = ['january','february','march','april','may','june','july','august','september','october','november','december']
    if month != 'all': # Practice Solution
        month = Name_of_Month.index(month)+1 # Practice Solution
        #print(month)
        df = df[df['month']==month]  # Practice Solution
        #print(df)
    if day != 'all':  # Practice Solution
        df = df[df['day_of_week']==day.title()]  # Practice Solution
        #print(df)


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    #common_month = df['month'].mode()[0]
    common_month = df['month'].value_counts().idxmax()
    print("\n the most common month is: ",common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].value_counts().idxmax()
    print("\n the most common day is: ",common_day)

    # TO DO: display the most common start hour

    common_hour = df['hour'].value_counts().idxmax()
    print("\n the most common hour is: ",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station_count = df['Start Station'].value_counts()[0]
    common_start_station_name = df['Start Station'].value_counts().idxmax()
    print("\nThe most commonly used start station is: ",common_start_station_name, "Counts:" , common_start_station_count)


    # TO DO: display most commonly used end station

    common_end_station_count = df['End Station'].value_counts()[0]
    common_end_station_name = df['End Station'].value_counts().idxmax()
    print("\nThe most commonly used end station is: ",common_end_station_name, "Counts:" , common_end_station_count)

    # TO DO: display most frequent combination of start station and end station trip


    df['Station Combo']= df['Start Station'] + ' ' + df['End Station'] #knowledge center
    frequent_station_combo_counts = df['Station Combo'].value_counts()[0]
    frequent_station_combo = df['Station Combo'].value_counts().idxmax()
    print('\nMost frequently used station combination is: ', frequent_station_combo, "Counts:" , frequent_station_combo_counts)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ', total_travel_time)


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time in seconds is: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))


    print('-' * 40)
    return df

    # TO DO: user information
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('The total number of users by user type is: ',user_types)



    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print("There is no Gender information for washington")
    else:
        user_gender = df['Gender'].value_counts()
        print('the total number of users by gender is: ',user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print("There is no Birth Year information for washington")
    else:
        older = df['Birth Year'].min()
        younger = df['Birth Year'].max()
        common = df['Birth Year'].value_counts().idxmax()
        print('the older user birth year: ' , older)
        print('the younger user birth year: ', younger)
        print('Most common users birth year: ', common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display raw of the city
def display_raw_data(df, city, month, day):

    #df = pd.read_csv(CITY_DATA[city])
    reply = input("Would you want to see the raw details yes or no?")
    if reply == "yes":
       print("The raw details of city: ", city ," month: ", month, ",day: ", day)
       count = 0
       for index,row in df.iterrows():
           print(row[0],row[1],row[2],row[3],row[4],row[5],row["day_of_week"])
           count = count +1
           if count %5 ==0:
              reply = input("Do you want to continue?")
              if reply == "yes":
                 continue
              else:
                break


def main():
    while True:

        city, month, day = get_cityfilters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
