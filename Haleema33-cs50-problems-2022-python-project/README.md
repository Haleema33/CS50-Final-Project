
# PROJECT TITLE: Text into Piano

#### Video Demo: https://www.youtube.com/watch?v=0YkL6s_3IMA
#### Description:
This project allows the user to input a sequence of characters (a-z), and generates a unique audio file composed of piano sounds corresponding to those characters. The system reads sound files from a predefined directory, processes them, and outputs a new WAV file with the audio sequence. The audio is speeded up 3x for an accelerated playback.

---

## Features
- **Character to Sound Mapping**: Maps each letter of the alphabet (a-z) to a corresponding piano sound file.
- **Read and Write WAV Files**: Reads WAV files, processes the audio, and writes the combined audio sequence into a new file.
- **Speed Adjustment**: The final output is sped up by 3x for a faster playback experience.
- **Unique Output Filename**: Automatically generates a unique filename for each new output to prevent overwriting.

---

## Requirements
The following Python libraries are required to run this project:

- `numpy`: For handling audio data manipulation.
- `wave`: Part of Python's standard library to read and write WAV files.
- `os`: Part of Python's standard library for file and directory operations.

To install the necessary libraries, you can run:

```bash
pip install numpy
```

Since `wave` and `os` are part of Python's standard library, no additional installation is required for them.

---

## Setup
1. Ensure that you have a directory named `sounds` in the same directory as this script, containing WAV files named `piano_a.wav`, `piano_b.wav`, ..., `piano_z.wav`.
2. You can adjust the directory path or the naming scheme in the `char_to_sound` dictionary if needed.

---

## Usage
1. **Run the Script**: Execute the script using Python:

```bash
python your_script_name.py
```

2. **Input**: The script will prompt you to enter a sequence of characters (a-z). The input will be converted to lowercase, and only valid characters (a-z) will be considered.
3. **Output**: The script will create a new WAV file containing the combined sounds of the input characters, with a unique filename to avoid overwriting previous outputs. The output will be sped up by 3x.
4. **Sound Directory Check**: If the `sounds` directory is not found, the script will terminate with an error message.

---

## Code Explanation

- **`char_to_sound`**: A dictionary that maps each character (a-z) to its corresponding piano sound file located in the `sounds` directory.
- **`read_wav(file_path)`**: Reads a WAV file and returns its audio data and parameters.
- **`write_wav(file_path, audio_data, params)`**: Writes the combined audio data to a new WAV file, adjusting the speed by 3x.
- **`generate_output_filename()`**: Generates a unique filename to avoid overwriting any existing files.
- **`main()`**: The main function of the script that orchestrates the user input, reading of sound files, combining the audio, and saving the output.

---

## Example

For example, if you input the string `"abc"`, the program will generate an audio file with the piano sounds of "a", "b", and "c" played in sequence, and the output file might be named `user_piano_sequence_1.wav`.

