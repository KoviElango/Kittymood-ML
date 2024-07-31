from utils import predict_mood
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Cat Mood Recognition')
parser.add_argument('image_path', type=str, help='Path to the image of the cat')
args = parser.parse_args()

# Predict mood
mood = predict_mood(args.image_path)
print(f'The cat is {mood}.')
