import cv2
import numpy as np
import os

# Path to the hand image
hand_path = "hand.png"

# Create a whiteboard canvas
canvas = np.ones((720, 1280, 3), dtype="uint8") * 255

# Define text and its position
text = "The stars shine bright at night."
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_thickness = 2
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

# Position the text in the center
text_x = (canvas.shape[1] - text_size[0]) // 2
text_y = (canvas.shape[0] + text_size[1]) // 2

# Load the "hand" image (PNG with transparency)
hand_image = cv2.imread(hand_path, cv2.IMREAD_UNCHANGED)

# Check if the hand image was loaded
if hand_image is None:
    print("Error: Hand image not found. Please ensure 'hand.png' is in the current directory.")
    exit()

# Resize the hand image
hand_height, hand_width = 100, 100
hand_image = cv2.resize(hand_image, (hand_width, hand_height))

# Simulate hand-drawing text
for i in range(1, len(text) + 1):
    # Clear the canvas
    frame = canvas.copy()
    
    # Draw partial text
    cv2.putText(frame, text[:i], (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

    # Get hand position
    hand_x = text_x + (text_size[0] // len(text)) * i - hand_width // 2
    hand_y = text_y - 50  # Adjust to position above text

    # Ensure hand stays within the canvas bounds
    if hand_x + hand_width > canvas.shape[1]:
        hand_x = canvas.shape[1] - hand_width
    if hand_y + hand_height > canvas.shape[0]:
        hand_y = canvas.shape[0] - hand_height

    # Overlay hand image on the canvas
    if hand_image.shape[2] == 4:  # Check if the image has an alpha channel
        alpha = hand_image[:, :, 3] / 255.0  # Alpha channel for transparency
        for c in range(0, 3):  # Loop through color channels
            frame[hand_y:hand_y+hand_height, hand_x:hand_x+hand_width, c] = (
                hand_image[:, :, c] * alpha +
                frame[hand_y:hand_y+hand_height, hand_x:hand_x+hand_width, c] * (1 - alpha)
            )
    else:  # If the image doesn't have an alpha channel
        hand_height, hand_width, _ = hand_image.shape
        frame[hand_y:hand_y+hand_height, hand_x:hand_x+hand_width] = hand_image

    # Display frame
    cv2.imshow("Whiteboard Animation", frame)
    cv2.waitKey(100)  # Wait 100ms between frames

# Close the window
cv2.destroyAllWindows()
