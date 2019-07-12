from digital_samples_to_peaks2 import sample_to_peaks
from time import sleep
from input_audio import get_mp3_data, get_mic_data, read_database_file
from fingerprint import

database_name = input("What is the path to the databse?")
database = read_database_file(database_name)

database_dict = database.dictionary

seconds = int(input("How many seconds would you like to record for?\n"))
print("Recording in 3")
sleep(1)
print("2")
sleep(1)
print("1")

mic_data = get_mic_data(seconds)

matches = check_matches(mic_data, database, 44100)

print(matches)