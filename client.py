import cv2

# Flask 서버에서 스트리밍하는 비디오 URL
stream_url = "http://127.0.0.1:8000/"

# OpenCV VideoCapture 객체 생성
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # 스트림으로부터 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # 프레임을 윈도우에 표시
    cv2.imshow('Video Stream', frame)

    # 'q' 키를 누르면 루프 탈출
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
