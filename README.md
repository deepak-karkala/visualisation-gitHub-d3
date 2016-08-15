# Visualisation of popular GitHub repositories using d3.js

This article aims to study the most popular GitHub repositories over the last five years. The entire GitHub archive is available as a public dataset on Google BigQuery.  The data for this work was obtained using SQL queries on this dataset. In order to create the plots, d3.js is used. d3 is a JavaScript library for visualising data using web standards. d3 is one of the most popular visualising techniques and uses SVG, Canvas and HTML.

In this work, the number of forks is considered as a measure of the popularity of repositories. This is certainly not the best method, but will hopefully give us some insight into the most popular repositories. The data considered in this work spans over the last five years.

The project aimed to answer the following questions using visualisations: 
1. Increase in GitHub usage
2. Most popular repositories over the last 5 years
3. 10 Most popular repositories of 2015