import tensorflow as tf
import numpy as np
import cv2

# Load the model
model = tf.keras.models.load_model('/app/models/cat_mood_model.keras')

# Preprocess image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150, 150))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Predict mood
def predict_mood(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    class_names = ['angry', 'calm', 'focused', 'groom', 'playful', 'sleepy']
    return class_names[np.argmax(prediction)]
