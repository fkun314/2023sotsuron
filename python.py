import cv2
import random
import numpy as np


# 画像の類似度を出力する

# def image_similarity(img1, img2):
#     # 画像のグレースケール化
#     img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   
#     # 画像のヒストグラムを計算
#     hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
#     hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
   
#     # 画像の類似度を計算
#     similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
   
#     return similarity

def get_random_color():
    # RGBの値域を限定したランダムな色を取得
    min = 50
    max = 205
    return (
        random.randint(min, max),
        random.randint(min, max),
        random.randint(min, max)
    )

# 画像の検出リストを画像にプロットする（２つの画像のサイズが異なるときのやつ）
def draw_objects_on_image(image, objects):
    for obj in objects:
        name = obj[0]
        x, y, w, h = obj[2:6]
        x, y, w, h = int(x), int(y), int(w), int(h)
        random_color = get_random_color()
        cv2.rectangle(image, (x, y), (w, h), random_color, 2)
        cv2.circle(image, (x, y), 3, random_color, -1)
        cv2.putText(image, f'({x}, {y})', (x-20, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, random_color, 2)
        cv2.circle(image, (w, y), 3, random_color, -1)
        cv2.putText(image, f'({w}, {y})', (w - 40, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, random_color, 2)
        cv2.circle(image, (x,  h), 3, random_color, -1)
        cv2.putText(image, f'({x}, { h})', (x-20,  h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.3, random_color, 2)
        cv2.circle(image, (w,  h), 3, random_color, -1)
        cv2.putText(image, f'({w}, { h})', (w - 40,  h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.3, random_color, 2)
        cv2.rectangle(image, (x, y), (x + len(name)*11, y+15), (40,40,40), -1)
        cv2.putText(image, name, (x+5, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, random_color, 2)

    return image

# 動画から４枚を抽出するやつ
def extract_img(video_path):
    # 動画の読み込み
    video = cv2.VideoCapture(video_path)

    # 動画情報の取得
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # 動画から4つのフレームを取得
    frames1 = []
    frames2 = []
    for i in range(4):
        # i番目のフレーム番号を計算
        frame_number = int(i * frame_count / 4)
        video.set(1, frame_number)
        _, frame = video.read()
        # フレーム番号を追加
        cv2.putText(frame, "Frame No."+str(frame_number), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 150, 255), 15)
        if i < 2:
            frames1.append(frame)
        else:
            frames2.append(frame)

    frame = cv2.hconcat(frames1)
    frame = cv2.vconcat([frame, cv2.hconcat(frames2)])

    # 画像として保存
    cv2.imwrite(video_path.replace('.mp4', '.png'), frame)

    # 動画のクローズ
    video.release()



if __name__ == '__main__':
    # 画像を読み込む
    # img1 = cv2.imread('33ae80cd-098e-4d09-8db1-fd5e91567dd6.png')
    # img2 = cv2.imread('38c05b83-3f9a-4b09-825d-9fe3968c0623.png')
   
    # 画像の類似度を計算
    # print(image_similarity(img1, img2))

    # # サイズの異なる画像の検出座標を出力
    # img1 = cv2.imread('./crop2big.png')
    # img2 = cv2.imread('./crop3small.png')

    # detected_list = [['person', 0.9992720484733582, 804.4257, 121.03796, 964.77716, 540.2267], ['person', 0.998677670955658, 190.58006, 31.238832, 326.66342, 537.68823], ['skateboard', 0.9700283408164978, 783.2626, 489.77808, 960.4012, 539.8653]]
    # detected_list2 = [['person', 0.9986074566841125, 447.15125, 71.88957, 533.78705, 302.49005], ['person', 0.99834144115448, 108.21198, 23.095757, 186.76569, 302.90826], ['skateboard', 0.8907840847969055, 435.82407, 274.11307, 529.33984, 302.0106]]

    # # cv2.imwrite("result.jpg", draw_objects_on_image(img1, detected_list))
    # cv2.imwrite("result.jpg", draw_objects_on_image(img2, detected_list2))

    # 動画から４枚を抽出するやつ
    extract_img('9.mp4')
