import requests
from bs4 import BeautifulSoup
import csv
import re


# Get input date from the user
date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")

# Get input date from the user and validate the format
while True:
    input_date = input("Please enter a date on this format MM/DD/YYYY: ")
    if re.match(date_pattern, input_date):
        break
    else:
        print("Invalid date format. Please enter the date in MM/DD/YYYY format.")

# Construct the URL with the input date

# Construct the URL with the input date
url = requests.get(f"https://www.yallakora.com/match-center/matchesclipAll?date={input_date}")

def main(url):
    # Fetch the HTML content from the URL
    src = url.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    # Find all championships in the HTML
    championships = soup.find_all("div", {"class": "matchCard"})
    
    def get_match_info(championships):
        # Extract championship title
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("li")
        num_of_matches = len(all_matches)
        
        for i in range(num_of_matches):
            # Extract teams' names
            team_a = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            team_b = all_matches[i].find("div", {"class": "teamB"}).text.strip()

            # Extract match result or note if match not played
            match_result = all_matches[i].find("div", {"class": "MResult"}).find_all("span", {"class": "score"})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # Extract match time 
            match_time = all_matches[i].find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()

            # Extract match status
            match_status = all_matches[i].find("div", {"class": "matchStatus"}).find("span").text.strip()
            
            # Extract channel
            channel_element = all_matches[i].find("div", {"class": "channel"})
            if channel_element:
                channel = channel_element.text.strip()
            else:
                channel = "No channel information available"
            
            # Add match info to matches_details
            matches_details.append({"البطولة": championship_title, "الفريق الأول": team_a, "الفريق الثاني": team_b, 
                                    "ميعاد المباراة": match_time, "النتيجة": score, "حالة المباراة": match_status, 
                                    "القناة": channel})
    
    # Process each championship
    for i in range(len(championships)):
        get_match_info(championships[i])
        
    # Define CSV column names
    keys = matches_details[0].keys()

    # Write data to CSV file
    with open("D:/webscraping/matches_details.csv", 'w', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)

# Execute the main function
main(url)
