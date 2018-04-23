import csv
import errno
import sys
import os


# CSV reader for videos.csv
def videos_csv_reader(video_data, local_machine_path):
    """Open's videos.csv, reads each line, and
    appends them to the video_data list"""
    try:
        video_path = os.path.join(local_machine_path, "videos.csv")
        video_file = open(video_path)
        video_reader = csv.reader(video_file, strict=True)
        video_header = next(video_reader)

        for row in video_reader:
            id = int(row[0])
            title = str(row[1])
            total_likes = int(row[2])
            total_purchases = int(row[3])
            unit_price_in_usd = float(row[4])

            video_data.append([
                id,
                title,
                total_likes,
                total_purchases,
                unit_price_in_usd
                ])

        video_file.close()
        return video_data

    except ValueError as e:
        print(
            'Invalid value in videos.csv.' +
            'Must be float or integer. Error:{0} '.format(e))


# CSV reader for exchange_rates.csv
def exchange_rate_csv_reader(rate_data, local_machine_path):
    """Open's exchange_rates.csv using the folder file path in local_machine_path,
    reads each line, and appends them to the rate_data list"""
    rate_path = os.path.join(local_machine_path, "exchange_rates.csv")
    rate_file = open(rate_path)
    rate_reader = csv.reader(rate_file, strict=True)
    rate_header = next(rate_reader)

    for row in rate_reader:
        currency = str(row[0])
        exchange_rate_from_usd = float(row[1])

        rate_data.append([currency, exchange_rate_from_usd])

    rate_file.close()
    return rate_data


# Sorts the video.csv into two csv's of valid and invalid csv's
def sort_valid_and_invalid_videos(video_data, rate_data, local_machine_path):
    """Pulls in appended video_data and rate_data, along with
    the folder path in local_machine_path. Runs
    convert_USD_to_CAD_exchange_rate to pull in defined exchange rate.
    Defines a valid and invalid csv writer, followed by which rows
    should be checked. Finally an if statement is used for filtering
    by the rules defined. The csv writer will then write new rows
    in the invalid and valid csv's if they pass or fail the
    filtering rules. Finally, a print statement will display in the
    terminal window the total doller value of the valid videos in
    videos.csv"""
    total_cash = 0
    CAD_exchange_rate = convert_USD_to_CAD_exchange_rate(rate_data)
    vid_purchases_conversion = 0
    
    path_to_valid_writer = valid_csv_writer(local_machine_path)
    
    path_to_invalid_writer =  invalid_csv_writer(local_machine_path)    

    # Sort valid and invalid ID's
    for i in range(len(video_data)):
        # Define the rows to be checked
        row_data = video_data[i]
        vid_id = row_data[0]
        vid_title = row_data[1]
        vid_likes = row_data[2]
        vid_purchases = row_data[3]
        vid_purchases_USD = row_data[4]
        vid_purchases_conversion = vid_purchases_USD * CAD_exchange_rate

        # Filtering rules
        if (len(vid_title) < 30 and
                vid_likes > 10 and
                vid_purchases > 200 and
                vid_purchases_conversion < 25):
            # Adds each valid video to the cash total and its ID to valid.csv
            total_cash += vid_purchases_USD
            valid_ID = vid_id
            path_to_valid_writer[0].writerow([valid_ID])
        # Videos taht fail the filtering are placed in invalid.csv
        else:
            invalid_ID = vid_id
            path_to_invalid_writer[0].writerow([invalid_ID])

    # If vid_purchases_conversion is 0, the tool could not access exchange_rate
    if (vid_purchases_conversion == 0):
            total_cash = 0
            print('Unable to find currency conversion rate')
    # If total_cash is 0, no valid videos were found
    if (total_cash <= 0):
        print("Unable to find any valid videos with a cash value.")
    else:
        print ("Total US dollar value of valid videos is ${0}"
               .format(round(total_cash)))

    path_to_valid_writer[1].close()
    path_to_invalid_writer[1].close()


# Converts USD to CAD
def convert_USD_to_CAD_exchange_rate(rate_data):
    """Open's rate_data list, reads each line, searches for
    CAD(canandian exchange rate), and
    returns that rate in CAD_exchange_rate"""
    CAD_exchange_rate = 0
    # Pull in conversion rates
    for i in range(len(rate_data)):
        ex_data = rate_data[i]
        rate_currency = ex_data[0]
        rate = ex_data[1]

        if rate_currency == "CAD":
            CAD_exchange_rate = rate

            return CAD_exchange_rate


# Define valid writer
def valid_csv_writer(local_machine_path):

    valid_path = os.path.join(local_machine_path, "valid.csv")
    valid_file = open(valid_path, 'w')
    valid_writer = csv.writer(valid_file)
    valid_writer.writerow(["Valid ID"])

    return [valid_writer, valid_file]


# Define invalid writer
def invalid_csv_writer(local_machine_path):
    
    invalid_path = os.path.join(local_machine_path, "invalid.csv")
    invalid_file = open(invalid_path, 'w')
    invalid_writer = csv.writer(invalid_file)
    invalid_writer.writerow(["Invalid ID"])

    return [invalid_writer, invalid_file]


# Bundles the other functions and gives the folder file path
def main():
    """This function will initiate the all others"""
    try:
        local_machine_path = os.getcwd()
        rate_data = []
        video_data = []
        videos_csv_reader(video_data, local_machine_path)
        exchange_rate_csv_reader(rate_data, local_machine_path)
        sort_valid_and_invalid_videos(
            video_data,
            rate_data,
            local_machine_path)

    except FileNotFoundError as e:
        print(e)

main()
input("Press enter to exit ")
