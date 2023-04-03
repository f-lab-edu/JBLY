import time
from multiprocessing import Process
from morecherry_img_download import morecherry_img_downloader
from common.ProductTypes import product_types

if __name__ == '__main__':
    start_time = time.time()

    p_outwear = Process(target=morecherry_img_downloader, args=("https://more-cherry.com/category/outwear/24/?page=", product_types.OUTWEAR.name))
    # p_top = Process(target=morecherry_img_downloader, args=("https://more-cherry.com/category/top/25/?page=", product_types.TOP.name))
    # p_bottom = Process(target=morecherry_img_downloader, args=("https://more-cherry.com/category/pants/26/?page==", product_types.BOTTOM.name))
    # p_acc = Process(target=morecherry_img_downloader, args=("https://more-cherry.com/category/accessory/28/?page=", product_types.ACCESSORY.name))
    # p_shoes = Process(target=morecherry_img_downloader, args=("https://more-cherry.com/category/shoes/42/?page=", product_types.SHOES.name))

    p_outwear.start()
    # p_top.start()
    # p_bottom.start()
    # p_acc.start()
    # p_shoes.start()

    p_outwear.join()
    # p_top.join()
    # p_bottom.join()
    # p_acc.join()
    # p_shoes.join()

    print(time.time() - start_time)
