# predator-implementation
Re-implements the GIMP "Predator" image transformation in python using the cv library.

# algorithm details
This image transformation follows these three steps:
1 - "pixelize" (average pixels in an X by X area, the size of which is defined by the user) (currently unimplemented)
2 - "min/max RGB" (finds the smallest or largest of the R, G, B values and set the others to zero)
3 - sobel edge-detect

# running the program
At present, this program must be run in the terminal window.
Make sure to chmod the file if you want to run it without the python3 command!

command for changed mode: \[user@domain]$ ./predator.py image-path k-value minmax

command for unchanged mode:\[user@domain]$ python predator.py image-path k-value minmax

image-path - path to a desired image
k-value - the k-value needed by the sobel transformation. A higher value results in thicker edges.
minmax - "min" or "max", chooses whether to select the minimum or maximum RGB value for each pixel
