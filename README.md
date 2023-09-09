# BikeShare Data Analysis

This Python script, `bikeshare.py`, allows users to explore bike-sharing data from three major cities in the United States: Chicago, New York City, and Washington. It provides various insights and statistics based on user input, such as city, month, and day.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Statistics](#statistics)
- [Viewing Raw Data](#viewing-raw-data)
- [Conclusion](#conclusion)

## Introduction

The Bikeshare Data Analysis script is designed to provide users with valuable information about bike-sharing patterns in different cities. Users can filter data by city, month, and day to obtain specific insights. This script utilizes the Pandas and NumPy libraries to perform data analysis and generate statistical summaries.

## Getting Started

Before you can start using the script, make sure you have the following prerequisites:

- Python 3.x installed on your computer.
- The Pandas and NumPy libraries installed. You can install them using pip:

  ```bash
  pip install pandas numpy
  ```

- The Bikeshare data files (`chicago.csv`, `new_york_city.csv`, and `washington.csv`) located in the same directory as the script.

## Usage

To get started with the Bikeshare Data Analysis, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where the `bikeshare.py` script is located.

3. Run the script using Python:

   ```bash
   python bikeshare.py
   ```

4. Follow the prompts to specify the city, month, and day for analysis.

## Statistics

The script provides the following statistical information:

- **Most Frequent Times of Travel:**
  - Most common month for bike rides.
  - Most common day of the week for bike rides.
  - Most common start hour for bike rides.

- **Most Popular Stations and Trip:**
  - Most commonly used start station.
  - Most commonly used end station.
  - Most frequent combination of start and end stations for trips.

- **Trip Duration:**
  - Total travel time (in seconds) for all trips.
  - Mean travel time (in seconds) for all trips.

- **User Statistics:**
  - Counts of user types (e.g., Subscribers, Customers).
  - Counts of gender (if available).
  - Earliest, most recent, and most common birth years (if available).

## Viewing Raw Data

The script also allows users to view raw data from the selected city's dataset. Users can choose to display rows of raw data in increments of 5. This feature is useful for exploring specific trip details.

## Conclusion

The Bikeshare Data Analysis script offers a convenient way to explore bike-sharing data, generate statistics, and gain insights into bike ride patterns in major U.S. cities. Users can customize their analysis by selecting the city, month, and day of interest. Enjoy exploring the world of bike-sharing!
