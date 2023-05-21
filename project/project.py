import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.color import rgb2lab
import time

class MeanShift:
    def __init__(self, bandwidth=1.0, tau=0.01):
        self.bandwidth = bandwidth
        self.tau = tau

    def distance(self, p1, p2):
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def flat_kernel(self, distance):
        return int(distance <= self.bandwidth)

    def mean_shift(self, data):
        num_samples = len(data)
        modes = []

        for i in range(num_samples):
            mode = data[i].copy()
            converged = False

            while not converged:
                new_mode = np.zeros_like(mode, dtype=float)
                total_weight = 0.0

                for j in range(num_samples):
                    dist = self.distance(mode, data[j])
                    weight = self.flat_kernel(dist)
                    new_mode += weight * data[j]
                    total_weight += weight

                if total_weight == 0:
                    break

                new_mode /= total_weight

                if self.distance(mode, new_mode) < self.tau:
                    converged = True
                else:
                    mode = new_mode

            modes.append(new_mode)

        return modes

    def mean_shift_clustering(self, data):
        modes = self.mean_shift(data)

        # Remove modes with only one pixel
        modes = [mode for mode in modes if len(mode) > 1]

        return modes

    def segment_image(self, image):
        # Convert the image to LAB color space
        lab_image = rgb2lab(image)

        # Convert the LAB image to a numpy array
        image_array = np.array(image)

        # Reshape the LAB image to a 2D array of pixels
        pixels = image_array.reshape(-1, 3)

        # Perform mean shift clustering on the LAB values
        modes = self.mean_shift_clustering(pixels)

        # Create a segmented image with highlighted segments
        segmented_image = np.zeros_like(pixels)
        for i, mode in enumerate(modes):
            segment_color = np.array(mode).astype(int)
            segmented_image[np.where((pixels == segment_color).all(axis=1))] = segment_color

        # Reshape the segmented image back to the original shape
        segmented_image = segmented_image.reshape(image_array.shape)

        return segmented_image

    def plot_segmentation(self, image, segmented_image):
        # Visualize the segmented image
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        fig.suptitle(f"Image Segmentation with bandwidth = {self.bandwidth} and tau = {self.tau}")

        ax[0].imshow(image)
        ax[0].set_title('Original Image')
        ax[0].axis('off')

        ax[1].imshow(segmented_image)
        ax[1].set_title('Segmented Image')
        ax[1].axis('off')

        plt.show()


# Load the image
filename = 'bay_10.png'
image_path = '/home/enigma/Desktop/dm2023/project/' + filename
image = Image.open(image_path)

mean_shift = MeanShift(bandwidth=0.2, tau=0.1)


# Measure the running time
start_time = time.time()

# Perform segmentation
segmented_image = mean_shift.segment_image(image)

end_time = time.time()
running_time = end_time - start_time
print("Running time: %.2f seconds" % running_time)

# Visualization
mean_shift.plot_segmentation(image, segmented_image)
