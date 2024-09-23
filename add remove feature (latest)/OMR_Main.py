import cv2
import numpy as np
import utlis

########################################################################
webCamFeed = True
cap = cv2.VideoCapture(0)  # Change to 0 to use the default camera
cap.set(10, 160)
heightImg = 700
widthImg = 700
questions = 5
choices = 5
ans = [1, 2, 0, 2, 4]
########################################################################

count = 0

# Check if the camera is opened successfully
if webCamFeed and not cap.isOpened():
    print("Could not open video device")
    exit()

retry_limit = 5  # Retry limit if the camera fails
retry_count = 0

def process_image(img, ans):
    img = cv2.resize(img, (widthImg, heightImg))  # Resize image
    imgFinal = img.copy()
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # Create a blank image for debugging
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert image to gray scale
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # Add Gaussian blur
    imgCanny = cv2.Canny(imgBlur, 10, 70)  # Apply Canny edge detector

    try:
        # Image processing and contour detection
        imgContours = img.copy()
        imgBigContour = img.copy()
        contours, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
        rectCon = utlis.rectContour(contours)
        biggestPoints = utlis.getCornerPoints(rectCon[0])
        gradePoints = utlis.getCornerPoints(rectCon[1])

        if biggestPoints.size != 0 and gradePoints.size != 0:
            biggestPoints = utlis.reorder(biggestPoints)
            cv2.drawContours(imgBigContour, biggestPoints, -1, (0, 255, 0), 20)
            pts1 = np.float32(biggestPoints)
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

            gradePoints = utlis.reorder(gradePoints)
            cv2.drawContours(imgBigContour, gradePoints, -1, (255, 0, 0), 20)
            ptsG1 = np.float32(gradePoints)
            ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
            matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)
            imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))

            imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
            imgThresh = cv2.threshold(imgWarpGray, 170, 255, cv2.THRESH_BINARY_INV)[1]

            boxes = utlis.splitBoxes(imgThresh)
            countR = 0
            countC = 0
            myPixelVal = np.zeros((questions, choices))
            for image in boxes:
                totalPixels = cv2.countNonZero(image)
                myPixelVal[countR][countC] = totalPixels
                countC += 1
                if countC == choices:
                    countC = 0
                    countR += 1

            myIndex = []
            for x in range(questions):
                arr = myPixelVal[x]
                myIndexVal = np.where(arr == np.amax(arr))
                myIndex.append(myIndexVal[0][0])

            grading = []
            for x in range(questions):
                grading.append(1 if ans[x] == myIndex[x] else 0)

            score = sum(grading)

            utlis.showAnswers(imgWarpColored, myIndex, grading, ans)
            utlis.drawGrid(imgWarpColored)
            imgRawDrawings = np.zeros_like(imgWarpColored)
            utlis.showAnswers(imgRawDrawings, myIndex, grading, ans)
            invMatrix = cv2.getPerspectiveTransform(pts2, pts1)
            imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))

            imgRawGrade = np.zeros_like(imgGradeDisplay, np.uint8)
            cv2.putText(imgRawGrade, str(int(score)), (70, 100),
                        cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 3)
            invMatrixG = cv2.getPerspectiveTransform(ptsG2, ptsG1)
            imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg))

            imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1, 0)
            imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1, 0)

            return imgFinal
        else:
            return imgBlank

    except Exception as e:
        print(f"An error occurred: {e}")
        return imgBlank

def start_camera():
    cap = cv2.VideoCapture(0)  # Adjust the index if you have multiple cameras

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image from camera.")
            break

        final_result = process_image(frame, ans)
        cv2.imshow("Final Result", final_result)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    start_camera()
