from ultralytics import YOLO
import argparse

def load_model():
    model = YOLO("yolov8l-seg.pt")
    return model

def identify(model, image_path):
    return model.predict(source = image_path, save = True, save_txt = True)

def main():
    parser = argparse.ArgumentParser(description = "Identify objects in an image")
    parser.add_argument("image_path", help = "Path to the image to identify")
    args = parser.parse_args()
    
    model = load_model()
    results = identify(model, args.image_path)
    print(results)

if __name__ == "__main__":
    main()

