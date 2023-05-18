# Descramble_image
This program uses the pillow, pandas, and sqlite3 libraries to descramble an image. 
It iterates over the lines of a given SQLite database, crops out the corresponding tile from the scrambled image, and places it in the descrambled image.
Eventually, I presented the descrambled image and also a slightly blurred version of it, because it makes the "lines" creates by the pixelation of the scramled image less visible.
How to run:
First, download the libraries pillow and pandas (using pip). No need to install sqlite3 as it is included in Python 2.5 and above.
Then, run the python code regularly (keeping the original arrangement of files and folders is important) and wait for the solution to appear.
