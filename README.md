# 12_image_resize

This script resizing the images by given dimensions and saving it.<br /><br />

Script gets for input next parameters:<br />
Required:<br />
-image [path_to_original_image]<br />
Optional:<br />
-width [width_to_resize]<br />
-height [height_to_resize] <br />
-scale [scale_to_resize] <br />
-output [path_to_save_result] <br />

#Rules:
If given only "width" then "height" will be recalculated to save proportions and in reverse.<br />
If given "scale" then "width" and "height" must be missing in other way you will get an error message.<br />
By default image will be saved near the origin image.<br />

# How to run:<br />
1. Run the program: <br />
python image_resize.py -image \<path_to_original_image\> -scale 2 -output \<path_to_result_folder\> <br />
or <br />
python image_resize.py -image \<path_to_original_image\> -width 1000 <br />
2. Program will print path to the new resided image. Example:<br />
"New image created and saved in D:\images\image_17x10.jpg"


