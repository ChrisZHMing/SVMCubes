SVMCubes
========

This project trains and tests an SVM based object detector.
The example used here detects Power Cubes, the game object for the 2018 FRC game, milk crates covered in yellow cloth covers.
The detector as currently trained is not 100% accurate.
Many of the files in testing_imgs/ are not successfully detected.
dlib is used for the object detection, and openCV is used to setup the training data.
Each python file has a specific role in the process of training and testing:

#### video_handler.py

video_handler.py takes video files placed in the 'videos' directory (or wherever the code specifies)
and pulls frames from the video to use for training. Input and output directories are configurable in the code

#### marking_tool.py

marking_tool.py takes images from any number of directories and presents them to user for marking the object location.
Currently only configured for a single object per image.
Marking is done by clicking once for each edge of the object, starting with the top and working in a clockwise direction.
Pressing 'n' saves object location and moves to the next file.
Pressing 'r' resets the current object location for the image.
Pressing 's' skips the current image without saving any data.
Pressing 'q' quits the entire program.

#### trainer.py

trainer.py actually trains the object detector. The detector will be saved to a file.

#### tester.py

tester.py shows each image on the screen, with an overlay for whatever is detected by the object detector.
Hit enter after each file to progress to the next one.
Images are selected from whatever directory is configured in the code.

## Make your own

To configure your own object detector, replace the video files in the 'videos' directory with your own short videos of an object.
Then run `python video_handler.py`, then `python marking_tool.py`. Follow the instructions above to mark your images.
Run `python trainer.py`, then `python tester.py` to verify your detector. Adjust settings in trainer.py and re-run if needed.
Use tester.py as an example to implement object detection in your own code.

---

Note: this project is configured for PyCharm by Jetbrains, with a virtual environment containing all modules used. 