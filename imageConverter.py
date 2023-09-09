import cv2


class ImageToAsciiArt(object):
    def __init__(self):
        self.ASCII_CHARS = " .,'`\"^:;-~+*i|!1lI?COQ0MWB8%$@#"
        self.ASCII_CHAR_COUNT = len(self.ASCII_CHARS)

    def scale_image(self, image, new_width=100):
        (original_width, original_height) = image.shape[1], image.shape[0]
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio)
        new_image = cv2.resize(image, (new_width, new_height))
        return new_image

    def convert_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def map_pixel_to_ascii(self, pixel_value, range_width=25):
        ascii_index = pixel_value // range_width
        return self.ASCII_CHARS[ascii_index]

    def convert_image_to_ascii(self, image, new_width=100):
        image = self.scale_image(image, new_width)
        image = self.convert_grayscale(image)
        ascii_lines = []

        for y in range(image.shape[0]):
            ascii_line = ""
            for x in range(image.shape[1]):
                pixel = image[y, x]
                ascii_char = self.map_pixel_to_ascii(pixel)
                ascii_line += ascii_char
            ascii_lines.append(ascii_line)

        return "\n".join(ascii_lines)

    def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            if not ret:
                break
            elif cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ascii_art = self.convert_image_to_ascii(frame)
            print(ascii_art)

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    converter = ImageToAsciiArt()
    converter.run()
