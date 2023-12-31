'''import asyncio
import concurrent.futures
import cv2

async def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video Player', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

async def main():
    video_path = 'prueba.mp4'  # Reemplaza con la ruta de tu video

    play_video(video_path)
    print('hellor word')
asyncio.run(main())'''
import asyncio
import cv2
async def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow('Video Player', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

