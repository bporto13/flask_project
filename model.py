import requests
import random

bbcard = []

# only if the player is active

def get_player_gif(name):
    gif_num = random.randint(0,10)
    GIPHY = "rhdH6aZFvknwMQN55nQ0TgJgu4TWJTsg"
    gif = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key=rhdH6aZFvknwMQN55nQ0TgJgu4TWJTsg&q='{name}%'&limit=11&offset=0&rating=G&lang=en").json()
    player_gif = gif["data"][gif_num]["images"]["downsized"]["url"]
    return player_gif


def get_player_info(status, name):
    # for i in range(0, 3):
    if status.lower() == "active":

        playerName = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name.lower()}%'&search_player_all").json()

        pName = playerName["search_player_all"]["queryResults"]["row"]["name_display_first_last"]
        
        return pName

# decides what info to give for the player absed on input


def get_player_team(name, stat1Choice, stat2Choice,stat3Choice):
    if stat1Choice == "1" or stat2Choice == "1" or stat3Choice =="1" :
        playerName = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name.lower()}%'&search_player_all").json()

        team = playerName["search_player_all"]["queryResults"]["row"]["team_full"]

        return team
    else:
        return "(You did not choose this statistic)"


def get_player_number(name, stat1Choice, stat2Choice,stat3Choice):
    if stat1Choice == "2" or stat2Choice == "2" or stat3Choice =="2" :
        playerName = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name.lower()}%'&search_player_all").json()

        ID = playerName["search_player_all"]["queryResults"]["row"][
            "player_id"]

        playerDetail = requests.get(
        f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{ID}'").json()

#             # print(playerDetail)

        jerseyNum = (playerDetail["player_info"]
                 ["queryResults"]["row"]["jersey_number"])

#             # print(jerseyNum)
        return jerseyNum
#             bbcard.append(jerseyNum)
    else:
        return "(You did not choose this statistic)"


def get_player_home(name, stat1Choice, stat2Choice,stat3Choice):
    if stat1Choice == "3" or stat2Choice == "3" or stat3Choice =="3" :
        playerName = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name.lower()}%'&search_player_all").json()

        born = playerName["search_player_all"]["queryResults"]["row"]["birth_country"]

#                 # print(born)
        return born
#                 bbcard.append(born)
# s
    else:
        return "(You did not choose this statistic)"



def get_player_position(name, stat1Choice, stat2Choice,stat3Choice):
    if stat1Choice == "4" or stat2Choice == "4" or stat3Choice =="4" :
        playerName = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name.lower()}%'&search_player_all").json()
        position = playerName["search_player_all"]["queryResults"]["row"][
            "position"]
        return position
    else:
        return "(You did not choose this statistic)"

#         # #If player is retired
#         if status.lower() == "retired":

#             playerName = requests.get(
#                 f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='N'&name_part='{player.lower()}%'&search_player_all"
#             ).json()

#             pName = playerName["search_player_all"]["queryResults"]["row"][0]["name_display_first_last"]
#             # print(player)

#             # ask what they want to know about a player
#             data2 = input(
#                 "\nWhat 3 items would you like to be printed on the baseball card?\n\n1)Last team they played for\n2)Jersey number\n3)Where they are from\n4)Position\n\n"
#             )

#             if data2 == '1':

#                 team = playerName["search_player_all"]["queryResults"]["row"][0][
#                 "team_full"]

#                 bbcard.append(team)

#             # print (team)

#             elif data2 == '2':

#                 ID = playerName["search_player_all"]["queryResults"]["row"][0][
#                 "player_id"]

#                 # print(ID)

#                 playerDetail = requests.get(
#                   f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{ID}'"
#             ).json()

#                 jerseyNum = (playerDetail["player_info"]["queryResults"]["row"]
#                          ["jersey_number"])

#                 bbcard.append(jerseyNum)

#                 # print(jerseyNum)

#             elif data2 == '3':

#                 born = playerName["search_player_all"]["queryResults"]["row"][0][
#                 "birth_country"]

#                 # print(born)
#                 bbcard.append(born)

#             elif data2 == '4':

#                 position = playerName["search_player_all"]["queryResults"]["row"][
#                 0]["position"]

#                 bbcard.append(position)

#                 # print (position)
