import pandas as pd 
import matplotlib.pyplot as plt

def analyze_and_visualize_data(filename='data.csv', save_folder = "images/"):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)

    # Display basic statistics
    print("Basic Statistics:")
    print(df.describe())

    # Calculate average prevalence rate
    avg_prevalence_rate = df['prevalence_rate'].mean()
    print("\nAverage Prevalence Rate:", avg_prevalence_rate)

    # Group by age group and calculate average prevalence rate for each age group
    avg_prevalence_by_age = df.groupby('age_group')['prevalence_rate'].mean()
    print("\nAverage Prevalence Rate by Age Group:")
    print(avg_prevalence_by_age)
    
    # Create a bar plot for average prevalence rate by age group
    plt.figure(figsize=(10, 6))
    avg_prevalence_by_age.plot(kind='bar', color='skyblue')
    plt.title('Average Prevalence Rate by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Prevalence Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_folder + 'prevalence_by_age_group.png')
    plt.show()
    
    # Group by zone and calculate average prevalence rate for each zone
    avg_prevalence_by_zone = df.groupby('zone')['prevalence_rate'].mean()
    print("\nAverage Prevalence Rate by Zone:")
    print(avg_prevalence_by_zone)   
    
    # Create a bar plot for average prevalence rate by zone
    plt.figure(figsize=(12, 6))
    avg_prevalence_by_zone.plot(kind='bar', color='lightgreen')
    plt.title('Average Prevalence Rate by Zone')
    plt.xlabel('Zone')
    plt.ylabel('Average Prevalence Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_folder + 'prevalence_by_zone.png') 
    plt.show()
    
    # Group by year and count the number of entries for each year
    df['year'] = df['year'].str[:4]
    # Take the first part, which represents the year

    year_counts = df['year'].value_counts()

    # Create a pie chart for distribution of data by year
    plt.figure(figsize=(8, 8))
    plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Data by Year')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig(save_folder + 'data_distribution_by_year.png')
    plt.show()
   
    
  