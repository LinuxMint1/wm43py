import os
import subprocess

def convert_wav_to_mp3(wav_filepath, mp3_filepath=None):
    """
    Converts a WAV file to MP3 format using FFmpeg.

    Args:
        wav_filepath: Path to the input WAV file.
        mp3_filepath: Optional path to the output MP3 file.
                      If not provided, the output file will have the same name
                      as the input file but with the .mp3 extension.
    """

    if not os.path.exists(wav_filepath):
        raise FileNotFoundError(f"Syöttötiedostoa ei löydy hakemistosta: {wav_filepath}")

    if not wav_filepath.lower().endswith(".wav"):
        raise ValueError("Syöttötiedoston on oltava WAV-tiedosto!")

    if mp3_filepath is None:
        mp3_filepath = os.path.splitext(wav_filepath)[0] + ".mp3"

    try:
        subprocess.run([
            "ffmpeg",
            "-i", wav_filepath,
            "-acodec", "libmp3lame",  # Use LAME MP3 encoder
            "-q:a", "2",  # Set audio quality (0 is best, 9 is worst)
            mp3_filepath
        ], check=True, capture_output=True, text=True)

        print(f"Onnistuneesti muunnettu '{wav_filepath}' vaille '{mp3_filepath}'")

    except subprocess.CalledProcessError as e:
        print(f"Virhe muunnoksen aikana:")
        print(f"  Palautuskoodi: {e.returncode}")
        print(f"  Stdout: {e.stdout}")
        print(f"  Stderr: {e.stderr}")

def convert_mp4_to_mp3(mp4_filepath, mp3_filepath=None):
    """
    Extracts audio from an MP4 video file and converts it to MP3 format using FFmpeg.

    Args:
        mp4_filepath: Path to the input MP4 file.
        mp3_filepath: Optional path to the output MP3 file.
                      If not provided, the output file will have the same name
                      as the input file but with the .mp3 extension.
    """

    if not os.path.exists(mp4_filepath):
        raise FileNotFoundError(f"Syöttötiedostoa ei löydy hakemistosta: {mp4_filepath}")

    if not mp4_filepath.lower().endswith(".mp4"):
        raise ValueError("Syöttötiedoston on oltava MP4-tiedosto")

    if mp3_filepath is None:
        mp3_filepath = os.path.splitext(mp4_filepath)[0] + ".mp3"

    try:
        subprocess.run([
            "ffmpeg",
            "-i", mp4_filepath,
            "-vn",  # Disable video processing (extract audio only)
            "-acodec", "libmp3lame",
            "-q:a", "2",
            mp3_filepath
        ], check=True, capture_output=True, text=True)

        print(f"Muutettu onnistuneesti '{mp4_filepath}' vaille '{mp3_filepath}'")

    except subprocess.CalledProcessError as e:
        print(f"Virhe muuntamisen aikana:")
        print(f"  Palautuskoodi: {e.returncode}")
        print(f"  Stdout: {e.stdout}")
        print(f"  Stderr: {e.stderr}")

if __name__ == "__main__":
    # Example usage:
    # convert_wav_to_mp3("audio.wav")
    # convert_mp4_to_mp3("video.mp4", "audio_output.mp3")

    while True:
        print("\nValitse Merkintä:")
        print("1. Muuntaa WAV vaille MP3")
        print("2. Muuntaa MP4 vaille MP3")
        print("3. Poistu")

        choice = input("Syötä (1-3): ")

        if choice == '1':
            wav_file = input("Syötä WAV-tiedoston hakemisto: ")
            convert_wav_to_mp3(wav_file)
        elif choice == '2':
            mp4_file = input("Syötä MP4-tiedoston hakemisto: ")
            convert_mp4_to_mp3(mp4_file)
        elif choice == '3':
            break
        if choice == '46':
              print("....niin muistitko? Mecca, Ohio. 8. joulukuuta 2024." ) 
        if choice == '88':
              print("niin muistitko? Mecca, Ohio. 8. joulukuuta 2024." )
        if choice == '1140':
              print("Adachi Altoinen oli täällä!" )
        else:
            print("Virheellinen merkintä. Yritä uudelleen oikealla polulla.")
