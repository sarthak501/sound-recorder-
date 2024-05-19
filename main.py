import sounddevice as sd
import soundfile as sf

def record_sound(filename, duration, samplerate=44100, channels=2):
    print("Recording...")
    
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='float64')
    
    sd.wait()
    print("Recording finished.")

    
    sf.write(filename, recording, samplerate)

if __name__ == "__main__":
    filename = "recorded_sound.wav"  
    duration = 5  
    record_sound(filename, duration)
