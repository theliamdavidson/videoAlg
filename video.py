import cv2
import pytesseract
from PIL import Image
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
NA = ['NA']

def video_cap():
    # Use the attached camera to capture images
    # 0 stands for the first one
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(Image.fromarray(img1))
        cv2.imshow('Neuropathic View', img1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return None
        split_txt = text.split("\n")
        matches = [match for match in split_txt if "PI" in match]
        matches += [match for match in split_txt if "VF" in match]
        array_length = len(matches)
        for i in range(array_length):
            matches[i] = ",".join( matches[i].split() )

        #print("Extracted Text: ", text)
        #print("split text: ", split_txt)
        print(matches)
        #print(df)
        print("sent to nums.csv: ", matches)
    cap.release()

if __name__ == "__main__":
    video_cap()