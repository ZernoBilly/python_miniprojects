seasons = ["Spring", "Summer", "Autumn", "Winter"]
# count = 1

# for season in seasons:
#     print(count, season)
#     count += 1

# for count in range(len(seasons)):
#     print(count + 1, seasons[count])

for count, season in enumerate(seasons, start=1):
    print(count, season)
