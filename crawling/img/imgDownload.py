import threading
import time
from multiprocessing import Pool
from img import TheVerlinImgDownload
import multiprocessing as mp
from multiprocessing import Process
from TheVerlinImgDownload import theverlin_img_downloader
from parsing.ProductTypes import product_types
from downloader import outwear_downloader

if __name__ == '__main__':
    start_time = time.time()

    p_outwear = Process(target=theverlin_img_downloader, args=("https://theverlin.com/product/list.html?cate_no=42&page=", product_types.OUTWEAR.name))
    p_top = Process(target=theverlin_img_downloader, args=("https://theverlin.com/product/list.html?cate_no=43&page=", product_types.TOP.name))
    p_bottom = Process(target=theverlin_img_downloader, args=("https://theverlin.com/product/list.html?cate_no=44&page=", product_types.BOTTOM.name))
    p_acc = Process(target=theverlin_img_downloader, args=("https://theverlin.com/product/list.html?cate_no=48&page=", product_types.ACCESSORY.name))
    p_shoes = Process(target=theverlin_img_downloader, args=("https://theverlin.com/product/list.html?cate_no=193&page=", product_types.SHOES.name))

    p_outwear.start()
    p_top.start()
    p_bottom.start()
    p_acc.start()
    p_shoes.start()

    p_outwear.join()
    p_top.join()
    p_bottom.join()
    p_acc.join()
    p_shoes.join()

    print(time.time() - start_time)
