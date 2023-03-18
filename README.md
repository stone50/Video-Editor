# Video Editor
 
## Cut Duplicate Frames
Produces a new .mp4 video file where similar consecutive frames have been cut from the original. The new file will be in the same directory as cut_duplicate_frames.py

**Usage:** cut_duplicate_frames.py \<fileName\> [--threshold] [--no-messages]

**Example:** cut_duplicate_frames.py "input video.mp4" -t=0.9

**Parameters**

- fileName:

    Contains: String

    Description: The name of the video file to cut frames from. This must include the file extension. The file must be located in the same directory as cut_duplicate_frames.py

- threshold (optional):

    Usage: --threshold or -t

    Contains: Float, Range [0, 1], Default = 1

    Description: The percent similarity between consecutive frames for them to be copied
 
    1 = only consecutive frames which are exactly identical will be cut
 
    0 = all frames will be cut

- messages (optional)

    Usage: \<empty\> or --no-messages or -nm

    Contains: Boolean, Default = True

    Description: Whether or not to print messages. If the --no-messages flag is used, this will be False, otherwise this will be True


## Image Similarity
Returns the percent similarity between images. Both images must have the same dimensions

**Usage:** image_similarity.py \<image1FileName\> \<image2FileName\> [--no-messages]

**Example:** image_similarity.py "input image 1.png" "input image 2.png"

**Parameters**

- image1FileName:

    Contains: String

    Description: The name of an image file to compare. This must include the file extension. The file must be located in the same directory as image_similarity.py

- image2FileName:

    Contains: String

    Description: The name of an image file to compare. This must include the file extension. The file must be located in the same directory as image_similarity.py

- messages (optional)

    Usage: \<empty\> or --no-messages or -nm

    Contains: Boolean, Default = True

    Description: Whether or not to print messages. If the --no-messages flag is used, this will be False, otherwise this will be True
    
