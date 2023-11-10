# Convert C# code to Python code

from datetime import datetime, timedelta


def main():
    """
    Main function to calculate time of arrival based on input steps and time in seconds
    """
    leaves = datetime.strptime(input("Enter the leaving time (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')

    steps = float(input("Enter the number of steps: ")) % 86400  # steps in seconds
    time_in_seconds = float(input("Enter the time in seconds for each step: ")) % 86400  # time in seconds for each step

    all_time = steps * time_in_seconds / 3600  # in seconds
    arrival_time = leaves + timedelta(hours=all_time)
    print("Time Arrival:", arrival_time.time())


if __name__ == "__main__":
    main()
