# predator-implementation
Re-implements the GIMP "Predator" image transformation in python using the cv library.

# algorithm details
This image transformation follows these three steps:

1 - "pixelize" (average pixels in an X by X area, the size of which is defined by the user)

2 - "min/max RGB" (finds the smallest or largest of the R, G, B values and set the others to zero)

3 - sobel edge-detect

# running the program
At present, this program must be run in the terminal window.
Make sure to chmod the file if you want to run it without the python command!

command for changed mode: \[user@domain]$ ./predator.py image-path \[k-value] \[scale] \[minmax] \[pixelize]

command for unchanged mode:\[user@domain]$ python predator.py image-path \[k-value] \[scale] \[minmax] \[pixelize]

image-path - path to a desired image. This is the only required argument.

k-value - the k-value needed by the sobel transformation. A higher value results in thicker edges. - default of 3

scale - the scale value used in the sobel transformation. A higher value results in brighter edges. - default of 1

minmax - "min" or "max", chooses whether to select the minimum or maximum RGB value for each pixel - default of "min"

pixelize - the X of the pixelize step's X by X area - default of 3

# image details
Included in this repository is an example image to put through the transformation, as well as the output of the image when the default values are used.
