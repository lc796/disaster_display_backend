# Disaster Display Backend
## [View the live site](https://api.disaster.lukecs.dev)

## Introduction
Project built using Django. This consumes the public ReliefWeb and NASA EONET APIs to process alongside the EU EMDAT data to provide a comprehensive unified source of disasters. 

The app uses the package DjangoRestFramework to provide a public facing API. This will allow the React frontend to consume the disasters with a GET request. Additionally, the following parameters can be specified: disaster id, category, or country.

The response will return a list of disasters. Please note that some of the following attributes might be null:
- id
- api (*which API/dataset the rest of the data is sourced from*)
- source (*the source of the disaster as provided by the consumed API/dataset*)
- name
- category (*given in the singular, i.e., earthquake, not earthquakes*)
- reference (*the original APIs page for this disaster*)
- country (*if spanning multiple countries, primary country is used*)
- date
- description (*given in HTML format*)
- status
- longitudinal
- latitudinal

## Technology used
- Python
- Django
- DjangoRestFramework

Deployed using Heroku.