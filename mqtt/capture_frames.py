import cv2
cap = cv2.VideoCapture(0)
def capture_frames(count=10):
    frames = []
    for _ in range(count):
        ret, frame = cap.read()
        frames.append(frame)
    return frames

if __name__ == "__main__":
    print(capture_frames(3))