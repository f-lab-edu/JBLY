import datetime
import Application
import sys

sys.setrecursionlimit(10 ** 7) # RecursionError 방지

if __name__ == '__main__':

    beforeCrawling = datetime.datetime.now()
    beforeCrawlingTime = beforeCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print("크롤링 애플리케이션 시작 시간 : ", beforeCrawlingTime)

    Application.run()

    afterCrawling = datetime.datetime.now()
    afterCrawlingTime = afterCrawling.strftime("%Y-%m-%d %H:%M:%S")
    print("크롤링 애플리케이션 종료 시간 : ", afterCrawlingTime)

