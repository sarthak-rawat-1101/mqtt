from crypt import methods
from flask import Flask, render_template, request, redirect,session,Response
import os
from deepface import DeepFace
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# while(True):
#     ret,frame = camera.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# camera.release()
# cv2.destroyAllWindows()


# # cap2 = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("home/dash.html",segment='index')


# verify = DeepFace.find("data/13.jpg", db_path="data/db",enforce_detection=False)
# verify = DeepFace.verify("data/4.jpg","data/5.jpg" ,enforce_detection=False)

# print(verify)

if __name__ == "__main__":
    app.run(threaded=True)