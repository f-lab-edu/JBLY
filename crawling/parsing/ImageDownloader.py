import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

def getImage(url):
    protocal = "https://"
    imageUrl = "m.more-cherry.com/web/product/medium/202302/a575fb018b36eb7cb4db1a68b05417c7.gif"

    # image file 앞에 http protocal이 존재하지 않을 경우
    if not imageUrl.startswith(protocal):
        imageUrl = protocal + imageUrl

    binaryTypeImage = urllib.request.urlopen(imageUrl).read()
    with open("imageBinary01.gif", mode="wb") as f:
        f.write(binaryTypeImage)
    urlImage = urllib.request.urlretrieve(imageUrl)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData