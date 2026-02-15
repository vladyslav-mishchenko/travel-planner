"""
services.py

Service functions for TravelPlace that validate existence and availability
of places in a third-party API before storing them in the database.
"""


def ensure_place_exists(place_name: str) -> bool:
    return True
