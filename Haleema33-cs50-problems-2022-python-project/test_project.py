import unittest
import numpy as np
import wave
import os
from project import read_wav, write_wav, generate_output_filename, sound_directory, char_to_sound


class TestPianoSequence(unittest.TestCase):
    # Test for read_wav function
    def test_read_wav(self):
        # Create a test file in the sound_directory
        test_file_path = os.path.join(sound_directory, 'piano_a.wav')
        # Ensure the file exists before running the test
        if not os.path.isfile(test_file_path):
            self.skipTest(f"Test skipped: file '{test_file_path}' does not exist.")

        # Test reading a valid file
        audio_data, params = read_wav(test_file_path)
        self.assertIsNotNone(
            audio_data, "Audio data should not be None for a valid file.")
        self.assertIsNotNone(
            params, "Params should not be None for a valid file.")

        # Test reading a non-existing file
        invalid_file_path = os.path.join(
            sound_directory, 'non_existent_file.wav')
        audio_data, params = read_wav(invalid_file_path)
        self.assertIsNone(
            audio_data, "Audio data should be None for a non-existent file.")
        self.assertIsNone(
            params, "Params should be None for a non-existent file.")

    # Test for write_wav function
    def test_write_wav(self):
        # Create sample data for testing
        sample_data = np.array([0, 1, -1, 32767, -32768], dtype=np.int16)
        params = wave._wave_params(nchannels=1, sampwidth=2, framerate=44100, nframes=len(
            sample_data), comptype='NONE', compname='not compressed')
        output_file = "test_output.wav"

        # Write the sample data to a file
        write_wav(output_file, sample_data, params)

        # Check if the file was created
        self.assertTrue(os.path.exists(output_file),
                        "Output file was not created.")

        # Clean up the test file
        if os.path.exists(output_file):
            os.remove(output_file)

    # Test for generate_output_filename function
    def test_generate_output_filename(self):
        # Generate the first filename
        filename1 = generate_output_filename()

        # Create a temporary file to simulate file existence
        with open(filename1, 'w') as f:
            f.write("")  # Just create an empty file

        # Generate the second filename
        filename2 = generate_output_filename()

        # Assert the filenames are unique
        self.assertNotEqual(filename1, filename2,
                            "Generated filenames should be unique.")

        # Clean up the created file
        if os.path.exists(filename1):
            os.remove(filename1)

    # Test for dictionary mapping characters to their sound files
    def test_char_to_sound(self):
        for char in char_to_sound:
            expected_file = os.path.join(sound_directory, f'piano_{char}.wav')
            self.assertEqual(char_to_sound[char], expected_file, f"Sound file path for '{char}' is incorrect.")

    # Test for the sound_directory existence
    def test_sound_directory_exists(self):
        self.assertTrue(os.path.exists(sound_directory), f"Sound directory '{sound_directory}' does not exist.")

# Entry point for running tests
if __name__ == "__main__":
    unittest.main()
