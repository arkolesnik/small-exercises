first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())
first_seconds_sum = first_hours * 3600 + first_minutes * 60 + first_seconds
second_seconds_sum = second_hours * 3600 + second_minutes * 60 + second_seconds
print(second_seconds_sum - first_seconds_sum)
