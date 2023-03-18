import argparse
import cv2
import numpy as np

def get_image_similarity(image1: np.ndarray, image2: np.ndarray) -> float:
    return 1 - np.sum(image1 - image2) / (image1.size * 255)

def image_similarity(image1FileName: str, image2FileName: str, printMessages: bool = True) -> float:
    similarity = get_image_similarity(cv2.imread(image1FileName), cv2.imread(image2FileName))
    if printMessages:
        print(f"Similarity: {similarity:.2%}")
    return similarity

if __name__ == "__main__":
    
    # setup argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("image1FileName", type=str, help="name of the first image file including the file extension")
    parser.add_argument("image2FileName", type=str, help="name of the second image file including the file extension")
    parser.add_argument("--no-messages", "-nm", dest="messages", action="store_false", help="do not print messages")
    
    # parse arguments
    args = parser.parse_args()
    
    # cut duplicate frames
    image_similarity(
        args.image1FileName,
        args.image2FileName,
        args.messages
    )
