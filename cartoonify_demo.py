import cv2
import matplotlib
import matplotlib.pyplot as plt
import os

def cartoonify(imagefile,folder):
    path = os.path.join(folder,imagefile)
    img=cv2.imread(path)
    #Apply Bilateral Filter
    col_img = cv2.bilateralFilter(img,5,255,255)
    #Convert Image from bgr to gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Apply Median Blur
    gray = cv2.medianBlur(gray,3)

    #get the edges
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)

    #Bitwise And of bilateral filter and mask is edges
    cartoon = cv2.bitwise_and(col_img,col_img,mask=edges)
    return cartoon

def load_images_from_folder(folder):
    images = []
    filenames=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        filenames.append(filename)
        if img is not None:
            images.append(img)
    return images,filenames

def run(input_folder,output_folder,vis=False):
    images,filenames = load_images_from_folder(input_folder)
    for imagefile in filenames:
        # 处理图像
        output_image = cartoonify(imagefile,input_folder)

        #保存图像
        name = list(imagefile.split('.'))[0]
        cv2.imwrite(os.path.join(output_folder,name+'_cartoonify.jpg'),output_image)

        if vis:
            # 显示图像
            cv2.imshow('Result visualization', output_image)
            # 等待用户按键（这里的 0 表示无限等待）
            cv2.waitKey(0)
            # 销毁所有窗口
            cv2.destroyAllWindows()

input_folder="inputs"
output_folder = "outputs" 
run(input_folder,output_folder,vis=False) # 若每张图片处理时想直接看结果，则将vis设置为True

