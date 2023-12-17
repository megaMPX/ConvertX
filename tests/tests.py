from pydub import AudioSegment
from pydub import effects

song = AudioSegment.from_wav("convert.wav")

go = song[12000:20000]


go.export( 'ggg.wav', format="wav")

a = 1.01
print(type(a))
so = song.speedup(1.01, 150, 25)

so.export('gggg.wav', format="wav")


fo = effects.normalize(song)

fo.export('ggggg.wav',format='wav')


octaves = 2/10/2#0.05
print(float(2))
new_sample_rate = int(song.frame_rate * (2.0 ** octaves))
hipitch_sound = song._spawn(song.raw_data, overrides={'frame_rate': new_sample_rate})
hipitch_sound = hipitch_sound.set_frame_rate(44100)

hipitch_sound.export('gggggg.wav',format='wav')