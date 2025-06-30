import cv2 as cv

def get_image_from_web():
      cam = cv.VideoCapture(0)

      cv.namedWindow("test")
      img_name = "opencv_frame.png"

      while True:
            ret, frame = cam.read()
            if not ret:
                  print("failed to grab frame")
                  break
            cv.imshow("test", frame)

            k = cv.waitKey(1)
            if k%256 == 32:
                  # SPACE pressed
                  cv.imwrite(img_name, frame)
                  print("{} written!".format(img_name))
                  break

      cam.release()

      cv.destroyAllWindows()
      return frame

def viewImage(image, name_of_window="Image"):
      cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
      cv.resizeWindow(name_of_window, 800, 500)
      cv.imshow(name_of_window, image)
      cv.waitKey(0)
      cv.destroyAllWindows()

def rgb(image):
      print("1) red\n" \
      "2) green \n" \
      "3) blue ")

      choice = input("Какой канал показать: ")
      
      RED = "1"
      GREEN = "2"
      BLUE = "3"

      if choice == BLUE:
            blue = image.copy()
            # set green and red channels to 0
            blue[:, :, 1] = 0
            blue[:, :, 2] = 0
            viewImage(blue)
      elif choice == GREEN:
            green = image.copy()
            # set blue and red channels to 0
            green[:, :, 0] = 0
            green[:, :, 2] = 0
            viewImage(green)
      elif choice == RED:
            red = image.copy()
            # set blue and green channels to 0
            red[:, :, 0] = 0
            red[:, :, 1] = 0
            viewImage(red)
      else: print("smth goes wrong")

def increase_brigthness(image):
      try:
            beta = float(input("Введите значение на сколько хотите повысить яркость: "))
            if beta < 0: raise ValueError
      except ValueError:
            print("Число должно быть положительным")
      image = cv.convertScaleAbs(img, alpha=2, beta=beta)
      viewImage(image)

def draw_circle(image, name_of_window="Image"):
      try:
            print("Введите координаты центра круга")
            x = int(input("x: "))
            y = int(input("y: "))
            rad = int(input("Введите радиус круга: "))
            if x < 0 or x > 800 or \
            y < 0 or y > 500 \
            or rad < 0:
                  raise ValueError
      except ValueError:
            print("smth goes wrong")
      cv.circle(image, (x, y), rad, (0, 0, 255), 5)
      viewImage(image)

while True:
      print("1) Загрузить изображение\n" \
            "2) Сделать снимок с веб-камеры\n" \
            "0) Выход")

      action = input("Выберите действие: ")
      UPLOAD_IMG = "1"
      WEB_PHOTO = "2"
      EXIT = "0"

      if action == UPLOAD_IMG: img = cv.imread("C:/Users/daiko/Desktop/98802d213532114e6aac07121355e7d3.jpg")
      elif action == WEB_PHOTO: img = get_image_from_web()
      elif action == EXIT: break
      else: continue

      print("1) Показать изображение\n" \
      "2) Показать красный синий или зеленый канал изображения\n" \
      "3) Показать негативное изображение\n" \
      "4) Повысить яркость\n" \
      "5) Нарисовать круг\n" \
      "0) Выход")

      action = input("Выберите действие: ")
      SHOW_IMG = "1"
      SHOW_RGB = "2"
      SHOW_NEG = "3"
      INC_BRIGHT = "4"
      DRAW_CIRC = "5"

      if action == SHOW_IMG:
            viewImage(img)
      elif action == SHOW_RGB: 
            rgb(img)
      elif action == SHOW_NEG: 
            img = cv.bitwise_not(img)
            viewImage(img)
      elif action == INC_BRIGHT: 
            increase_brigthness(img)
      elif action == DRAW_CIRC: 
            draw_circle(img)
      else: continue
