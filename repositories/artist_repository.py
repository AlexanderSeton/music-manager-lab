from db.run_sql import run_sql
from models.artist import Artist


def save(artist):
    sql = "INSERT INTO artists (full_name) VALUES (%s) RETURNING *"
    values = [artist.full_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row["full_name"], row["id"])
        artists.append(artist)
    return artists

def select_artist_by_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["full_name"], result["id"])
    return artist

def create_and_save_artist():
    full_name = input("\nEnter the artist's full name: ")
    artist = Artist(full_name)
    sql = "INSERT INTO artists (full_name) VALUES (%s)"
    values = [artist.full_name]
    result = run_sql(sql, values)
    id = result[0]["id"]
    artist.id = id

def delete_all_artists():
    sql = "DELETE FROM artists"
    run_sql(sql)

def get_list_all_artist_names():
    artist_names = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist_names.append(row["full_name"])
    return artist_names

def get_artist_by_fullname(name):
    artist = None
    sql = "SELECT * FROM artists WHERE full_name = %s"
    values = [name]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["full_name"], result["id"])
    return artist

def list_all_artist_names():
    print("")
    sql = "SELECT full_name FROM artists"
    results = run_sql(sql)
    for row in results:
        print(row)
