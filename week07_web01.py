# import urllib.request
#
# url = "https://www.daelim.ac.kr/ajaxfile/CmnFileCpnt/fileView.do?gbn=x02&SITE_GROUP_NO=2&SITE_NO=2"
# urllib.request.urlretrieve(url, filename= 'daelim.png') # 웹에서 가져 온 이미지를 보조기억장치에 저장
# print('저장완료')

import urllib.request

url = "https://www.daelim.ac.kr/ajaxfile/CmnFileCpnt/fileView.do?gbn=x02&SITE_GROUP_NO=2&SITE_NO=2"
logo = urllib.request.urlopen(url).read() # 이미지를 다운받아서 메모리에 저장

with open('daelim.png', 'wb') as file: # 원본이미지가 png 포맷이므로 쓰기 모드를 텍스트가 아닌 바이너리 형식으로 쓰기
    file.write(logo) # 실제 보조기억장치에 쓰기
    print('저장완료')