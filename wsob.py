import csv
import requests

api_url = 'http://balatro.virtualized.dev:4931/api/stats/leaderboard/1'
api_url2 = 'http://balatro.virtualized.dev:4931/api/stats/leaderboard/1?season=5'

response_s6 = requests.get(api_url)
response_s5 = requests.get(api_url2)
print("API responded")

s5 = list(response_s5.json().get('leaderboard'))
s6 = list(response_s6.json().get('leaderboard'))
data = [['Player','User ID', 'Score']]
table_path = 'main.csv'
number = 0
board = {}

for i in s5:
    board.update([(int(i.get('id')), float(i.get('peak_mmr')))])

for i in s6:
    c = board.get(int(i.get('id')), 0)
    if float(i.get('peak_mmr')) > c:
        board.update([(int(i.get('id')), float(i.get('peak_mmr')))])

for k, v in board.items():
    number += 1
    user_id = k
    mmr = v
    user = str('a') * number
    a = [user, user_id, mmr]
    data.append(a)
    print("User #" + str(number) + " recieved") 
    
print("Starting to write data...")
with open(table_path, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Finished!")
