# Gamers be Gamin' Consulting

Brian purpose of proj

Proj 1 trying to teach amethodogy to argue a point.

The workflow for proj 2 is the focus.
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

which tags yield the highest engagement measured by viewership and positivity
Gamers be Gamin' Consulting is examining twitch vs review data. Correlation between genre tags and highest viewer engagement vs review standpoint.
Is there a genre with a discrepancy between viewership and reviews?

Target: What tags can we present as "the bestest"
Metrics for "the bestest": 
* review positivity (satisfaction)
* highest twitch average viewers? (player retention proxy)
* percentile breakdown of...
* sythecize a single numeric metric from 1-2
	* review positive * 0.5 + twitch_viewership * 0.5 normalized to max 1
* bad pr in videogames can do so much. Helldivers 2 example

We have:

Aggregate review and twitch data

monthly top 200 twitch data

USE AVG_HOURS_STREAM**ED** not viewership
* provides the clearest relationship

### New presentation (needs to be rebuilt again)
Task  | Story beat | Assigned to
---|---|---
Steam is a online games store like yelp. Twitch is a platform to watch folks live stream games with commentary and interaction| Set the stage of what steam and twitch are | Nate MadB
Case study on hell divers | huge positive release, mismanagement to rapid obscurity | MadO
Case study on hunt showdown| initial flop, adjusted target demographics and growth over years | Nate?
2 vis. Top 10 games on twitch visualization. Tag freq table| which genre our game should be based on frequency table of tags|?
"After data exploration we discovered xyz tags are most prolific in top 10 of hours_streamed" | **Transition to DEMO** |  Nate MadB
describe bar chart and significance | describe avg_hours_streamed as primary metric w/ bar chart | Ryan MadO
describe bubble chart bubblename=title, bubblesize=hours_streamed, bubblecolor=positivity. display all of top 30% viewership? popup?| shows competator games. Shows market saturation. number of competators | Ryan MadO
top ten twitch viewership by month. only last x years. only displays top 5/10 from list| displays what we talked about in the case studies |  Ryan MadO
Should invest in xyz genre if targetting highest longevity of game measured by twitch| conclusion | MadB? Nate
Q&A?

### steam pros
* private company compared to others
* ease of access is huge: buy, install, play. easy to navigate
* discovery queue, caters to person and makes recs based off library, integrates live streams into rec'd games as well which is a great tool for developers
* refund policies are good, marketplace is good, security like MFA is great
* they were a games first company, they developed before turning into a marketplace

### twitch pros
* wide reach
* dominance in live streaming
* most streamers use steam as it is great for discovering, installing and 
* playing games quickly
* real-time engagement
* community building

---
# Minutes and action items
---
## 08/22/24
## Minutes
rebuild presentation outline _again_
## Action Items

---

## 08/21/24

### Minutes
Revisit presentation table

Mayhaps do a case study on helldivers 2?

Case study on 1 game. importance of twitch as an indicator for long term interest and sustained growth of audiance. 

correlation with steam review data which may be more intuitive
xyz tags  are best tags.

2 case studies.

Helldivers - huge positive release, mismanagement to rapid obscurity

Hunt Showdown - initial flop, adjusted target demographics and grew over years

bubble chart where you can select bubbles and it displays overlay bar chart of binned histo

we can make a statement like: after some data exploration we decided xyz tags are most prolific in top 10-50-100 and we'd like to show our dashboard 

### Elias:feedback

Hooked with case studies Hunt vs Helldivers

Pivotted away from those stories

If we don't have the data on hunt and helldivers, tell the story, if we have time later, add it in. What do we have support for when they engaged on twich

What maps to hunt to present an argument to hunt.

These are the features that show us what should work. Helldivers should have these features, but failed.

These metrics were really good at predicting things failed for helldivers.

Bring in our data and predictions of what should be good. hypothesis trends in tags. hours streams and reviews. define a sucessful game.

Case Study Hell Divers. They failed, but should have succeeded by our metrics.  
Case Study Hunt showdown. Increase in focus on interactivity on twitch. 

Focusing on fanbase and communication tha matters.

If time. If look at new thing the model fits better.

closing statement - how many of you looked up hunt showdown if more than hunt showdown that is why we believe community engagement matters a lot

### Action Items
Person | Action Item | timeline
---|---|---
MadB|Readme |?
MadB|skeleton of presentation|?
Ryan|look up when hunt showdown started to do twitch promotion. dev streams? identify spikiness. build a dataset.|class thurs
Nate|look at tag similarity between helldivers and hunt|class thurs
Nate|top 10 + helldivers and hunt hours_streamed vs review percentage|class thurs
MadO| make brainstorm on what to say about relationship of reviews and hours_streamed to a sucessful product with longevity| class thurs




---

## 08/19/24
### Minutes
How to merge twitch data(game-yearly) into single row aggregate steam data.
Drop revenue. compare review total and positivity to twitch, not rev
make a dashboard type github pages webapp with our 4? graphs and a tag selection thingy

EndGoal : webpage (github) with 3 tags + metric(twitch, review_total, positivity) selection. Displays a list of games (desc) of that metric. + 2-3 plots

sum of total hours, sum hours streamed, avg streamers, avg viewers, avg channels.
bubble and twitch summary stats 
after join have at most 2k games. cut everything prior to date(2018?)
line chart is 2018-2023 
sums/avgs are 2018-2023
list release date on game list on left

Use flask to localhost a visualization

### Action Items
Add data sources for new twitch data
make tags+steam sqlite db 
Make api functions for selecting tags and querying db

Person | Action Item | timeline
---|---|---
MadO| Make basic flask webpage up| Tuesday
MadO| Make html tags for the plots and dropdowns etc | Tuesday
Ryan| inner join steam and twitch summary statistics| Tuesday
Nate| make and load sqlitedb of tag, steam+twitch, and twitch yearly dat|tuesday night
Nate| build sqlalchemy/flask functions for bubble graph| Wed
MadO| build sqlalchemy/flask functions for twitch summary stats| Wed
Ryan| build sqlalchemy/flask functions for 2018-2023 twitch line graph| Wed
Ryan| Edit presentation outline| before class Wed

---

## 08/15/24
### Minutes
Presentation outline made

### Action items
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
5. build flask app and visualization dashboard using altair
6. Presentation
	1. storyline pitch
	2. if cut and try we may have too much scope, narrow down to Q 1 and 4?
	
---

# Dataset Description


# Tools and Tech
Character_normalizer

# Data Sources:

Name| type| data| url
---|---|---|---
Steam Trends 2023 by @evlko and @Sadari|65000|release date, tags, review number, review avg, title, game id, launch price|[Steam Trends 2023](https://docs.google.com/spreadsheets/d/1D5MErWbFJ2Gsde9QxJ_HNMltKfF6fHCYdv4OQpXdnZ4/edit?gid=1714749788#gid=1714749788)
IGDB|api|Lots of meta-info, no $$ info, use to determine if dlc|[IGDB](https://api-docs.igdb.com/#website)
RAWG|api| Lots og meta-info, esp twitch related (paid only) | [RAWG](https://api.rawg.io/docs/#operation/games_additions_list)

### data limitations
No individual sales data
Limited time frames of twitch data

---
