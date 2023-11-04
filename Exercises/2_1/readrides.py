# readrides.py

from collections import namedtuple
import csv


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionary(filename):
    """
    Read the bus ride data as a list of dictionary
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
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
            records.append(record)
    return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    """
    Read the bus ride data as a list of objects
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


RideTuple = namedtuple("RideTuple", ["route", "date", "daytype", "rides"])


def read_rides_as_namedtuple(filename):
    """
    Read the bus ride data as a list of named tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RideTuple(route, date, daytype, rides)
            records.append(record)
    return records


class RowWithSLots:
    __slots__ = ("route", "date", "daytype", "rides")

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class_with_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            record = RowWithSLots(
                route=row[0], date=row[1], daytype=row[2], rides=row[3]
            )
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_tuples("../../Data/ctabus.csv")
    print(
        "Memory Use for tuples: Current %d, Peak %d" % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_dictionary("../../Data/ctabus.csv")
    print(
        "Memory Use for dictionary: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_class("../../Data/ctabus.csv")
    print(
        "Memory Use for classes: Current %d, Peak %d" % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_namedtuple("../../Data/ctabus.csv")
    print(
        "Memory Use for namedtuple: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()

    tracemalloc.start()
    rows = read_rides_as_class_with_slots("../../Data/ctabus.csv")
    print("Memory Use for slots: Current %d, Peak %d" % tracemalloc.get_traced_memory())
    tracemalloc.stop()

