# Gamers be Gamin' Consulting

Brian purpose of proj

proj 1 trying to teach amethodogy to argu a point.

The workflow for proj 2 is the focus

The thing that we care about is the process. Extarct, load, transform, visualize, communicate insights. 

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
1. What game genre should we focus on to create a captivating and successful title?
	* split tag data in Steam Trends
	* process as revenues by tag
2. When is the optimal release date to effectively engage and capture our target audience?
	* group by quarterly/monthly release
	* process revenues by quarter/time
3. What payment model would maximize profitability for our upcoming game?
	* NLP of prev tag data? aggregate by DLC info?
	* Pick a different Q if you want to
4. How are twitch viewership correlate to profitability?
	* How does are profitability and twitch viewership correlated?
	* How does twitch viewers correlate to total revenue
	* How does twitch viewers correlate to review totals
	
### Reduce scope
Q1 - MadB Nate
Q4 - MadO Ryan
One hot encoding of tags.


## Presentation Outline
Task order | Story beat | Assigned to
---|---|---
1| Presentation introduction Tell them what we are going to present (short) | Ryan MadO
2| why do our investors care about twitch data (and revenue, but that's obv) | Ryan MadO
3| how we measure these, what are we measuring| Nate MadB
4| what is our data, what features did we engineer | Nate MadB
5| interactable bar chart, revenue by tags | Nate MadB
6| bubble chart of revenue top... 30-50(?) tags |  Nate MadB
7| twitch data for engagement and product promotion | Ryan MadO
8| twitch viewer count to review count correlation x=review_count y=twitch_count size=revenue | Ryan MadO
9| twitch viewer count by tag/genre. interactible, select from top 30-50(?) tags |  Ryan MadO
10| conclusion - reiterate insights | MadB? Nate
---
## Action items from Aug15
Person | Action Item | timeline
---|---|---
MadO| Find Twitch data| Fri
Nate| make tag split csv data, clean it| Mon
Nate| load into SQlite| Fri
MadB Nate| do revenue column feature add, document how | Fri?
Ryan| Make API requests for twtich data| Sat?
Ryan| join twitch data to cleaned steamd data| Mon?
MadB| Skeleton of presentation| Mon
MadO| Have birthday Fun| Mon 

### File organization
Keep descriptive names!!
One notebook loads a piece of data, generates a change, saves to a new file
eg. load raw, process, save to clean
eg. Load clean data, make plots, save images

---

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

---
