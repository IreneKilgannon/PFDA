#! /bin/bash
date
echo Downloading weather data
wget -O data/electricity/`date +"%Y%m%d_%H%M%S.csv"` https://www.smartgriddashboard.com/#roi
echo Weather data downloaded
date