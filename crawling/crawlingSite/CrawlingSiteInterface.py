'''
상속 받는 python module은 아래와 같은 값들을 가져야 합니다.
store_name = "" # 쇼핑몰 이름
base_url = "" # 쇼핑몰 dns
user_agent = "" # web agent
total_url = [] # I/O 처리 후 데이터를 저장하는 Url
enter_url_with_item_type_list = [] # (item type first page url, item type) 을 갖는 리스트
'''


class CrawlingSiteInterface:

    def __init__(self, store_name: str, base_url: str, user_agent: str, enter_url_with_item_type_list: list):
        '''Python에선 기본적으로 여러개의 생성자를 만들 수 없습니다. 데코레이터를 통해 만들 수 있지만 필요하게 된다면 적용'''
        self.store_name = store_name
        self.base_url = base_url
        self.user_agent = user_agent
        self.enter_url_with_item_type_list = enter_url_with_item_type_list
        self.total_url = None

    def print_site_default_info(self):
        result = self.store_name + " " + self.base_url + " " + self.user_agent
        print(result)
        for enter_url_with_item_type in self.enter_url_with_item_type_list:
            print(enter_url_with_item_type)
        return None
