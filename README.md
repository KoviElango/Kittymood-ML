Kitty Mood
Kitty Mood is a machine learning project designed to recognize and classify the moods of your cat based on images. The project fine-tunes the MobileNetV2 model to identify six distinct cat moods: angry, calm, focused, grooming, playful, and sleepy.

Features
Cat Mood Classification: Predicts your cat's mood from images.
Six Moods Recognized: Angry, calm, focused, grooming, playful, and sleepy.
Data Augmentation: Enhances model robustness.
Pre-trained Model: Built on MobileNetV2 for efficiency and accuracy.

Prerequisites
Python 3.8+
TensorFlow 2.x
OpenCV
NumPy

Model Architecture
Base Model: MobileNetV2 (pre-trained on ImageNet)
Fine-tuned Layers: GlobalAveragePooling2D, Dropout, Dense with softmax activation.
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
