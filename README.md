repository link = https://github.com/code-evince/Project-Worldometer

```bash
python3 main.py
```
module_wikipedia

module_worldometer

# Contributers 

Bishnu Prasad Nayak 23CS60R28 (code-evince)

Chaitanya Kale 23CS60R29 (ChaitanyaKale7)

Ayush Shakya 23CS60R26 (code-edge7)


![Screenshot 2024-03-29 040733](https://github.com/code-evince/Project-Worldometer/assets/38295546/d6cfb918-71e6-4341-af20-45ee92267df9)

# MODULE WORLDOMETER


menu.py - driver file of this module

getWorld.py - uses the worldometer.py to scrape the main worldometer page

getData.py - scrapes the country page and calls 3 other modules getActiveCases.py, getDailyDeaths.py and getRecovered_NewCases.py to scrape the country data 

worldometer.py - uses ply to scrape the covid worldometer table

getActiveCases.py - uses ply to scrape the country covid page of a given country and retrives the active cases

getDailyDeaths.py - uses ply to scrape the country covid page of a given country and retrives the daily deaths

getRecovered_NewCases - uses ply to scrape the country covid page of a given country and retrives the newly recovered cases and new cases

# Mapper, Combiner, and Reducer for COVID-19 Data Analysis

This project implements a Mapper-Combiner-Reducer workflow to analyze COVID-19 data. The workflow consists of three main components: Mapper, Combiner, and Reducer.

## Overview

- **Mapper**: The Mapper script reads data from the input file and selects particular columns based on the query provided as a command-line argument. It then passes the selected data to the Combiner.

- **Combiner**: The Combiner script receives data from the Mapper and performs the aggregation of cases. It combines the data based on the query and passes the sum and value to the Reducer.

- **Reducer**: The Reducer script receives aggregated data from the Combiner and calculates the sum. It then prints the output, providing the final result of the analysis.

## Usage

To run the workflow:


1. Run the module worldometer  with appropriate command-line arguments:
   ```bash
   python3 menu.py

![Screenshot 2024-03-29 043346](https://github.com/code-evince/Project-Worldometer/assets/38295546/7f533633-5f7f-4151-bfe1-560f929859b1)


# MODULE WIKIPEDIA COVID



## Module Description

This module crawls the wikipedia Coivid Timeline, extract all the world wide news, responses for all time. Further it parses specific countries and extract all its news.

## Folders and Files

checkCountriesCache.txt, checkResponsesCache.txt, checkTimelinesCache.txt - These files contain the time when all the websites of countries, responses and timelines respectively were parsed. These websites are parsed only when it has been parsed in the last 24 hours. Thus it leads to faster execution and performance time.

CovidNewsTxt - Contains text files we get after parsing Countries, Responses and Timelines webpages.
Format of text file: 'Date::News'

Webpages - Contains the webpages of countries, responses and timelines

menu2.py - contains menu for Module Wikipedia

utilities - This folder contains the mapper, reducer and combiner used for addressing queries related to Country, Responses and Timelines

JaccardResults - Contains text files that stores news for all the countries for given time period. These files are then used for calculating Jaccard Score


