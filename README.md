# pseudo\_shuffle

## Demonstration

``` cmd
flask run
```

``` cmd
Ensure your redirect URI == flask server address + '/callback'
```

```
Values are hard coded in atm, so just gotta change them to take data according to site input
```

``` cmd
FOR JAMES: directory variable stores the songs in the format you wanted, 
if you were to input it into the algorithm you're making
```

## Intro

A shuffle specific to you.

Do you ever get sick of hearing the same songs every time you reshuffle your playlist?
Are you tired of having more popular artists play far more often than lesser known ones?
Have you wondered about those songs that haven't been played to you in years since they never come up?

I have.

Call me a conspiracy nut, but I find that the *shuffle* features on popular music players seem to be biased.
For over 5 years this issue has been nagging away at my mind that although we use shuffle to try spice up our playlists and revive old tastes, we have settled for the mediocre solution we have now.

'*But what would be a better solution?*' I hear nobody ask.
In reality, the majority of us don't want a truly random playlist but instead one that has been carefully crafted to give you a sort of round-robbin one.

This project will attempt to generate said playlist.

## What would this look like?

Take the following music library of boppin' Soundcloud rapper EP's:

```
├── artist_1
│   ├── album_1
│   │   ├── song_1
│   │   ├── song_2
│   │   └── song_3
│   └── album_2
│       ├── song_1
│       ├── song_2
│       ├── song_3
│       └── song_4
├── artist_2
│   └── album_1
│       ├── song_1
│       ├── song_2
│       ├── song_3
│       ├── song_4
│       └── song_5
└── artist_3
    ├── album_1
    │   ├── song_1
    │   ├── song_2
    │   └── song_3
    ├── album_2
    │   ├── song_1
    │   └── song_2
    └── album_3
        ├── song_1
        ├── song_2
        ├── song_3
        └── song_4
```

Considering the statistics:

- 3 artists
- 6 albums
- 21 songs

```
artist_3/album_1/song_1
artist_2/album_1/song_1
artist_1/album_1/song_1
artist_3/album_1/song_2
artist_1/album_1/song_2
artist_3/album_1/song_3
artist_2/album_1/song_2
artist_1/album_1/song_3
artist_3/album_2/song_1
artist_1/album_2/song_1
artist_3/album_2/song_2
artist_2/album_1/song_3
artist_1/album_2/song_2
artist_3/album_3/song_1
artist_1/album_2/song_3
artist_2/album_1/song_4
artist_3/album_3/song_2
artist_1/album_2/song_4
artist_3/album_3/song_3
artist_2/album_1/song_5
artist_3/album_3/song_4
```

The above ensured that no artist is played twice in a row, but still leaves a lot to desire.
Albums and songs are still mostly in alphanumerical order (because I'm shuffling this myself).

When more requirements are added in, such as not having the same album from an artist in a row and so on, it becomes impossible to reliably achieve.
A solution to this would be to put weightings to requirements. 
Consider the `no same artist in a row` as +1.0  and `no same album from artist` as +0.8.
When the task is impossible, the weightings will determine what rule overrides the other.

## Who is this for?

To start - no one.
It will begin as a concept to generate a list of songs in the desired format.
Once achieved, the next step will be to integrate it with an open standard such as an [mpd](https://www.musicpd.org/) player.
That would only be of interest to a very small niche but turn the concept into a prototype.

I would love to be able to integrate the final project with [Apple Music](https://www.apple.com/uk/apple-music/) and [Spotify](https://www.spotify.com/uk/) at least, but am not sure how feasible it is for such interoperability with these solutions.

## Future ideas

- Track songs that get skipped more than others, giving the potential to put said songs lower down in the playlist.
  
- Consider the songs that weren't reached from the previous playlist and prioritise those songs to ensure you hear new songs every time.

- Take metadata into consideration.
  - Want to go through the ages? How about prioritising earlier songs over newer ones? 
  - Only want songs around the 3-minute mark at the top? ~3:00 duration weightings could be heightened.
  - Feeling hyped? prioritise genres such as Drum & Bass, Electro, etc. or if available, go by songs with higher BPM.
  - With the addition of these little customisations, you could truly get a pseudo-shuffled playlist for you.
  
The above would be optional, allowing the user to make the shuffle that suits them.