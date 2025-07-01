from PyQt5.QtWidgets import QFileDialog, \
      QApplication, QWidget, QVBoxLayout, \
      QPushButton, QHBoxLayout, QInputDialog, QLabel
from PyQt5.QtGui import QFont
import numpy
import sys
import cv2 as cv

class main():
      def __init__(self):
            self.img = None
            self.name_of_window = "Image"
            self.app = QApplication(sys.argv)
            self.window = QWidget()
            self.v_layout = QVBoxLayout(self.window)
            self.first_buttons()
            self.window.show()
            self.app.exec()

      def get_image_from_web(self):
            hint = QLabel("Чтобы сфотать нажмите на пробел")
            hint.setFont(QFont('Arial', 50))
            hint.show()
            cam = cv.VideoCapture(0)

            img_name = "opencv_frame.png"
            hint = QLabel("Вебка не найдена чтобы решить данную проблему см. README.md")
            hint.setFont(QFont('Arial', 20))
            while True:
                  cv.namedWindow("test")
                  ret, frame = cam.read()
                  if not ret:
                        if self.v_layout.count() == 3:
                              self.v_layout.addWidget(hint)
                        elif self.v_layout.count() == 4:
                              item = self.v_layout.takeAt(3)
                              widget = item.widget()
                              widget.deleteLater()
                              self.v_layout.addWidget(hint)
                              
                        return
                  cv.imshow("test", frame)

                  k = cv.waitKey(1)
                  if k%256 == 32:
                        # SPACE pressed
                        cv.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        break

            cam.release()

            cv.destroyAllWindows()
            self.img = frame
            self.second_buttons()

      def viewImage(self):
            cv.namedWindow(self.name_of_window, cv.WINDOW_NORMAL)
            cv.resizeWindow(self.name_of_window, self.width, self.height)
            cv.imshow(self.name_of_window, self.img)
            cv.waitKey(0)
            cv.destroyAllWindows()

      def rgb(self):
            
            choise = QWidget()
            temp = self.img

            def red_ch():
                  self.img[:, :, 0] = 0
                  self.img[:, :, 1] = 0
                  self.viewImage()
                  choise.close()
            
            def blue_ch():
                  self.img[:, :, 1] = 0
                  self.img[:, :, 2] = 0
                  self.viewImage()
                  choise.close()
                                    
            def green_ch():
                  self.img[:, :, 0] = 0
                  self.img[:, :, 2] = 0
                  self.viewImage()
                  choise.close()

            h_layout = QHBoxLayout(choise)
            red = QPushButton("Красный канал")
            red.clicked.connect(red_ch)
            blue = QPushButton("Синий канал")
            blue.clicked.connect(blue_ch)
            green = QPushButton("Зеленый канал")
            green.clicked.connect(green_ch)
            h_layout.addWidget(red)
            h_layout.addWidget(blue)
            h_layout.addWidget(green)

            choise.show()

      def negative(self):
            self.img = cv.bitwise_not(self.img)
            self.viewImage()

      def increase_brigthness(self):
            beta, ok = QInputDialog.getInt(QWidget(), "Чило хочу", "Введите на сколько хотите повысить яроксть: ", 0, 0)
            if ok:
                  self.img = cv.convertScaleAbs(self.img, alpha=1, beta=beta)
                  self.viewImage()

      def draw_circle(self):
            x, done1 = QInputDialog.getInt(QWidget(), "Координаты круга", "Введите координату x центра круга: ", 0, 0, self.width)
            y, done2 = QInputDialog.getInt(QWidget(), "Координаты круга", "Введите координату y центра круга: ", 0, 0, self.height)
            rad, done3 = QInputDialog.getInt(QWidget(), "Координаты круга", "Введите радиус круга: ", 0, 0)
            if done1 and done2 and done3:
                  cv.circle(self.img, (x, y), rad, (0, 0, 255), 5)
                  self.viewImage()

      def read_file(self):
            temp = QFileDialog.getOpenFileName()
            file = open(temp[0], "rb")
            bytes = bytearray(file.read())
            numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
            self.img = cv.imdecode(numpyarray, cv.IMREAD_UNCHANGED)
            hint = QLabel("Фото не загрузилось")
            hint.setFont(QFont('Arial', 20))
            if self.img is None:
                  if self.v_layout.count() == 3:
                        self.v_layout.addWidget(hint)
                  elif self.v_layout.count() == 4:
                        item = self.v_layout.takeAt(3)
                        widget = item.widget()
                        widget.deleteLater()
                        self.v_layout.addWidget(hint)
                  return
            self.second_buttons()

      def clear_layout(self):
            cv.destroyAllWindows()
            if self.v_layout is not None:
                  while self.v_layout.count():
                        item = self.v_layout.takeAt(0)
                        widget = item.widget()
                        if widget is not None:
                              widget.deleteLater()
                        else:
                              self.clear_layout()

      def go_back(self):
            self.clear_layout()
            self.first_buttons()

      def second_buttons(self):

            self.clear_layout()

            self.height, self.width, self.channels = self.img.shape
            self.height = int(self.height * 0.6)
            self.width = int(self.width * 0.6)
            self.img = cv.resize(self.img, (self.width, self.height))

            show_img = QPushButton("Показать картинку")
            show_img.clicked.connect(self.viewImage)
            show_rgb = QPushButton("Показать канал изображения")
            show_rgb.clicked.connect(self.rgb)
            show_neg = QPushButton("Показать негатив")
            show_neg.clicked.connect(self.negative)
            inc_bright = QPushButton("Повысить яркость")
            inc_bright.clicked.connect(self.increase_brigthness)
            draw_circ = QPushButton("Нарисовать круг")
            draw_circ.clicked.connect(self.draw_circle)
            back = QPushButton("Назад")
            back.clicked.connect(self.go_back)

            self.v_layout.addWidget(show_img)
            self.v_layout.addWidget(show_rgb)
            self.v_layout.addWidget(show_neg)
            self.v_layout.addWidget(inc_bright)
            self.v_layout.addWidget(draw_circ)
            self.v_layout.addWidget(back)
            

      def first_buttons(self):
            
            upload_img = QPushButton("Файл")
            upload_img.clicked.connect(self.read_file)
            web_photo = QPushButton("Вебка")
            web_photo.clicked.connect(self.get_image_from_web)
            end = QPushButton("Выход")
            end.clicked.connect(self.window.close)
            self.v_layout.addWidget(upload_img)
            self.v_layout.addWidget(web_photo)
            self.v_layout.addWidget(end)

if __name__ == "__main__":
      temp = main()
