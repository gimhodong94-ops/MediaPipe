#!/usr/bin/env python
# 위 줄은 파이썬 인터프리터를 지정합니다.
# -*- coding: utf-8 -*-  # 파일 인코딩을 UTF-8로 지정합니다.
import cv2  # 영상 입력과 화면 출력을 위해 OpenCV를 불러옵니다.
import mediapipe as mp  # MediaPipe 솔루션을 사용하기 위해 불러옵니다.
mp_face_detection = mp.solutions.face_detection  # 얼굴 검출 솔루션을 가져옵니다.
mp_drawing = mp.solutions.drawing_utils  # 검출 결과를 그릴 도구를 가져옵니다.
face_detection = mp_face_detection.FaceDetection(  # 얼굴 검출기를 생성합니다.
    model_selection=0,  # 근거리 얼굴 검출 모델을 선택합니다.
    min_detection_confidence=0.5  # 최소 얼굴 검출 신뢰도를 설정합니다.
)  # 얼굴 검출기 생성을 마칩니다.
cap = cv2.VideoCapture("face.mp4")  # 현재 폴더의 face.mp4 파일을 엽니다.
print("얼굴 검출을 시작합니다. ESC 키를 눌러 종료하세요.")  # 시작 안내를 출력합니다.
while cap.isOpened():  # 영상 파일이 열려 있는 동안 반복합니다.
    success, image = cap.read()  # 다음 프레임을 읽습니다.
    if not success:  # 프레임을 읽지 못했는지 확인합니다.
        print("프레임을 읽지 못했습니다. face.mp4 파일을 확인하세요.")  # 읽기 실패 원인을 안내합니다.
        break  # 반복을 종료합니다.
    image = cv2.flip(image, 1)  # 화면을 좌우 반전합니다.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR 영상을 RGB로 변환합니다.
    result = face_detection.process(image_rgb)  # 현재 프레임에서 얼굴을 검출합니다.
    if result.detections:  # 얼굴 검출 결과가 있는지 확인합니다.
        for detection in result.detections:  # 검출된 얼굴을 하나씩 처리합니다.
            mp_drawing.draw_detection(image, detection)  # 얼굴 경계 상자와 주요 지점을 그립니다.
    cv2.imshow("MediaPipe Face Detector", image)  # 검출 결과 프레임을 화면에 표시합니다.
    if cv2.waitKey(5) & 0xFF == 27:  # ESC 키를 눌렀는지 확인합니다.
        print("종료합니다.")  # 종료 안내를 출력합니다.
        break  # 반복을 종료합니다.
cap.release()  # 영상 파일을 닫고 자원을 해제합니다.
face_detection.close()  # 얼굴 검출기의 자원을 해제합니다.
cv2.destroyAllWindows()  # OpenCV 창을 모두 닫습니다.