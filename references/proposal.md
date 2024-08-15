# Gamers be Gamin' Consulting
---

## Members

Ryan Ponticelli

Madison Outland

Nate Sheibley

Madison Bethke


### Due Date: 26/08/2024
---
# Proposal
At Gamers be Gamin' Consulting, our mission is to revolutionize the gaming industry by creating the next best video game that captivates players and sets new standards of excellence. To achieve this, we have partnered with expert data analysts who will leverage advanced analytics to identify the optimal genre, release date, and payment model. By harnessing data-driven insights, we aim to maximize profitability while delivering an unforgettable gaming experience that resonates with audiences worldwide. Our commitment is to blend creativity and innovation with strategic decision-making to craft a game that defines the future of entertainment.

## Questions
1. What game genre should we focus on to create a captivating and successful title?
	* split tag data in Steam Trends
	* process as revenues by tag
2. When is the optimal release date to effectively engage and capture our target audience?
	* group by quarterly/monthly release
	* process revenues by quarter/time
3. What payment model would maximize profitability for our upcoming game?
	* NLP of prev tag data? aggregate by DLC info?
4. How does twitch viewership correlate to profitability?
	* How does are profitability and twitch viewership correlated?

# Visualizations
1. What tags show up in the most profitable games 
	* avg profitability per tag. Bubble map where size of the bubble is profitability of the tag
2. profitability by quarter released
3. interactive visual of tag selection/ordering
4. from prev selection, associate summary stats of twitch viewers



## Data Sources:

Name| type| data| url
---|---|---|---
Steam Trends 2023 by @evlko and @Sadari|65000|release date, tags, review number, review avg, title, game id, launch price|[Steam Trends 2023](https://docs.google.com/spreadsheets/d/1D5MErWbFJ2Gsde9QxJ_HNMltKfF6fHCYdv4OQpXdnZ4/edit?gid=1714749788#gid=1714749788)
IGDB|api|Lots of meta-info, no $$ info, use to determine if dlc|[IGDB](https://api-docs.igdb.com/#website)
RAWG|api| Lots og meta-info, esp twitch related | [RAWG](https://api.rawg.io/docs/#operation/games_additions_list)

### data limitations
No individual sales data
