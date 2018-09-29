import cv2
import os

vid_dir = 'videos/'
vid_ext = '.mp4'

training_img_dir = 'training_imgs/'
testing_img_dir = 'testing_imgs/'

frame_count = 3  # 1 in <frame_count> frames will actually be processed and saved
testing_frame_count = 4  # 1 in <testing_frame_count> of processed frames will be placed in a testing directory


def main():
    if not os.path.exists(training_img_dir):
        os.makedirs(training_img_dir)
    if not os.path.exists(testing_img_dir):
        os.makedirs(testing_img_dir)

    files = os.listdir(vid_dir)
    videos = []
    for file in files:
        name, ext = os.path.splitext(file)
        if ext == vid_ext:
            videos.append(vid_dir + file)

    print('videos to be processed')
    print(videos)

    count = 0
    for video in videos:
        vid_cap = cv2.VideoCapture(video)
        success, image = vid_cap.read()
        while success:
            if count % (frame_count * testing_frame_count) == 0:
                cv2.imwrite(testing_img_dir + f'frame{count}.jpg', image)
            elif count % frame_count == 0:
                cv2.imwrite(training_img_dir + f'frame{count}.jpg', image)
            count += 1
            success, image = vid_cap.read()
            if not success:
                print(f'{video} finished')
                print(f'{count} frames so far')


if __name__ == '__main__':
    main()
