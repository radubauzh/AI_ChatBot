# Overview
This ChatBot is designed to interact with users by answering questions, providing recommendations, and fetching information related to humans, films, and various other entities. It utilizes a graph database to store and query data, and a set of predefined classes to handle different aspects of the interactions.

## Features
**Data Queries**: Performs SPARQL queries on a graph database to fetch data about humans and films.
**Entity Resolution**: Matches user input to known entities in the database.
**Intent Recognition**: Identifies the user's intent from the question.
**Recommendations**: Provides movie and location recommendations based on user queries.
**Information Retrieval**: Fetches various types of information like images, frames, webpage links, occupations, genres, etc.
**Crowdsourcing Integration**: Utilizes crowdsourced data for enhancing responses.
**Fleiss Kappa Calculation**: Measures the reliability of agreement between different raters.
And much more


## Dependencies
**RDFLib**: For SPARQL queries and handling graph data.
**NLTK**: For natural language processing tasks.
Other dependencies for entity embedding, zero-shot classification, and other NLP tasks.
## Limitations
The bot's accuracy depends on the quality of data in the graph database.
It might not handle ambiguous or very complex queries effectively.
The bot is limited to the predefined intents and entities.
## Future Work
Expanding the database to include more entities and relations.
Improving the NLP model for better intent recognition and entity extraction.
Integrating more dynamic data sources for up-to-date information.





