import csv
from collections import defaultdict
from typing import Counter


def read_portfolio(filename: str):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            record = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(record)
    return portfolio


def read_rides_as_dictionaries(filename: str):
    """
    Read the bus ride data as a list of dictionary
    """
    results = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            results.append(record)
    return results


rides = read_rides_as_dictionaries("../../Data/ctabus.csv")

# 1. How many bus routes exist in Chicago?
bus_routes_count = len({ride["route"] for ride in rides})
print(f"There are {bus_routes_count} unique bus routes in Chicago.")
print()

# 2. How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?
rides_by_route_name = defaultdict(dict)
for ride in rides:
    rides_by_route_name[ride["route"]][ride["date"]] = ride["rides"]
print(
    f"{rides_by_route_name['22']['02/01/2011']} people rode the number 22 bus on February 2, 2011"
)
print(
    f"{rides_by_route_name['147']['08/31/2013']} people rode the number 147 bus on August 31, 2013"
)
print()

# 3. What is the total number of rides taken on each bus route?
rides_counter = Counter()
for ride in rides:
    rides_counter[ride["route"]] += ride["rides"]
for ride_counter in sorted(rides_counter.items()):
    print(
        f"The total number of rides for the {ride_counter[0]} bus route is {ride_counter[1]}"
    )
print()

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
rides_by_route_in_2001 = Counter()
rides_by_route_in_2011 = Counter()
for ride in rides:
    if ride["date"].endswith("2001"):
        rides_by_route_in_2001[ride["route"]] += ride["rides"]
    if ride["date"].endswith("2011"):
        rides_by_route_in_2011[ride["route"]] += ride["rides"]

rides_delta_between_2001_to_2011 = Counter()
for route, rides in rides_by_route_in_2001.items():
    rides_delta_between_2001_to_2011[route] = rides_by_route_in_2011[route] - rides

five_greatest_increases = rides_delta_between_2001_to_2011.most_common(5)
for i in range(0, 5):
    print(
        f"The number {i+1} increase is {five_greatest_increases[i][0]} with {five_greatest_increases[i][1]} passengers"
    )
