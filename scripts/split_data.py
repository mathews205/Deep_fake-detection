import os
import glob
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(src_dir, train_dir, val_dir, test_dir, split_ratios=(0.7, 0.2, 0.1)):
    # Get all images in the source directory
    images = glob.glob(f"{src_dir}/*.jpg")
    train, temp = train_test_split(images, test_size=(1 - split_ratios[0]))
    val, test = train_test_split(temp, test_size=(split_ratios[2] / (split_ratios[1] + split_ratios[2])))

    # Ensure output directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Move images to corresponding directories
    for file in train:
        shutil.move(file, os.path.join(train_dir, os.path.basename(file)))
    for file in val:
        shutil.move(file, os.path.join(val_dir, os.path.basename(file)))
    for file in test:
        shutil.move(file, os.path.join(test_dir, os.path.basename(file)))

if __name__ == "__main__":
    base_path = r"C:\Users\mathe\Documents\deepfake_detection"

    # Define source directories for 'real' and 'fake' images
    real_src_dir = r"C:\Users\mathe\Documents\deepfake_detection\Frames_extracted\real"
    fake_src_dir = r"C:\Users\mathe\Documents\deepfake_detection\Frames_extracted\fake"

    # Splitting frames for real images
    split_dataset(
        real_src_dir,
        os.path.join(base_path, "frames", "train", "real"),
        os.path.join(base_path, "frames", "val", "real"),
        os.path.join(base_path, "frames", "test", "real"),
    )

    # Splitting frames for fake images
    split_dataset(
        fake_src_dir,
        os.path.join(base_path, "frames", "train", "fake"),
        os.path.join(base_path, "frames", "val", "fake"),
        os.path.join(base_path, "frames", "test", "fake"),
    )
