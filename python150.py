import json
import random
import string
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


class ETL:

    def __init__(self):
        self.engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
        self.message = None
        self.is_running = False
        self.source_type = None
        self.file = None
        self.msgQueue = q.Queue

    def run_simulation(self):
        while True:
            self.message = {'key': random.choice(string.ascii_letters), 'value': random.randint(0, 100),
                            'ts': gen_datetime()}
            self.source_type = 'simulation'
        return self

    def read_from_file(self, file):
        with open('somefile') as openfileobject:
            for line in openfileobject:
                self.message = line
                self.source_type = "file"
                return self

    def write_to_sink(self, sink_type):
        if sink_type == "console":
            print(self.message)

        elif sink_type == "postgres":
            data = json.loads(self.message)
            df = pd.DataFrame(data)
            df.to_sql("JSON_Store", self.engine)


""" Example usage ETL.run_simulation().write_to_sink("console/postregs") 
    Better implementation would be to use sockets 
    and have a function that keeps the socket open forever for the simulation source """
