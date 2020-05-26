#!/usr/bin/env python3
import json
from pathlib import Path

movies = [
  {"id": 1, "name": "Terminator", "year": 1989},
  {"id": 2, "name": "Little Wonder", "year": 1985},
]

#Write json to file
data = json.dumps(movies)
Path("movies.json").write_text(data)

#Read data from json file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]['name'])
