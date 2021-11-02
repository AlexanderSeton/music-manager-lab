import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artistr
import repositories.album_repository as albumr

# Deletes
albumr.delete_all_albums()
artistr.delete_all_artists()

# Artists
artist1 = Artist("Michael Jackson")
artistr.save(artist1)
artist_list = artistr.select_all()
for artist in artist_list:
    print(artist.__dict__)

# Albums
album1 = Album("Thriller", "Pop", artist1)
albumr.save(album1)
album_list = albumr.select_all()
for album in album_list:
    print(album.__dict__)

# Set trace
pdb.set_trace()
