import pandas
import time

emails = pandas.read_csv("Emails.csv")
rawtext = list(emails['RawText'])
capital_letters = []

start_time = time.time()

for text in rawtext:
    capital_letters.append(len([char for char in text if char.isupper()]))
    
total = time.time() - start_time

print(total)