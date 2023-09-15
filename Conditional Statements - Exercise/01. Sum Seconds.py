first = int(input())
second = int(input())
third = int(input())

total_time = first + second + third
time_minutes = total_time // 60
time_seconds = total_time % 60
if time_seconds < 10:
    print(f"{time_minutes}:0{time_seconds}")
else:
    print(f"{time_minutes}:{time_seconds}")