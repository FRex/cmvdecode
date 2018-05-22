import sys
import math


if __name__ != '__main__':
    raise RuntimeError("This is a script, not a module.")


if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} cmv-in wav-out jpeg-folder-out", file=sys.stderr)
    sys.exit(1)

jpeg_folder = sys.argv[3]
f = open(sys.argv[1], 'rb')


with open(sys.argv[2], 'wb') as g:
    riff_header = f.read(8)
    assert len(riff_header) == 8
    assert riff_header[0:4] == b'RIFF'
    riff_len = int.from_bytes(riff_header[4:8], 'little')
    print(f"RIFF WAV is {(8 + riff_len) / 1024 ** 2} MiB.")
    while riff_len > 0:
        towrite = min(riff_len, 2 ** 13)
        g.write(f.read(towrite))
        riff_len -= towrite


cmv_header = f.read(51)
assert len(cmv_header) == 51
assert cmv_header[0:9] == b'CMV001000'
vid_width = int.from_bytes(cmv_header[9:12], 'little')
vid_height = int.from_bytes(cmv_header[12:15], 'little')
chunk = int.from_bytes(cmv_header[21:24], 'little')
frames = int.from_bytes(cmv_header[24:27], 'little')
fileframes = int.from_bytes(cmv_header[27:30], 'little')
fps = int.from_bytes(cmv_header[36:39], 'little')
chunks = math.ceil(fileframes / frames)
print(f"CMV Video is {vid_width}x{vid_height}@{fps}FPS.")
print(f"It has {fileframes} frames in {chunks} chunks, {chunk / 1024} KiB each.")
print(f"It's {(fileframes / fps) / 60} minutes of footage.")
for i in range(chunks):
    if (i % (chunks // 10 + 1)) == 0:
        print(f"{i}/{chunks} chunks done.")

    cdata = f.read(chunk)
    jpeglen = int.from_bytes(cdata[0:3], 'little')
    with open(f'{jpeg_folder}/chunk-{i:06}.jpeg', 'wb') as g:
        g.write(cdata[3:3 + jpeglen])

print(f"{chunks}/{chunks} chunks done.")
