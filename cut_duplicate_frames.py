
import sys
import cv2
import numpy as np

# put the given milliseconds into the format H:MM:SS:mmm
def format_time(milliseconds: int):
    return f"{milliseconds // 3_600_000}:{milliseconds // 60_000 % 60:0>2d}:{milliseconds // 1_000 % 60:0>2d}.{milliseconds % 1_000:0<3d}"

# get command line argument values
INPUT_FILE_NAME = sys.argv[1]
DIFFERENCE_THRESHOLD = sys.argv[2] if len(sys.argv) > 2 else 0.001

# open the input video
inputVideo = cv2.VideoCapture(INPUT_FILE_NAME)

# initialize variables for processing the input video
INPUT_VIDEO_FRAME_COUNT = int(inputVideo.get(cv2.CAP_PROP_FRAME_COUNT))
INPUT_VIDEO_FPS = int(inputVideo.get(cv2.CAP_PROP_FPS))
success, frame = inputVideo.read()
if not success:
    print(f"Error reading {INPUT_FILE_NAME}")
    inputVideo.release()
    sys.exit()
MAX_COLOR_SUM = frame.size * 255
previousFrame = frame
framesCopied = 0

# open the output video
outputVideo = cv2.VideoWriter(
    f"{INPUT_FILE_NAME}_cut.mp4",
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
    print(f"\rVideo Time Elapsed: {format_time(int(inputVideo.get(cv2.CAP_PROP_POS_MSEC)))}\t( {inputVideo.get(cv2.CAP_PROP_POS_FRAMES) / INPUT_VIDEO_FRAME_COUNT:.2%} )", end="")
    
    # copy the frame to the output video if it is different than the previous frame
    if np.sum(frame - previousFrame) / MAX_COLOR_SUM > DIFFERENCE_THRESHOLD:
        outputVideo.write(frame)
        previousFrame = frame
        framesCopied += 1
    
    # read the next frame
    success, frame = inputVideo.read()

# print results
print('\n')
print(f"New Video Length: {format_time(int(framesCopied * 1_000 / INPUT_VIDEO_FPS))}")

# cleanup
inputVideo.release()
outputVideo.release()