# 중복된 데이터를 제거하는 역할을 담당합니다.
def check(crawling_datas, db_datas):
    key = 'image'
    result = [crawling_data for crawling_data in crawling_datas if not any(crawling_data[key] == db_data[key] for db_data in db_datas)]

    # 중복을 제거한 데이터를 [[item01], [item02]] 형식으로 내보내줍니다.
    return [list(element.values()) for element in result]
