#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:13:18 2022

This python script scrapes the idmb ratings of the TV Series Star Wars The Clone Wars
and other metadata associated with the episodes

@author: cyrusjackson
"""


# import libraries
from requests import get
from bs4 import BeautifulSoup
import pandas as pd


def main():
    # Populate empty list to store each episode's data
    all_eps = []

    # Loop through all 7 seasons
    for sn in range(1, 8):
        '''get html content of the season's episodes'''
        response = get(
            'https://www.imdb.com/title/tt0458290/episodes?season=' + str(sn))

        # Parse content
        page_html = BeautifulSoup(response.text, 'html.parser')

        # episode containers with each episode's data
        episode_containers = page_html.find_all('div', class_='info')

        # For each episode in each season
        for episode in episode_containers:
            # get season, convert from string to integer
            season = int(sn)
            # get episode number, convert from string to integer
            episode_number = int(episode.meta['content'])
            # get title of episode
            title = episode.a['title']
            # get episode's rating, convert from string to float
            rating = float(episode.find(
                'span', class_='ipl-rating-star__rating').text)
            # list with episode data
            episode_data = [season, episode_number, title, rating]
            # list of each episode's data
            all_eps.append(episode_data)

    # data frame with each episode's data
    eps_df = pd.DataFrame(
        all_eps, columns=['season', 'episode_number', 'title', 'rating'])
    # export dataframe to csv
    df_out = eps_df.to_csv('eps_df.csv', index=False)
    return df_out


main()
