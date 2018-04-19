import csv
import errno
import os



# Please add videos.csv filepath
video_path = "C:\\Users\\DrBrowntown\\Vimeo\\videos.csv"
# Please add exchange_rates.csv filepath
rate_path = "C:\\Users\\DrBrowntown\\Vimeo\\exchange_rates.csv"
# Please add valid.csv filepath
valid_path = "C:\\Users\\DrBrowntown\\Vimeo\\valid.csv"
# Please add invalid.csv filepath
invalid_path = "C:\\Users\\DrBrowntown\\Vimeo\\invalid.csv"


# CSV reader for videos.csv
def videos_csv_reader(video_list):
    try:
        video_file = open(video_path, newline='')
        video_reader = csv.reader(video_file, strict=True)
        video_header = next(video_reader)

        for row in video_reader:
            id = int(row[0])
            title = str(row[1])
            total_likes = int(row[2])
            total_purchases = int(row[3])
            unit_price_in_usd = float(row[4])

            video_list.append([
                id,
                title,
                total_likes,
                total_purchases,
                unit_price_in_usd
                ])

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(
            'Invalid value in videos.csv. Must be float or integer. Error: ' +
            str(e))


# CSV reader for exchange_rates.csv
def exchange_rate_csv_reader(rate_list):
    try:
        rate_file = open(rate_path, newline='')
        rate_reader = csv.reader(rate_file, strict=True)
        rate_header = next(rate_reader)

        for row in rate_reader:
            currency = str(row[0])
            exchange_rate_from_usd = float(row[1])

            rate_list.append([currency, exchange_rate_from_usd])

    except FileNotFoundError as e:
        print(e)


# Sorts the video.csv into two csv's of valid and invalid csv's
def sort_valid_and_invalid_videos(video_list, rate_list):

    total_cash = 0
    CAD_exchange_rate = 0
    vid_purchases_conversion = 0
    # Define valid writer
    valid_file = open(valid_path, 'w')
    valid_writer = csv.writer(valid_file)
    valid_writer.writerow(["Valid ID"])

    # Define invalid writer
    invalid_file = open(invalid_path, 'w')
    invalid_writer = csv.writer(invalid_file)
    invalid_writer.writerow(["Invalid ID"])

    # Pull in conversion rates
    for i in range(len(rate_list)):
        ex_data = rate_list[i]
        rate_currency = ex_data[0]
        rate = ex_data[1]

        if rate_currency == "EUR":
            EUR_exchange_rate = rate

        elif rate_currency == "CAD":
            CAD_exchange_rate = rate

    # Sort valid and invalid ID's
    for i in range(len(video_list)):
        # Define the rows to be checked
        row_data = video_list[i]
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
            valid_writer.writerow([valid_ID])
        # Videos taht fail the filtering are placed in invalid.csv
        else:
            invalid_ID = vid_id
            invalid_writer.writerow([invalid_ID])

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


def main():
    rate_list = rate_data = []
    video_list = video_data = []
    videos_csv_reader(video_list)
    exchange_rate_csv_reader(rate_list)
    sort_valid_and_invalid_videos(video_list, rate_list)

main()
