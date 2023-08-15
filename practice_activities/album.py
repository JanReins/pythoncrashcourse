def make_album(artist, album_name, num_songs= None):
    album = {
        "artist": artist,
        "album": album_name,
    }
    if num_songs is not None:
        album["num_songs"] = num_songs
    return album

while True:
    artist = input("Enter artist name: ")
    if artist == "quit":
        break
    album_name = input("Enter album name: ")
    num_songs = input("Enter song number: ")

    final_album = make_album(artist, album_name, num_songs)
    print(final_album)
