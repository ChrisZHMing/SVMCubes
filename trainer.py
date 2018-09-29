import os
import dlib

training_dir = 'training_imgs/'
testing_dir = 'testing_imgs/'
file_name = 'data.xml'
detector_name = 'detector.svm'


def main():
    options = dlib.simple_object_detector_training_options()
    options.add_left_right_image_flips = True
    options.C = 4
    options.epsilon = 0.05
    options.num_threads = 8
    options.be_verbose = True

    training_xml_path = os.path.join(training_dir, file_name)
    testing_xml_path = os.path.join(testing_dir, file_name)

    dlib.train_simple_object_detector(training_xml_path, detector_name, options)

    print("")
    print("================================")
    print("")
    print(f'Training accuracy: {dlib.test_simple_object_detector(testing_xml_path, detector_name)}')


if __name__ == '__main__':
    main()
