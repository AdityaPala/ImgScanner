import cv2
import numpy as np

#{{ SkewCorrection.cover.url }}
path = "media/media/aetna_rotated.png"
img = cv2.imread(path)

class Correction:

    def __init__(self, img):
        self.img = img

    def preProcess(self, img):
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
        imgCanny = cv2.Canny(imgBlur, 1.3, 10)
        imgThresh = cv2.threshold(imgCanny, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return imgThresh

    def skewFix(self, img):
        processedImg = self.preProcess(img)
        coords = np.column_stack(np.where(processedImg > 0))
        angle = cv2.minAreaRect(coords)[-1]

        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        (h, w) = processedImg.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1)
        rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        cv2.imwrite('media/output/imgSkewed.png', rotated)
        print("Angle: {:.2f} degrees".format(angle))

        # draw the correction angle on the image so we can validate it
        cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 0, 255), 2)
        return rotated


# processedImg = preProcess(img)
#
# coords = np.column_stack(np.where(processedImg > 0))
# angle = cv2.minAreaRect(coords)[-1]
#
# if angle < -45:
#     angle = -(90 + angle)
# else:
#     angle = -angle
#
# (h, w) = processedImg.shape[:2]
# center = (w//2, h//2)
# M = cv2.getRotationMatrix2D(center, angle, 1)
# rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#
# # draw the correction angle on the image so we can validate it
# cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# cv2.imshow("og", img)
# cv2.imshow("img", rotated)
#
# cv2.waitKey(0)

# A = Correction
# A.skewFix(A, img)