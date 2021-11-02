from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
from repositories import artist_repository


def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) returning *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select_artist_by_id(row["artist_id"])
        album = Album(row["title"], row["genre"], artist)
        albums.append(album)
    return albums

def create_and_save_album():
    title = input("\nEnter the album's title: ")
    genre = input("\nEnter the album's genre: ")
    artist_fn = input("\nEnter the album's artist's full name: ")
    existing_artist_names = artist_repository.get_list_all_artist_names()
    print("\n\nexisting artist names:", existing_artist_names)
    if artist_fn in existing_artist_names:
        artist = artist_repository.get_artist_by_fullname(artist_fn)
        album = Album(title, genre, artist)
        sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
        values = [title, genre, artist.id]
        result = run_sql(sql, values)
        id = result[0]["id"]
        album.id = id
    else:
        print("ERROR: artist not found. Please create the artist first.")
    
def delete_all_albums():
    sql = "DELETE FROM albums"
    run_sql(sql)

def list_all_album_titles():
    print("")
    sql = "SELECT title FROM albums"
    results = run_sql(sql)
    for row in results:
        print(row)
