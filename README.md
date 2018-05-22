This is a simple Python3 script to decode Creative's CMV format.

It splits out the WAV and JPG parts without altering them. The resulting files
are unusual (WAV is IMA ADPCM encoded and JPGs have several frames of video in
them each and black bars for padding) but can be opened by normal programs
(VLC, Paint, etc.) without a problem.

It's also safe to use on a very big CMV files because it only loads a few KB
of the WAV and one chunk of the CMV Video into RAM at a time.

Arguments are: cmv file, output wav file, output directory for jpegs (must exist).

For more information about this file format see: [link](https://wiki.multimedia.cx/index.php/CMV).

It could easily be adapted to work on Python 2 and if you're interested in
that or find a file that doesn't work with it or have any other problem feel
free to open an issue on this repo.

Sample usage and output:
```
$ python cmvdecode.py test.cmv test.wav test
RIFF WAV is 348.2812957763672 MiB.
CMV Video is 160x118@25FPS.
It has 206325 frames in 8253 chunks, 48.830078125 KiB each.
Total CMV Video size: 393.54944801330566 MiB
It's 137.55 minutes of footage.
0/8253 chunks done.
826/8253 chunks done.
1652/8253 chunks done.
2478/8253 chunks done.
3304/8253 chunks done.
4130/8253 chunks done.
4956/8253 chunks done.
5782/8253 chunks done.
6608/8253 chunks done.
7434/8253 chunks done.
8253/8253 chunks done.
Padding in chunks was 39.071351051330566 MiB.
```
