from json import JSONDecoder

from rest_framework import viewsets
import requests
from .models import Disaster
from .serializer import DisasterSerializer


def fetch_data_reliefweb():
    print("Fetching ReliefWeb data!")
    url = "https://api.reliefweb.int/v1/disasters?limit=1000"
    initial_response = requests.get(url)

    total_count = 0
    try:
        initial_response.raise_for_status()
        initial_response_json = initial_response.json()
        total_count = initial_response_json["totalCount"]
    except:
        print("Error occurred fetching ReliefWeb data.")
        return None

    # Calculate iterations by the total count of disasters modulo
    # by the return limit (1000), + 1 to get the number of pages
    iterations = (total_count // 1000)
    disasters = []

    print("total ", total_count)
    print("iterations ", iterations)

    for _ in range(iterations):
        response = requests.get(url)

        try:
            response.raise_for_status()
            response_json = response.json()
            response_data = response_json["data"]
            for entry in response_data:

                # Make request to provided href
                entry_url = entry["href"]
                entry_response = requests.get(entry_url)
                try:
                    entry_response.raise_for_status()
                    entry_response_json = entry_response.json()
                except:
                    print("Error occurred fetching ReliefWeb data.")
                    return None

                disaster = {
                    "id": entry_response_json["data"]["id"],
                    "api": "ReliefWeb",
                    "source": None,
                    "name": entry_response_json["data"]["fields"]["name"],
                    "category": entry_response_json["data"]["fields"]["primary_type"]["name"],
                    "reference": entry_response_json["data"]["fields"]["url"],
                    "country": entry_response_json["data"]["fields"]["primary_country"]["name"],
                    "date": entry_response_json["data"]["fields"]["date"]["event"],
                    "description": entry_response_json["data"]["fields"]["description-html"],
                    "status": entry_response_json["data"]["fields"]["status"],
                    "longitudinal": None,
                    "latitudinal": None
                }
                disasters.append(disaster)
        except:
            print("Error occurred fetching ReliefWeb data.")
            return None

        url = response_json["links"]["next"]["href"]

    return disasters


def fetch_data_eonet():
    print("Fetching EONET data!")
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    response = requests.get(url)

    try:
        response.raise_for_status()
        return response.json()["events"]
    except:
        print("Error occurred fetching ReliefWeb data.")
        return None


def process_category_eonet(category: str):
    match category:
        case "drought":
            return Disaster.DROUGHT
        case "dustHaze":
            return Disaster.DUST_HAZE
        case "earthquakes":
            return Disaster.EARTHQUAKE
        case "floods":
            return Disaster.FLOOD
        case "landslides":
            return Disaster.LANDSLIDE
        case "manmade":
            return Disaster.MAN_MADE
        case "seaLakeIce":
            return Disaster.SEA_LAKE_ICE
        case "severeStorms":
            return Disaster.SEVERE_STORM
        case "snow":
            return Disaster.SNOW
        case "tempExtremes":
            return Disaster.TEMPERATURE_EXTREME
        case "volcanos":
            return Disaster.VOLCANO
        case "waterColor":
            return Disaster.WATER_COLOR
        case "wildfires":
            return Disaster.WILDFIRE
    return None


class DisasterViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = DisasterSerializer

    def get_queryset(self):
        data = Disaster.objects.all()

        # Enable filtering by API source
        api = self.request.query_params.get("api")
        if api is not None:
            data = data.filter(api=api)

        # Enable filtering by category
        category = self.request.query_params.get("category")
        if category is not None:
            data = data.filter(category=category)

        # Enable filtering by event id
        event_id = self.request.query_params.get("id")
        if event_id is not None:
            data = data.filter(id=event_id)

        return data

    def get_disaster_data(self):
        reliefweb_data = fetch_data_reliefweb()
        eonet_data = fetch_data_eonet()

        return reliefweb_data, eonet_data

    def save_disaster_data(self):
        reliefweb_data, eonet_data = self.get_disaster_data()

        # Handle EONET data
        if eonet_data is not None:
            for disaster in eonet_data:
                try:
                    disaster_object = Disaster.objects.create(
                        id=disaster["id"],
                        source=disaster["source"],
                        api=disaster["api"],
                        name=disaster["title"],
                        reference=disaster["link"],
                        category=process_category_eonet(disaster["categories"][0]["id"]),
                        country=None,
                        date=None,
                        description=None,
                        status=None,
                        longitudinal=disaster["geometry"][0]["coordinates"][0],
                        latitudinal=disaster["geometry"][0]["coordinates"][1]
                    )
                    disaster_object.save()
                except:
                    print("Error saving disaster from EONET...")
                    pass
            print("Saved EONET data!")

        # todo: refactor to handle both data sets at once.. move the JSON processing to its fetch function.. or a helper

        # Handle ReliefWeb data
        if reliefweb_data is not None:
            for disaster in reliefweb_data:
                try:
                    reliefweb_disaster_object = Disaster.objects.create(
                        id=disaster["id"],
                        source=disaster["source"],
                        api=disaster["api"],
                        name=disaster["title"],
                        reference=disaster["reference"],
                        category=disaster["category"],
                        country=disaster["country"],
                        date=disaster["date"],
                        description=disaster["description"],
                        status=disaster["status"],
                        longitudinal=disaster["longitudinal"],
                        latitudinal=disaster["latitudinal"]
                    )
                    reliefweb_disaster_object.save()
                except:
                    print("Error saving disaster from ReliefWeb...")
                    pass
            print("Saved ReliefWeb data!")

        print("Finished scheduled API fetch operation.")
