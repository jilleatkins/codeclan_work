from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def select_all():
  artists = []

  sql = "SELECT * FROM artists"
  results = run_sql(sql)

  for row in results:
    artist = Artist(row['artist_name'], row['id'])
    artists.append(artist)
  return artists

def save(artist):
  sql = f"INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
  values = [artist.artist_name]
  results = run_sql(sql, values)
  id = results[0]['id']
  artist.id = id
  return artist

def select(id):
  artist = None
  sql = "SELECT * FROM artist WHERE = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  if result:
    artist = Artist(result['artist_name'])
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artist WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
  sql = "UPDATE artist SET (artist_name)"
  values = [artist.artist_name]
  run_sql(sql, values)

def albums(artist):
  albums = []
  sql = "SELECT * FROM albums WHERE album_id = %s"
  values = [artist.id]
  results = run_sql(sql, values)
  for row in results:
    album = Album(artist, row['album_name'], row['album_year'], row['id'])
    albums.append(album)
  return albums