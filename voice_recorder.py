# pip install pyaudio
# before executing the below program install the pyaudio in terminal by typing "pip install pyaudio" to it.
import pyaudio
import wave
import os

class VoiceRecorder:
    def __init__(self, output_folder='recordings'):
        self.audio = pyaudio.PyAudio()
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.is_recording = False
        self.stream = None

    def start_recording(self, filename):
        if not self.is_recording:
            self.is_recording = True
            self.stream = self.audio.open(format=pyaudio.paInt16,
                                          channels=1,
                                          rate=44100,
                                          input=True,
                                          frames_per_buffer=1024)
            self.frames = []
            print("Recording...")
            self.filename = filename

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            print("Recording stopped.")
            self.stream.stop_stream()
            self.stream.close()

            wf = wave.open(os.path.join(self.output_folder, self.filename), 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            print(f"Recording saved as {self.filename}")

    def record(self, duration=5, filename="output.wav"):
        self.start_recording(filename)
        for _ in range(int(44100 / 1024 * duration)):
            data = self.stream.read(1024)
            self.frames.append(data)
        self.stop_recording()

if __name__ == "__main__":
    recorder = VoiceRecorder()
    recorder.record()