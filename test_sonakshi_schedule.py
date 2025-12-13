import datetime
import sys
import os

# Change to Sonakshi's directory
os.chdir('D:/py/ip-project/Sonakshi Rohliyan')

# Test schedule logic
blue = []
f = open('metro_data.txt', 'r')
for line in f.readlines():
    stripped_line = line.strip()
    if not stripped_line or stripped_line.startswith('Line,'):
        continue
    Line, Current_station, Time_for_next_station = stripped_line.split(', ')
    if Line == 'Blue_common':
        blue.append(Current_station)
        blue.append(int(Time_for_next_station))
f.close()

# Test metro_sim logic
station = 'Rajiv Chowk'
timee = '09:18'
t = 0
index = blue.index(station)
for i in range(1, index, 2):
    t = t + blue[i]

print(f'Travel time from start to {station}: {t} minutes')

# Calculate first metro arrival
first_metro = datetime.datetime.strptime('06:00', '%H:%M') + datetime.timedelta(minutes=t)
print(f'First metro arrives at {station}: {first_metro.strftime("%H:%M")}')

# Generate times (simulating the full schedule)
times = []
start_time = first_metro
end_time = datetime.datetime.strptime('08:00', '%H:%M')
while start_time <= end_time:
    times.append(start_time.strftime('%H:%M'))
    start_time = start_time + datetime.timedelta(minutes=8)

start_time = datetime.datetime.strptime('08:00', '%H:%M')
end_time = datetime.datetime.strptime('10:00', '%H:%M')
while start_time <= end_time:
    times.append(start_time.strftime('%H:%M'))
    start_time = start_time + datetime.timedelta(minutes=4)

# Find next metro after 09:18
for i in range(0, len(times)):
    if times[i] >= timee:
        print(f'\nNext metro at {station} after {timee}: {times[i]}')
        print(f'Next 5 metros: {times[i+1:i+6]}')
        break
