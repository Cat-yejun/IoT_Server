from flask import Flask, request, Response
import cv2
import numpy as np
import base64
import threading

app = Flask(__name__)

# 전역 변수로 프레임 저장
frame = None

@app.route('/')
def index():
    return Response(open('index.html').read(), mimetype='text/html')

@app.route('/video_feed', methods=['POST'])
def video_feed():
    global frame
    try:
        data = request.json['image']
        image_data = base64.b64decode(data.split(',')[1])
        np_arr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return '', 204
    except Exception as e:
        print(f"Error processing image: {e}")
        return str(e), 500

def display_frame():
    global frame
    while True:
        if frame is not None:
            cv2.imshow('Webcam Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    threading.Thread(target=display_frame).start()
    app.run(host='0.0.0.0', port=8000)
