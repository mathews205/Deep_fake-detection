import cv2
import os

def extract_frames(video_dir, output_dir, frame_rate=1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    videos = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    for video in videos:
        video_path = os.path.join(video_dir, video)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        success = True
        while success:
            success, frame = cap.read()
            if not success:
                break
            if frame_count % (30 * frame_rate) == 0:  # Extract 1 frame per second
                frame_name = f"{os.path.splitext(video)[0]}_frame_{frame_count}.jpg"
                cv2.imwrite(os.path.join(output_dir, frame_name), frame)
            frame_count += 1
        cap.release()

if __name__ == "__main__":
    base_path = r"C:\Users\mathe\Documents\deepfake_detection"
    extract_frames(os.path.join(base_path, "dataset", "real"), os.path.join(base_path, "Frames_extracted", "real"))
    extract_frames(os.path.join(base_path, "dataset", "fake"), os.path.join(base_path, "Frames_extracted", "fake"))