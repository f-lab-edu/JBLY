from multiprocessing import Pool
from img import TheVerlinImgDownload
import multiprocessing


# 이런식으로 한번에 할 수 있음
# aa = [TheVerlinImgDownload, MoreCherry, ...]
#
# for i in aa:
#     i.get_images_for_url()

if __name__ == '__main__':

    path_folder_outwear = 'D:\\Jblyoutwear\\'
    path_folder_top = 'D:\\Jblytop\\'
    path_folder_bottom = "D:\\Jblybottom\\"
    path_folder_acc = 'D:\\Jblyacc\\'
    path_folder_shoes = 'D:\\Jblyshoes\\'

    urls = [
        ("https://theverlin.com/product/list.html?cate_no=42&page=", path_folder_outwear),
        ("https://theverlin.com/product/list.html?cate_no=43&page=", path_folder_top),
        ("https://theverlin.com/product/list.html?cate_no=44&page=", path_folder_bottom),
        ("https://theverlin.com/product/list.html?cate_no=48&page=", path_folder_acc),
        ("https://theverlin.com/product/list.html?cate_no=193&page=", path_folder_shoes)
    ]
    with multiprocessing.get_context('spawn').Pool(processes=len(urls)) as pool:
        pool.map(TheVerlinImgDownload.get_images_for_url, urls)

