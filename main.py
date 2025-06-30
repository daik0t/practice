import cv2 as cv

def viewImage(image, name_of_window):
    cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
    cv.resizeWindow(name_of_window, 800, 500)
    cv.imshow(name_of_window, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

while True:
      print("1) Загрузить изображение\n" \
            "2) Сделать снимок с веб-камеры\n" \
            "0) Выход")

      action = input("Выберите действие: ")
      UPLOAD_IMG = "1"
      WEB_PHOTO = "2"
      EXIT = "0"

      if action == UPLOAD_IMG: img = cv.imread("C:/Users/daiko/Desktop/XYI.png")
      elif action == WEB_PHOTO: pass
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
            viewImage(img, "Image")
      elif action == SHOW_RGB: pass
      elif action == SHOW_NEG: pass
      elif action == INC_BRIGHT: pass
      elif action == DRAW_CIRC: pass
      else: continue
