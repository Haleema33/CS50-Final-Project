import wave
import numpy as np
import os

# Directory for sound files
sound_directory = "sounds"

# Explicitly create the dictionary mapping characters to their sound files
char_to_sound = {chr(i): os.path.join(sound_directory, f'piano_{chr(i)}.wav') for i in range(ord('a'), ord('z') + 1)}

# Function to read a WAV file and return its data and parameters
def read_wav(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None, None

    try:
        with wave.open(file_path, 'rb') as wf:
            params = wf.getparams()
            frames = wf.readframes(params.nframes)
            audio_data = np.frombuffer(frames, dtype=np.int16)
        return audio_data, params
    except wave.Error as e:
        print(f"Error reading '{file_path}': {e}")
        return None, None

# Function to write WAV data to a file with 2x speed
def write_wav(file_path, audio_data, params):
    with wave.open(file_path, 'wb') as wf:
        # Convert to mono if needed
        if params.nchannels > 1:
            audio_data = audio_data.reshape(-1, params.nchannels).mean(axis=1).astype(np.int16)
            wf.setnchannels(1)
        else:
            wf.setnchannels(params.nchannels)

        # Set the sample width and framerate
        wf.setsampwidth(min(params.sampwidth, 2))
        wf.setframerate(params.framerate * 3)  # Speed up by 3x
        wf.setnframes(len(audio_data))
        wf.writeframes(audio_data.tobytes())

# Function to generate a unique output filename
def generate_output_filename(base_name="user_piano_sequence", extension=".wav"):
    counter = 1
    while True:
        output_file = f"{base_name}_{counter}{extension}"
        if not os.path.exists(output_file):
            return output_file
        counter += 1

# Main function encapsulating the core logic
def main():
    # Check if sound directory exists
    if not os.path.exists(sound_directory):
        print(f"Error: The sound directory '{sound_directory}' does not exist.")
        exit(1)

    # Get user input
    user_input = input("Enter a sequence of up to 1000 characters (a-z): ").lower().strip()

    # Ensure input is valid and within the allowed length
    user_input = ''.join(filter(lambda x: x in char_to_sound, user_input))[:1000]

    # Combine audio segments
    combined_audio = np.array([], dtype=np.int16)
    params = None

    for char in user_input:
        sound_file = char_to_sound.get(char)
        if sound_file:
            audio_data, file_params = read_wav(sound_file)
            if audio_data is not None:
                if params is None:
                    params = file_params
                combined_audio = np.concatenate((combined_audio, audio_data))

    # Generate the unique output filename
    output_file = generate_output_filename()

    # Save the combined audio to a uniquely named file
    if params and len(combined_audio) > 0:
        write_wav(output_file, combined_audio, params)
        print(f"Your piano sequence has been saved as '{output_file}'.")
    else:
        print("No valid audio data found. Nothing to save.")

# Entry point of the script
if __name__ == '__main__':
    main()







