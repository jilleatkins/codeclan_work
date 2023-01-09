 

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Eminem")
artist_repository.save(artist1)

artist2 = Artist("Ed Sheeran")
artist_repository.save(artist2)

album1 = Album(artist1, "Curtain Call", "2005")
album_repository.save(album1)

album2 = Album(artist1, "MMLP", "2000")
album_repository.save(album2)

album3 = Album(artist2, "Divide", "2017")
album_repository.save(album3)

album4 = Album(artist2, "Plus", "2011")
album_repository.save(album4)

pdb.set_trace()

