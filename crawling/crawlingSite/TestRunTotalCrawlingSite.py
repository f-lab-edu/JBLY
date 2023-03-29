from CrawlingSiteInterface import *
from parsing.ProductTypes import productTypes

'''
self.store_name = store_name
self.base_url = base_url
self.user_agent = user_agent
self.enter_url_with_item_type_list = enter_url_with_item_type_list

base_url = 
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36"

'''


def run():
    more_cherry = CrawlingSiteInterface('morecherry', 'https://more-cherry.com',
                                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/109.0.0.0 Safari/537.36',
                                        [
                                            ("https://more-cherry.com/category/outwear/24/?page=",
                                             productTypes.OUTWEAR.name),
                                            ("https://more-cherry.com/category/top/25/?page=", productTypes.TOP.name),
                                            ("https://more-cherry.com/category/pants/26/?page=",
                                             productTypes.BOTTOM.name),
                                            ("https://more-cherry.com/category/accessory/28/?page=",
                                             productTypes.ACCESSORY.name),
                                            ("https://more-cherry.com/category/shoes/42/?page=",
                                             productTypes.SHOES.name),
                                        ])

    porterna = CrawlingSiteInterface('porterna', 'https://porterna.com',
                                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                      [("https://porterna.com/product/list.html?cate_no=541&page=",
                                        productTypes.OUTWEAR.name), (
                                       "https://porterna.com/product/list.html?cate_no=789&page=",
                                       productTypes.TOP.name), (
                                       "https://porterna.com/product/list.html?cate_no=28&page=",
                                       productTypes.BOTTOM.name), (
                                       "https://porterna.com/product/list.html?cate_no=44&page=",
                                       productTypes.ACCESSORY.name), (
                                       "https://porterna.com/product/list.html?cate_no=79&page=",
                                       productTypes.SHOES.name)])

    theverlin = CrawlingSiteInterface('theverlin', 'https://theverlin.com/',
                                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                      [("https://theverlin.com/product/list.html?cate_no=42&page=",
                                        productTypes.OUTWEAR.name), (
                                       "https://theverlin.com/product/list.html?cate_no=43&page=",
                                       productTypes.TOP.name), (
                                       "https://theverlin.com/product/list.html?cate_no=44&page=",
                                       productTypes.BOTTOM.name), (
                                       "https://theverlin.com/product/list.html?cate_no=48&page=",
                                       productTypes.ACCESSORY.name),
                                       ("https://theverlin.com/category/shoes/193/?page=", productTypes.SHOES.name), ])

    more_cherry.print_site_default_info()
    porterna.print_site_default_info()
    theverlin.print_site_default_info()

run()