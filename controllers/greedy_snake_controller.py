from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QPixmap, QImage
import cv2
import numpy as np
from core.greedy_snake import GreedyAlgorithmAuto, ImgEnrgPyramid, getAvgDist

class GreedySnakeController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.initial_points = []
        self.points = []
        self.drawing = False
        self.gray_image = None
        self.color_image = None
        self.processed_image = None
        self.snake_thread = None

        # Mouse tracking
        self.main_window.lblOriginal.setMouseTracking(True)

        # Connect UI
        self.main_window.sliderAlpha.valueChanged.connect(self.update_parameters)
        self.main_window.sliderBeta.valueChanged.connect(self.update_parameters)
        self.main_window.sliderGamma.valueChanged.connect(self.update_parameters)
        self.main_window.btnApplySnake.clicked.connect(self.apply_snake)
        self.main_window.btnClearContour.clicked.connect(self.clear_contour)

        # Mouse events
        self.main_window.lblOriginal.mousePressEvent = self.mouse_press
        self.main_window.lblOriginal.mouseMoveEvent = self.mouse_move
        self.main_window.lblOriginal.mouseReleaseEvent = self.mouse_release

        self.alpha = 0.1
        self.beta = 0.1
        self.gamma = 1.0

    def get_image_coords(self, event_pos):
        if self.color_image is None:
            return None, None
        label = self.main_window.lblOriginal
        label_size = label.size()
        img_height, img_width = self.color_image.shape[:2]
        scale = min(label_size.width()/img_width, label_size.height()/img_height)
        displayed_width = img_width*scale
        displayed_height = img_height*scale
        offset_x = (label_size.width()-displayed_width)/2
        offset_y = (label_size.height()-displayed_height)/2
        rel_x = event_pos.x() - offset_x
        rel_y = event_pos.y() - offset_y
        if rel_x <0 or rel_y<0 or rel_x>=displayed_width or rel_y>=displayed_height:
            return None,None
        return int(rel_x/scale), int(rel_y/scale)

    def set_image(self, gray_img, color_img):
        self.gray_image = gray_img
        self.color_image = color_img
        self.processed_image = color_img.copy()
        self.initial_points = []
        self.points = []
        self.display_images()

    def mouse_press(self, event):
        if event.button() == Qt.LeftButton and self.color_image is not None:
            self.drawing = True
            x, y = self.get_image_coords(event.position())
            if x is not None:
                self.initial_points.append([x, y])
                self.points.append([x, y])

    def mouse_move(self, event):
        if self.drawing and self.color_image is not None:
            x, y = self.get_image_coords(event.position())
            if x is not None:
                self.initial_points.append([x, y])
                self.points.append([x, y])
                self.display_images()

    def mouse_release(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def display_images(self):
        if self.color_image is not None:
            # Input ثابت مع initial_points
            display_input = self.color_image.copy()
            if len(self.initial_points)>0:
                pts = np.array(self.initial_points, dtype=np.int32)
                for p in self.initial_points:
                    cv2.circle(display_input, (int(round(p[0])), int(round(p[1]))), 1, (0,255,0), -1)
                if len(self.initial_points)>1:
                    cv2.polylines(display_input, [pts], isClosed=False, color=(0,255,0), thickness=2)
            self.set_label_image(self.main_window.lblOriginal, display_input)

            # Processed image (Snake)
            if self.processed_image is not None:
                display_output = self.processed_image.copy()
                self.set_label_image(self.main_window.lblProcessed, display_output)

    def set_label_image(self,label,image):
        h,w,c = image.shape
        bytes_per_line = 3*w
        q_img = QImage(image.data, w,h,bytes_per_line,QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(pixmap.scaled(label.size(),Qt.KeepAspectRatio))
        label.update()

    def update_parameters(self):
        self.alpha = self.main_window.sliderAlpha.value()/100.0
        self.beta = self.main_window.sliderBeta.value()/100.0
        self.gamma = self.main_window.sliderGamma.value()/100.0

    def apply_snake(self):
        if len(self.initial_points)<3 or self.gray_image is None:
            return
        points = np.array(self.initial_points, dtype=np.float32)
        self.snake_thread = SnakeThread(points, self.gray_image, self.alpha, self.beta, self.gamma)
        self.snake_thread.update_signal.connect(self.update_snake_display)
        self.snake_thread.finished_signal.connect(self.snake_finished)
        self.snake_thread.start()

    def update_snake_display(self, points):
        self.processed_image = self.color_image.copy()
        pts = np.array(points,dtype=np.int32)
        cv2.polylines(self.processed_image,[pts],isClosed=True,color=(255,0,0),thickness=2)
        self.set_label_image(self.main_window.lblProcessed,self.processed_image)

    def snake_finished(self, final_points):
        self.points = final_points.tolist()

    def clear_contour(self):
        self.initial_points=[]
        self.points=[]
        self.processed_image=self.color_image.copy() if self.color_image is not None else None
        self.display_images()


class SnakeThread(QThread):
    update_signal = Signal(np.ndarray)
    finished_signal = Signal(np.ndarray)

    def __init__(self, points, img, alpha, beta, gamma):
        super().__init__()
        self.points = points.copy()
        self.img = img
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def run(self):
        points = self.points.astype(np.float32)
        n = len(points)
        energy_img = ImgEnrgPyramid(self.img, levels=3)
        avgDist = getAvgDist(points)

        iteration = 0
        while True:
            old_points = points.copy()
            moves = np.array([[dx, dy] for dx in [-1,0,1] for dy in [-1,0,1]])

            for i in range(n):
                prev = points[(i-1)%n]
                nextp = points[(i+1)%n]
                candidates = points[i]+moves
                candidates[:,0] = np.clip(candidates[:,0],0,self.img.shape[1]-1)
                candidates[:,1] = np.clip(candidates[:,1],0,self.img.shape[0]-1)

                Econt = np.abs(np.linalg.norm(candidates-prev,axis=1)-avgDist)
                Ecurv = np.linalg.norm(prev - 2*candidates + nextp, axis=1)**2
                Eimg = -energy_img[candidates[:,1].astype(int),candidates[:,0].astype(int)]
                E = self.alpha*Econt + self.beta*Ecurv + self.gamma*Eimg

                best_idx = np.argmin(E)
                points[i] = candidates[best_idx]

            iteration +=1
            if iteration%5==0:
                self.update_signal.emit(points.copy())

            max_movement = np.max(np.linalg.norm(points-old_points,axis=1))
            if max_movement<0.5 or iteration>5000:
                break

        self.finished_signal.emit(points)