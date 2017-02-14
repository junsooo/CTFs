#Ximage – 풀다 만 거

https://scoreboard.ctf.bsidessf.com/challenges/forensics

##시도해 본 것들

HxD로 neoncow.bmp파일을 열어보았다. 
Bmp 파일 뒤에 this is not the flag you're looking for, but keep looking!! 이라는 문자열들이 많이 써져있다. 맨 뒤에는 AAAAAAAAAAAAAAAAAAAAAA 가 써져있다.(‘A’*24)

24글자를 대문자 A로 바꿔놓은 것처럼 보인다.

이번에는 사진을 사진 뷰어로 열어보았다. 사진에 뜬금없이 알록달록한 픽셀들이 박혀있다. 마치 쿠키에 초코 칩이 박혀있는 것 같다.
이 픽셀들에 hidden data가 있을 줄 알고 일단 그림판으로 저 픽셀들 빼고 다 검은 색으로 채워 넣었다. (neoncow_change.bmp)

이후 python PIL을 가지고 비트 추출을 시도해 보았는데 안 된다. (ximage.py) 24비트 다 해봄

Bmp 파일은 사진 파일의 1바이트가 각 픽셀의 R, G, B 값을 가지기 때문에 당근 심플한 LSB stego 이런 비슷한 것인 줄 알았는데 직접 해보니 안돼서 슬펐다.

