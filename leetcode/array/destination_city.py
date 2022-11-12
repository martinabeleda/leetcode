from collections import defaultdict


def destination_city(paths: list[tuple[str, str]]) -> str:
    """Returns the destination city given a list of paths from source to destination

    Approach:
        - Keep a map of cities
        - The value in the map is a set of the outgoing destinations from that city
    """
    cities: dict[str, set] = defaultdict(set)
    for source, destination in paths:
        cities[source].add(destination)
        cities[destination]

    for city, outgoing in cities.items():
        if not outgoing:
            return city

    raise ValueError(f"Could not find a destination city from {cities=}")


def destination_city_set(paths: list[tuple[str, str]]) -> str:
    """A solution implemented using sets"""
    sources, destinations = map(set, zip(*paths))
    return (destinations - sources).pop()
