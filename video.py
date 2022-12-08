import cv2
import pytesseract
from PIL import Image
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
NA = ['NA']

def video_cap():
    # Use the attached camera to capture images
    # 0 stands for the first one
    return_list = []
    cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Neuropathic View', img1)
        text = pytesseract.image_to_string(Image.fromarray(img1))
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return None
        split_txt = text.split("\n")
        matchespi = [match for match in split_txt if "PI" in match]
        matchesvf = [match for match in split_txt if "Vol Flow" in match]
        matchestamv = [match for match in split_txt if "TAMV" in match]
        array_lengthpi = len(matchespi)
        array_lengthvf = len(matchesvf)
        array_lengthtamv = len(matchestamv)

        if array_lengthpi != 0:

            for i in range(array_lengthpi):
                matchespi[i] = ",".join( matchespi[i].split() )
                print(matchespi)
                print("sent pi to alg: ", matchespi)
                return(matchespi)

        elif array_lengthvf != 0:

            for i in range(array_lengthvf):
                matchesvf[i] = ",".join( matchesvf[i].split() )
                print(matchesvf)
                print("sent vf to alg: ", matchesvf)
                return(matchesvf)
        elif array_lengthtamv != 0:

            for i in range(array_lengthtamv):
                matchestamv[i] = ",".join( matchestamv[i].split() )
                print(matchesvf)
                print("sent vf to alg: ", matchestamv)
                return(matchestamv)
        else:
            print("no data found")

    cap.release()

if __name__ == "__main__":
    video_cap()