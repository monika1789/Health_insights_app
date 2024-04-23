import requests
import csv
import pandas as pd
from data_analysis import *
import configparser

 
def get_data_from_api():
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    #  Read the configuration
    config.read('config.conf')
     
    url = config['API']['url']
    app_token = config['API']['app_token']

    headers = {
        'Accept': 'application/json',
        'X-App-Token': app_token
    }

    response = requests.get(url, headers=headers)
    print (response)
   
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data from the API")
        return None
  
# Function to Parse the data
def extract_information(data):
    relevant_information = []
    for entry in data:
        year = entry['year']
        zone = entry['zone']
        sex = entry['sex']
        age_group = entry['age_group']
        population = entry['population']
        hypertension_count = entry['hypertension_count']
        prevalence_rate = entry['prevalence_rate']
        
        relevant_info_entry = {
            'year': year,
            'zone': zone,
            'sex': sex,
            'age_group': age_group,
            'population': population,
            'hypertension_count': hypertension_count,
            'prevalence_rate': prevalence_rate
        }
        relevant_information.append(relevant_info_entry)
    
    return relevant_information

# Function to save data into CSV file
def save_to_csv(data, filename='data.csv'):
    fieldnames = ['year', 'zone', 'sex', 'age_group', 'population', 'hypertension_count', 'prevalence_rate']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

# Main Function Calling Other Functions
def main():
    data = get_data_from_api()
    if data:
        relevant_information = extract_information(data)
        save_to_csv(relevant_information)
        print("Data saved to data.csv")
        analyze_and_visualize_data()  
    else:
        print("Failed to retrieve data from the API")

if __name__ == "__main__":
    main()
