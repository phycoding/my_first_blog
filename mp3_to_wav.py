import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, wav_folder):
    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(wav_folder):
        os.makedirs(wav_folder)

    # Loop through all the MP3 files in the input directory
    for filename in os.listdir(mp3_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(mp3_folder, filename)
            wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + ".wav")
            # Load the MP3 file and convert it to WAV format
            sound = AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python mp3_to_wav.py <mp3_folder> <wav_folder>")
        sys.exit(1)

    mp3_folder = sys.argv[1]
    wav_folder = sys.argv[2]

    # Convert the MP3 files to WAV format
    convert_mp3_to_wav(mp3_folder, wav_folder)

    print("Conversion complete!")
