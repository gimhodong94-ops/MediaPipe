import cv2
import mediapipe as mp
import yt_dlp

# YouTube 링크에서 재생 가능한 스트림 주소를 뽑는 함수
def get_youtube_stream(url):
    ydl_opts = {
        'quiet': True,                    # 불필요한 로그 제거
        'format': 'bestvideo[ext=mp4]/bestvideo',   # mp4 형식 우선 선택
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['url']

# YouTube 영상 주소 (손이 잘 보이는 영상으로 바꾸기)
youtube_url = "https://www.youtube.com/shorts/Cg-kD8jIflE?feature=share"

print("YouTube 스트림 URL을 가져오는 중...")
video_stream_url = get_youtube_stream(youtube_url)
print("스트림 URL 추출 완료")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# 파일 이름 대신 스트림 주소를 넣는다
cap = cv2.VideoCapture(video_stream_url)

if not cap.isOpened():
    print("YouTube 영상을 열 수 없습니다.")
    exit()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("영상 스트림이 끝났거나 프레임을 읽지 못했습니다.")
        break

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

    cv2.imshow('MediaPipe Hand Detector (YouTube)', image)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()