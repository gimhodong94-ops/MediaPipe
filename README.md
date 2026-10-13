# MediaPipe 예제 모음

공학설계입문 · 인공지능 기초 수업에서 MediaPipe로 손, 얼굴, 배경 분리를 실습한 코드 모음입니다.

- 이름: [이름]
- 학번: [학번]

## 실행 환경
- Windows, VS Code
- Python 3.12 (가상환경 .venv)
- opencv-python, mediapipe 0.10.21, yt-dlp

## 설치와 실행
1. 이 저장소를 내려받아 폴더를 VS Code로 엽니다.
2. 가상환경을 만들고 들어갑니다.
   py -3.12 -m venv .venv
   .\.venv\Scripts\activate
3. 패키지를 설치합니다.
   pip install -r requirements.txt
4. 영상 파일(hand.mp4, face.mp4)은 용량 때문에 올리지 않았습니다. 같은 폴더에 직접 넣어 주세요. 웹캠이 있으면 코드의 cv2.VideoCapture(0)을 사용합니다.
5. 원하는 파일을 실행합니다. 종료는 ESC 키입니다.
   python hand_detector.py

## 파일 설명
| 파일 | 설명 |
|---|---|
| hand_detector.py | 손 랜드마크 21점 감지 |
| face_detector.py | 얼굴 감지 |
| selfie_segmentation.py | 인물과 배경 분리 후 배경 흐리기 (블러 크기 조절) |
| hand_detector_youtube.py | 유튜브 영상에서 손 감지 |
| requirements.txt | 필요한 패키지 목록 |