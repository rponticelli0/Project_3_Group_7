# Gamers be Gamin' Consulting
---

### Due Date: 26/08/2024
---
# Project Overview (WIP-be ready to pivot)
At Gamers be Gamin' Consulting, our mission is to revolutionize the gaming industry by creating the next best video game that captivates players and sets new standards of excellence. To achieve this, we have partnered with expert data analysts who will leverage advanced analytics to identify the optimal genre, release date, and payment model. By harnessing data-driven insights, we aim to maximize profitability while delivering an unforgettable gaming experience that resonates with audiences worldwide. Our commitment is to blend creativity and innovation with strategic decision-making to craft a game that defines the future of entertainment.

## Project Team 7

Ryan Ponticelli

Madison Outland

Nate Sheibley

Madison Bethke

---
# Key Tasks and Components

## Goals
1. **Data exploration:** Analyze the dataset to determine what features we can synthesize to answer the Qs we postulated. 
2. **Hypothesis Development:** Establish a hypothesis based around our understandings of the industry and the face we are only doing steam games.
3. **Mystical Magical INSIGHTS** 
4. **Visualizations:** Intuitively demonstrate the insights we generate.
5. **Presentation:** Outline the presentation before working on data and code. 

## Questions
1. Nate - What game genre should we focus on to create a captivating and successful title?
	* split tag data in Steam Trends
	* process as revenues by tag
2. Ryan - When is the optimal release date to effectively engage and capture our target audience?
	* group by quarterly/monthly release
	* process revenues by quarter/time
3. MadB? - What payment model would maximize profitability for our upcoming game?
	* NLP of prev tag data? aggregate by DLC info?
	* Pick a different Q if you want to
4. MadO -How are twitch viewership correlate to profitability?
	* How does are profitability and twitch viewership correlated?
	* How does twitch viewers correlate to total revenue
	* How does twitch viewers correlate to review totals

## Procedure
1. Data Exploration
	* Load from csv
	* handle missing data
	* explore API results
2. Data Processing and feature engineering
 	* create new features from existing data (revenue, join api data)
3. Database integration
	* Joined data added through python
	* access with python for further querying 
	* MAYBE use flask and github pages to make interactive tag sorting bubble chart or other interactive plots
	* Can we use sqlite? Spin up Postgres local? DuckDB? 
4. Visualzatize the data to resolve the questions above
	1. What tags show up in the most profitable games 
		* avg profitability per tag. Bubble map where size of the bubble is profitability of the tag
	2. profitability by quarter released
	3. interactive visual of tag selection/ordering
	4. from prev selection, associate summary stats of twitch viewers
5. Presentation
	1. storyline pitch
	2. if cut and try we may have too much scope, narrow down to Q 1 and 4?
	

---

# Dataset Description


# Tools and Tech


# Data Sources:

Name| type| data| url
---|---|---|---
Steam Trends 2023 by @evlko and @Sadari|65000|release date, tags, review number, review avg, title, game id, launch price|[Steam Trends 2023](https://docs.google.com/spreadsheets/d/1D5MErWbFJ2Gsde9QxJ_HNMltKfF6fHCYdv4OQpXdnZ4/edit?gid=1714749788#gid=1714749788)
IGDB|api|Lots of meta-info, no $$ info, use to determine if dlc|[IGDB](https://api-docs.igdb.com/#website)
RAWG|api| Lots og meta-info, esp twitch related | [RAWG](https://api.rawg.io/docs/#operation/games_additions_list)

### data limitations
No individual sales data
