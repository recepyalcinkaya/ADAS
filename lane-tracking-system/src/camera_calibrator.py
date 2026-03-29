import numpy as np
import cv2
import glob
import os

class CameraCalibrator:
    def __init__(self, nx=9, ny=6):
        self.nx = nx # Satranç tahtasındaki yatay iç köşe sayısı
        self.ny = ny # Satranç tahtasındaki dikey iç köşe sayısı
        self.mtx = None
        self.dist = None

    def calibrate(self, image_dir, save_path="camera_calib.npz"):
        objpoints = [] # 3D noktalar (gerçek dünya)
        imgpoints = [] # 2D noktalar (resim düzlemi)

        # Gerçek dünya koordinatlarını hazırla: (0,0,0), (1,0,0), ..., (8,5,0)
        objp = np.zeros((self.nx * self.ny, 3), np.float32)
        objp[:, :2] = np.mgrid[0:self.nx, 0:self.ny].T.reshape(-1, 2)

        images = glob.glob(os.path.join(image_dir, '*.jpg'))
        
        if not images:
            print("Uyarı: Kalibrasyon için resim bulunamadı!")
            return

        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (self.nx, self.ny), None)

            if ret:
                imgpoints.append(corners)
                objpoints.append(objp)

        # Matrisi hesapla
        ret, self.mtx, self.dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        
        # Gelecekte tekrar hesaplamamak için kaydet
        np.savez(save_path, mtx=self.mtx, dist=self.dist)
        print(f"Kalibrasyon tamamlandı ve {save_path} olarak kaydedildi.")

    def load_calibration(self, load_path="camera_calib.npz"):
        if os.path.exists(load_path):
            data = np.load(load_path)
            self.mtx = data['mtx']
            self.dist = data['dist']
            return True
        return False

    def undistort(self, img):
        if self.mtx is not None and self.dist is not None:
            return cv2.undistort(img, self.mtx, self.dist, None, self.mtx)
        return img
