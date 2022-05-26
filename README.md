# Predicting Star Wars the Clone Wars Episode Ratings

## Goal

This project examines the episode scripts of the tv series Star Wars the Clone Wars, in attempt to uncover insights about viewers preference for the tv series. 

The IMDB ratings for all Star Wars the Clone Wars episodes were scraped using the Beautiful Soup Python package from https://www.imdb.com/title/tt0458290/episodes133. The scripts for each episode were scraped from the website https://subslikescript.com/series/Star_Wars_The_Clone_Wars-458290 also using the Beautiful Soup Python package. 

The scripts will be analyzed utilizing lasso regression, multiple linear regression, and clustering to predict an episode's rating, given the terms present in an episode's script. 

## Model Fitting and Insights

The output from the multiple linear regression model suggests that an episode's IMDB rating can be predicted reasonably well based on its script. This multiple linear regression model contained 56 predictors, and these predictors were selected using a lasso regression model, which reduced the number of predictors from 39,602 terms down to just 56. It was necessary to utilize lasso regression to fit a multiple regression model since the 39,602 terms were more than the 133 episodes being analyzed. 

The Residual Standard Error for the multiple regression model was 0.2186. Interpreting the Residual Standard Error, the multiple regression model predicts an episode's rating with an average error of approximately 0.22. 

The coefficients with the highest magnitude from the model pertained to terms that indicated action scenes, as the terms 'clone trooper' and 'jedi' had relatively high coefficient values. This suggests that Star Wars fans might be attracted to the franchise for its action scenes, clone troopers and jedi 


## Navigating this repository

The files 'ep_scripts.json' and 'eps_df.csv' contain the episode scripts data and the episode ratings data that was analyzed for the purposes of this project. The files'get_episode_scripts.py' and 'get_eps_data.py' are the scripts used to scrape the episode scripts and the episode ratings data. 

The two remaining files in the depository are the report that is more detailed about how the project was conducted and the R Markdown file that contains the code.


