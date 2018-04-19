import csv

video_path = "C:\\Users\\DrBrowntown\\Vimeo\\videos.csv"
video_file = open(video_path, newline='')
video_reader = csv.reader(video_file)

video_header = next(video_reader)

rate_path = "C:\\Users\\DrBrowntown\\Vimeo\\exchange_rates.csv"
rate_file = open(rate_path, newline='')
rate_reader = csv.reader(rate_file)

rate_header = next(rate_reader)

rate_data = []
for row in rate_reader:
    currency = str(row[0])
    exchange_rate_from_usd = float(row[1])

    rate_data.append([currency, exchange_rate_from_usd])

print(rate_data[0])


video_data = []
for row in video_reader:
    id = int(row[0])
    title = str(row[1])
    total_likes = int(row[2])
    total_purchases = int(row[3])
    unit_price_in_usd = float(row[4])    

    video_data.append([id, title, total_likes, total_purchases, unit_price_in_usd])

# print(video_data[0])

# Define valid writer
valid_path = "C:\\Users\\DrBrowntown\\Vimeo\\valid.csv"
valid_file = open(valid_path, 'w')
valid_writer = csv.writer(valid_file)
valid_writer.writerow(["Valid ID"])

# Define invalid writer
invalid_path = "C:\\Users\\DrBrowntown\\Vimeo\\invalid.csv"
invalid_file = open(invalid_path, 'w')
invalid_writer = csv.writer(invalid_file)
invalid_writer.writerow(["Invalid ID"])

total_cash = 0

# Sort valid and invalid ID's
for i in range(len(video_data)):
    
    row_data = video_data[i]
    vid_id = row_data[0]
    vid_title = row_data[1]
    vid_likes = row_data[2]
    vid_purchases = row_data[3]
    vid_purchases_USD = row_data[4]
    vid_purchases_euro = vid_purchases_USD * 0.838539

    if len(vid_title) < 30 and vid_likes > 10 and vid_purchases > 200 and vid_purchases_euro < 20:
        total_cash += vid_purchases_USD 
        valid_ID = vid_id   
      
        valid_writer.writerow([valid_ID])

    else:
        invalid_ID = vid_id
        invalid_writer.writerow([invalid_ID])
        

print ("Total value of valid videos is $"+ str(round(total_cash)))