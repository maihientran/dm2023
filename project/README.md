Project Data Mining 2023
=====================================
Topic: image instance segmentation using Mean-shift clustering
    Input: RGB image
    Output: instance segmented image with highlighted segments

-----------------------
* Student: Tran Thi Hien Mai
* ID: M22.ICT.004

# Image Segmentation using Mean Shift Clustering

This project demonstrates image segmentation using the mean shift clustering algorithm. It takes an input image and performs segmentation to group similar pixels together based on their color information.

## Requirements

- Python 3.6 or above
- NumPy
- Matplotlib
- PIL (Python Imaging Library)
- scikit-image

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries by running the following command:
    ```pip install -r requirements.txt```


## Usage

1. Place your input image in the project directory.
2. Open the `mean_shift_segmentation.py` file.
3. Modify the `filename`, `bandwidth`, and `tau` variables as desired.
4. Run the script using the following command:
    python project.py

5. The segmented image will be displayed, showing the original image and the segmented image side by side.

## Explanation

The project consists of the following files:

- `project.py`: The main Python script that performs image segmentation using the mean shift clustering algorithm.
- `README.md`: This file, providing an overview of the project and instructions for usage.
- `requirements.txt`: A text file listing the required Python libraries and their versions.
- `painting_5.jpg`: An example input image used for demonstration purposes.

The mean shift clustering algorithm is implemented in an object-oriented manner using the `MeanShift` class. The class provides methods for distance calculation, flat kernel computation, mean shift iterations, and clustering. It also includes a method for segmenting the input image and visualizing the segmented image.

To perform image segmentation, the `segment_image` method is called with the input image as the argument. The method converts the image to the LAB color space, reshapes it to a 2D array of pixels, and applies the mean shift clustering algorithm to group similar pixels together. The resulting segmented image is then reshaped back to the original shape.

The `plot_segmentation` method is used to visualize the original and segmented images side by side using Matplotlib.

You can adjust the `bandwidth` and `tau` parameters in the `project.py` file to control the level of segmentation and fine-tune the results according to your requirements.
