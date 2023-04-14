import cv2
from common.ProductTypes import product_types
import hashlib
import numpy as np

path_folder_outwear = 'D:\\morecherry_outwear\\'
path_folder_top = 'D:\\morecherry_top\\'
path_folder_bottom = 'D:\\morecherry_bottom\\'

def img_cropper(img, item_type):

    # 이미지 파일을 불러옵니다.
    image = cv2.imdecode(img, cv2.IMREAD_COLOR)

    # 첫 번째 이미지를 800x1000으로 자릅니다.
    first_crop = image[:1000, :800].copy()
    md5hash = hashlib.md5(first_crop).hexdigest() + ".jpg"
    if item_type == product_types.OUTWEAR.name:
        cv2.imwrite(path_folder_outwear + md5hash, first_crop)
    elif item_type == product_types.TOP.name:
        cv2.imwrite(path_folder_top + md5hash, first_crop)
    else:
        cv2.imwrite(path_folder_bottom + md5hash, first_crop)

    # 이후 이미지들을 800x800으로 자릅니다.
    num_crops = (image.shape[0] - 1000) // 800
    crop_positions = [(i * 800 + 1000, (i + 1) * 800 + 1000) for i in range(num_crops)]
    if (image.shape[0] - 1000) % 800 != 0:
        crop_positions.append((num_crops * 800 + 1000, image.shape[0]))

    # 이미지 파일에서 자른 이미지를 저장합니다.
    for i, (start, end) in enumerate(crop_positions):
        crop = image[start:end, :]

        # 왼쪽, 오른쪽 여백을 제거합니다.
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x, y, w, h = cv2.boundingRect(contours[0])
        crop = crop[y:y + h, x:x + w]

        # 중앙에 정렬된 이미지만 자릅니다.
        height, width = crop.shape[:2]
        if height > width:
            diff = height - width
            crop = crop[:, diff // 2:width + diff // 2]
        elif width > height:
            diff = width - height
            crop = crop[diff // 2:height + diff // 2, :]

        crop = np.ascontiguousarray(crop)
        md5hash_2 = hashlib.md5(crop).hexdigest() + ".jpg"
        if not crop.any():
            continue
        if item_type == product_types.OUTWEAR.name:
            cv2.imwrite(path_folder_outwear + md5hash_2, crop)
        elif item_type == product_types.TOP.name:
            cv2.imwrite(path_folder_top + md5hash_2, crop)
        else:
            cv2.imwrite(path_folder_bottom + md5hash_2, crop)
    return None



