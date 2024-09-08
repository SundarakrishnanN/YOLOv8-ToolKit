import cv2
import os


def extract_frames(video_path, output_folder, frame_skip):
   
    vid_path = video_path.strip('videos\\')
    vid_path = vid_path.strip('.mp4')
    print(vid_path)
    print(output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_frame_count = 0
    success = True

    

    while success:
  
        success, frame = cap.read()

        if success:
         
            if frame_count % frame_skip == 0:
                frame_filename = os.path.join(output_folder, f"{vid_path}_frame_{saved_frame_count:05d}.jpg")
                cv2.imwrite(frame_filename, frame)
                saved_frame_count += 1

            frame_count += 1

    cap.release()
    print(f"Extracted {saved_frame_count} frames to {output_folder}")


vid_path_input = "Video Path"

video_path = vid_path_input
output_folder = "Path where you wish to store the frames"
frame_skip = 50  

extract_frames(video_path, output_folder, frame_skip)
