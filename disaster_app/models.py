from django.db import models


class Disaster(models.Model):
    COLD_WAVE = "COLD_WAVE"
    COMPLEX_EMERGENCY = "COMPLEX_EMERGENCY"
    DROUGHT = "DROUGHT"
    DUST_HAZE = "DUST_HAZE"
    EARTHQUAKE = "EARTHQUAKE"
    EPIDEMIC = "EPIDEMIC"
    EXTRA_TROPICAL_CYCLONE = "EXTRA_TROPICAL_CYCLONE"
    FIRE = "FIRE"
    FLOOD = "FLOOD"
    HEAT_WAVE = "HEAT_WAVE"
    INSECT_INFESTATION = "INSECT_INFESTATION"
    LANDSLIDE = "LANDSLIDE"
    MUDSLIDE = "MUDSLIDE"
    MAN_MADE = "MAN_MADE"
    OTHER = "OTHER"
    SEA_LAKE_ICE = "SEA_LAKE_ICE"
    SEVERE_STORM = "SEVERE_STORM"
    SNOW = "SNOW"
    TEMPERATURE_EXTREME = "TEMPERATURE_EXTREME"
    TROPICAL_CYCLONE = "TROPICAL_CYCLONE"
    TSUNAMI = "TSUNAMI"
    VOLCANO = "VOLCANO"
    WATER_COLOR = "WATER_COLOR"
    WILDFIRE = "WILDFIRE"

    CATEGORIES = [
        (COLD_WAVE, "Cold Wave"),
        (COMPLEX_EMERGENCY, "Complex Emergency"),
        (DROUGHT, "Drought"),
        (DUST_HAZE, "Dust Haze"),
        (EARTHQUAKE, "Earthquake"),
        (EPIDEMIC, "Epidemic"),
        (EXTRA_TROPICAL_CYCLONE, "Extra Tropical Cyclone"),
        (FIRE, "Fire"),
        (FLOOD, "Flood"),
        (HEAT_WAVE, "Heat Wave"),
        (INSECT_INFESTATION, "Insect Infestation"),
        (LANDSLIDE, "Landslide"),
        (MUDSLIDE, "Mudslide"),
        (MAN_MADE, "Man Made"),
        (OTHER, "Other"),
        (SEA_LAKE_ICE, "Sea Lake Ice"),
        (SEVERE_STORM, "Severe Storm"),
        (SNOW, "Snow"),
        (TEMPERATURE_EXTREME, "Temperature Extreme"),
        (TROPICAL_CYCLONE, "Tropical Cyclone"),
        (TSUNAMI, "Tsunami"),
        (VOLCANO, "Volcano"),
        (WATER_COLOR, "Water Color"),
        (WILDFIRE, "Wildfire"),
    ]

    APIS = [
        ("Manual", "Manually Added"),
        ("EONET", "EONET"),
        ("ReliefWeb", "ReliefWeb")
    ]

    id = models.CharField(max_length=30, primary_key=True)
    api = models.CharField(max_length=30, choices=APIS, default=None)
    source = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORIES, default=None)
    reference = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(max_length=20000, null=True, blank=True)
    status = models.CharField(max_length=60, null=True, blank=True)
    longitudinal = models.FloatField(null=True, blank=True)
    latitudinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "({}) {}".format(self.api, self.name)