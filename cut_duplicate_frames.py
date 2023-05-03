
import argparse
import cv2
from utils import format_time
from image_similarity import get_image_similarity


def cut_duplicate_frames(inputFileName: str, similarityThreshold: float = 1, printMessages: bool = True):

    # open the input video
    inputVideo = cv2.VideoCapture(inputFileName)

    # initialize variables for processing the input video
    INPUT_VIDEO_FRAME_COUNT = int(inputVideo.get(cv2.CAP_PROP_FRAME_COUNT))
    INPUT_VIDEO_FPS = int(inputVideo.get(cv2.CAP_PROP_FPS))
    success, frame = inputVideo.read()
    if not success:
        inputVideo.release()
        raise FileNotFoundError(f"Error reading {inputFileName}")
    previousFrame = frame
    framesCopied = 0

    # open the output video
    outputVideo = cv2.VideoWriter(
        f"{inputFileName}_cut.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        INPUT_VIDEO_FPS,
        (
            int(inputVideo.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(inputVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
    )

    # process the input video
    success, frame = inputVideo.read()
    while success:

        # print progress
        if printMessages:
            print(
                f"\rVideo Time Elapsed: {format_time(int(inputVideo.get(cv2.CAP_PROP_POS_MSEC)))}\t( {inputVideo.get(cv2.CAP_PROP_POS_FRAMES) / INPUT_VIDEO_FRAME_COUNT:.2%} )", end="")

        # copy the frame to the output video if it is different than the previous frame
        if get_image_similarity(frame, previousFrame) < similarityThreshold:
            outputVideo.write(frame)
            previousFrame = frame
            framesCopied += 1

        # read the next frame
        success, frame = inputVideo.read()

    # print results
    if printMessages:
        print('\n')
        print(
            f"New Video Length: {format_time(int(framesCopied * 1_000 / INPUT_VIDEO_FPS))}")

    # cleanup
    inputVideo.release()
    outputVideo.release()


if __name__ == "__main__":

    # setup argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fileName",
        type=str,
        help="name of the video file including the file extension"
    )
    parser.add_argument(
        "--threshold",
        "-t",
        type=float,
        default=1,
        help="similarity threshold (1 = cut only exact duplicates, 0 = cut all frames)"
    )
    parser.add_argument(
        "--no-messages",
        "-nm",
        dest="messages",
        action="store_false",
        help="do not print messages"
    )

    # parse arguments
    args = parser.parse_args()

    # cut duplicate frames
    cut_duplicate_frames(
        args.fileName,
        args.threshold,
        args.messages
    )
