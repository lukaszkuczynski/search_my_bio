# Motivation
This app should automate CV projects lists and give you possibility to query it freely.  Index your projects to Elasticsearch.  Backend done in Flask.

## Running
Before you run API endpoint, you have to have Elasticsearch up and running.  Moreover it has to have index and type configured.  
Preparation script is named `indexmyprojects.py`, it takes yml file as input and outputs to Elasticsearch.
Run api endpoint using `start_api_server.sh` then go to [localhost:5000](http://localhost:5000).  

## API usage
 - Query for match on every field of document
 `/api/search?q=queried_text` returns list of documents matching `queried_text`
