from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album

def select_all():
  albums = []

  sql = "SELECT * FROM tasks"
  results = run_sql(sql)

  for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(artist, row('album_name'), row('album_year'), row['id'])
        albums.append(album)
  return albums

def save(album):
  sql = f"INSERT INTO albums (artist_id, album_name, album_year) VALUES (%s, %s, %s) RETURNING *"
  values = [album.artist.id, album.album_name, album.album_year]
  results = run_sql(sql, values)
  if results:
    id = results[0]['id']
    album.id = id
    return album

def select(id):
  album = None
  sql = "SELECT * FROM books WHERE id = %s"
  values = [id]
  results = run_sql(sql, values)
  if results:
    result = results[0]
    artist = artist_repository.select(result['album_id'])
    album = Album(artist, result['album_name'], result['album_year'])

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def update(album):
    sql = "UPDATE albums SET (album_name, album_year) = (%s, %s) WHERE id = %s"
    values = [album.album_name, album.album_year, album.id]
    run_sql(sql, values)