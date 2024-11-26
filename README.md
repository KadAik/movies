## The Site & User Behavior
We’re going to build a site that allows users to leave comments on movies. Well, we’re going to build some of it. We already saw, when building Blango, how to create a comment system, so we won’t build that part. We’re mostly going to focus on designing the models based on the data that OMDb returns, and discuss how to keep our data up to date. Let’s start by talking about the main use case we foresee.
A user will visit our site in order to comment on a movie, or read previous comments about a movie. When they visit the site, let’s assume they will begin by performing a search for that movie. How should this search operate?
If the user is performing a search for a title that is not in our database, then we’ll need to first find matching films on OMDb and use that to populate our database. Then we can query our own database and get results. Remember we should keep in mind that searching the local database is generally a lot faster than a remote API, and that it costs us (uses up API quota) every time a request is made to the API. However, we want to make sure our own database is (reasonably) up to date.
We’re going to solve this problem by keeping a record of search terms that have been used. We’ll only query the API if the search term hasn’t been searched for in the past 24 hours. Otherwise, we only search our local database.
Also notice in the API responses, the list response contains only some of the data (Title, Year, imdbID, Poster (URL) and Type), whereas the detailed response contains a lot more data. At this point, we need to decide if we want to store data that the detailed response contains, or if it’s only necessary to store list (summary) data.
In our case, we want to also store the plot and genre(s) of the movie, which means we’ll have to retrieve the detailed response too. This will allow us to display them on a movie detail page. In theory, it would also allow searching by these fields. However, those searches would have to go directly to our database. We can’t search OMDb by genre or plot, so we’d only be able to enable this once we have a fairly “decent-sized” database that gives reasonable results.
We need to consider how we go from summary results to detail results. In some applications, the detailed response might change over time. For example, if we were going to display the ratings of the movie, you could expect them to vary slightly over time. To get the latest rating values, you’d need to make sure that the movie data was re-fetched frequently to stay up to date, perhaps once a day or once a week. This would mean storing a last-fetched date/time and re-fetching after a certain period of time has elapsed since then.
Since we don’t expect any of our data to change, we’ll just store a flag to indicate if it’s the full record or not. If someone tries to view a movie that doesn’t have the full record we can go and fetch it in realtime, and expect it not to ever need to be updated.
With all that considered, here’s how the flow would work:
A user performs a search query on our site.
If it has been more than 24 hours since we’ve queried the API for that search term, re-fetch results.
Each result returned will be stored in our database with the is_full_record flag set to False.
We’ll query our local database using the search term.
A list of results will be displayed.
When the user visits the detail page for a movie, we’ll check the is_full_record flag.
If it’s False, we’ll query the API to get the full data.
The data that’s displayed is fetched from our local database.
We’ll go into each step in more detail as we build the site. Next we’ll look at modeling the movie data in Django.
## Django Models
It was important to see the response that was received from the API so that we know what fields are available and what we’re going to store. We’re going to need three models: Movie, Genre and SearchTerm. The first two should be obvious, the third will keep a record of search terms that were used so that we know when to re-run the queries.
