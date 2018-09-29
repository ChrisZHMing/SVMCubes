import dlib
import os

testing_dir = 'testing_imgs/'
image_ext = '.jpg'
detector_name = 'detector.svm'


def main():
    if not os.path.exists(testing_dir):
        print("Testing dir does not exist")
        exit(1)

    files = os.listdir(testing_dir)
    images = []
    for file in files:
        name, ext = os.path.splitext(file)
        if ext == image_ext:
            images.append(testing_dir + file)

    detector = dlib.simple_object_detector(detector_name)
    win = dlib.image_window()
    for image in images:
        img = dlib.load_rgb_image(image)
        dets = detector(img)
        win.clear_overlay()
        win.set_image(img)
        win.add_overlay(dets)
        dlib.hit_enter_to_continue()


if __name__ == '__main__':
    main()