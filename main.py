import os
import csv

file_path = os.path.join( "Resources", "best_corgies.csv")

with open(file_path) as fh:
    reader = csv.reader(fh)
    for cur_row in reader:
        print(cur_row)
