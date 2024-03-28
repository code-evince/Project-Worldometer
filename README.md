repository link = https://github.com/code-evince/Project-Worldometer

module_wikipedia

module_worldometer

# Contributers 

Bishnu Prasad Nayak 23CS60R28 (code-evince)

Chaitanya Kale 23CS60R29 (ChaitanyaKale)

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



