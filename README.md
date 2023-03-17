# Video Editor
 
## Cut Duplicate Frames
Produces a new .mp4 video file where similar consecutive frames have been removed

**Usage:** C:\Video Editor>python3 cut_duplicate_frames.py \<file name\> \<difference threshold\>

**Example:** C:\Video Editor>python3 cut_duplicate_frames.py "input video.mp4" 0.01

**Parameters**

- file name: The name of the file to cut frames from. This must include the file extension. The file must be located in the same directory as cut_duplicate_frames.py

- difference threshold (optional): The percent difference consecutive frames have to be to get copied to the new video.

  Default = 0.001
 
  1 = consecutive frames must be entirely different (this can result in an empty video)
 
  0 = consecutive frames can have any difference (this can result in an exact copy of the original video)
