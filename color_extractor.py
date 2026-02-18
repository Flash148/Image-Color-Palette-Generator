from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


#function that takes image file path as input, opens image with PIL, converts it to RGB format, converts it to a numpy array
def load_image(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    return np.array(image)


# takes image array and reshapes it
def reshape_image(image_array):
    return image_array.reshape(-1, 3)

#extract dominant colors using KMeans clustering
#return percentage of each color in the image
def extract_colors(image_array, num_colors):
    reshaped_image = reshape_image(image_array)
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(reshaped_image)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    counts = np.bincount(labels)
    percentages = counts / len(labels)

    #sort percentages and colors in descending order
    sorted_indices = np.argsort(percentages)[::-1]
    sorted_percentages = percentages[sorted_indices]
    sorted_colors = colors[sorted_indices]

    return sorted_colors.astype(int), sorted_percentages


#function that takes RGB values and returns hex string
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


#test the functions
if __name__ == "__main__":
    image_path = "test_image.jpg" # test image with known colors
    num_colors = 4 # number of colors to extract (we know there are 4 main colors)
    
    print(f"Loading image: {image_path}")
    image_array = load_image(image_path)
    print(f"Image shape: {image_array.shape}")
    
    print(f"Extracting {num_colors} dominant colors...")
    colors, percentages = extract_colors(image_array, num_colors)
    
   

    print("\nExtracted Colors (Hex):")
    for i, color in enumerate(colors, 1):
        hex_color = rgb_to_hex(color)
        print(f"Color {i}: RGB{tuple(color)} | HEX: {hex_color} | Percentage: {percentages[i-1]:.2%}")

        
    print("\nExpected colors should be close to:")
    print("Red: #ff0000")
    print("Green: #00ff00")
    print("Blue: #0000ff")
    print("Yellow: #ffff00")
    