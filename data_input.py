import csv
from cs50 import SQL

db = SQL("sqlite:///shows.db")

# Insert actors
with open("actors_data.csv", "r") as f:
    reader = csv.DictReader(f, fieldnames=["name", "image"])
    next(reader)
    for row in reader:
        data = {}
        db.execute(
            "INSERT INTO people (name, photo) VALUES(?,?);", row["name"], row["image"]
        )


# Insert genres
with open("movies_genres.csv", "r") as f:
    reader = csv.DictReader(f, fieldnames=["name"])
    next(reader)
    for row in reader:
        db.execute("INSERT INTO genres (name) VALUES(?);", row["name"])


with open("movies_data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        db.execute(
            """INSERT INTO movies (
            title,
            description,
            release,
            length,
            rating,
            poster,
            trailer,
            is_featured)
             VALUES (?,?,?,?,?,?,?,?)""",
            row["title"],
            row["description"],
            row["release"],
            row["length"],
            row["rating"],
            row["poster"],
            row["trailer"],
            bool(row["is_featured"]),
        )


# Insert Shows

with open("shows_data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(row)
        # print("\n\n\n\n")
        db.execute(
            """INSERT INTO shows (
            title,
            description,
            release,
            rating,
            poster,
            trailer,
            is_featured)
             VALUES (?,?,?,?,?,?,?)""",
            row["title"],
            row["description"],
            row["release"],
            row["rating"],
            row["poster"],
            row["trailer"],
            bool(row["is_featured"]),
        )
