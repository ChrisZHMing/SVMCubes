import cv2
import os

dirs = ['training_imgs/', 'testing_imgs/']
file_name = 'data.xml'
image_ext = '.jpg'

window_name = 'image'

next_key = 'n'
reset_key = 'r'
quit_key = 'q'
skip_key = 's'

box = []


def click_box(event, x, y, flags, param):
    global box
    if event == cv2.EVENT_LBUTTONDOWN and len(box) < 4:
        if len(box) % 2 == 0:
            box.append(y)
        else:
            box.append(x)


def main():
    global box

    for dir in dirs:
        if not os.path.exists(dir):
            print(f'dir: {dir} does not exist')
            continue

        xml_output = open(dir + file_name, 'w+')
        xml_output.write("<?xml version='1.0' encoding='ISO-8859-1'?>\n")
        xml_output.write("<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>\n")
        xml_output.write("<dataset>\n")
        xml_output.write("  <name>Power Cubes</name>\n")
        xml_output.write("  <comment>Images of power cubes.</comment>\n")
        xml_output.write("  <images>\n")

        files = os.listdir(dir)
        images = []
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == image_ext:
                images.append(file)
        print(images)

        for image_path in images:
            image = cv2.imread(dir + image_path)

            # resize to make sure largest dimension is 640
            r = 640.0 / max(image.shape)
            new_dim = (int(image.shape[1] * r), int(image.shape[0] * r))
            image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

            clone = image.copy()
            cv2.namedWindow(window_name)
            cv2.setMouseCallback(window_name, click_box)

            while True:
                cv2.imshow(window_name, image)
                key = cv2.waitKey(1) & 0xFF

                if key == ord(reset_key):
                    image = clone.copy()
                    box = []

                elif key == ord(next_key):
                    if len(box) < 4:
                        print('Not enough data points')
                        break

                    top = int(min(box[0], box[2]) / r)
                    left = int(min(box[1], box[3]) / r)
                    height = abs(int((box[2] - box[0]) / r))
                    width = abs(int((box[3] - box[1]) / r))

                    xml_output.write(f'  <image file=\'{image_path}\'>\n')
                    xml_output.write(
                        f'    <box top=\'{top}\' left=\'{left}\' width=\'{width}\' height=\'{height}\'/>\n')
                    xml_output.write('  </image>\n')

                    box = []
                    break

                elif key == ord(skip_key):
                    box = []
                    break

                elif key == ord(quit_key):
                    cv2.destroyAllWindows()
                    xml_output.write("  </images>\n")
                    xml_output.write("</dataset>")
                    xml_output.close()
                    exit(0)
                    break

            if len(box) == 4:
                print(box)

            cv2.destroyAllWindows()

        xml_output.write("  </images>\n")
        xml_output.write("</dataset>")
        xml_output.close()


if __name__ == '__main__':
    main()
