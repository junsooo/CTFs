Old Magic

KAIST GoN의 이준수가 대회가 끝나고 나서 푼 문제이다.

gameboy 에뮬레이터로 실행할 수 있는 secret.gb 파일이 주어졌다.
리버싱 문제이기 때문에 디버깅을 할 수 있는 bgb emulator를 사용하였다.

일단 Password: 가 뜨고 엔터키를 누르면 INCORRECT 문자열이 나온다.

문제를 풀기 위해서 CORRECT 문자열을 찾기로 하였다.
이 문자열은 0x0744 위치에 있다. 이 위치로 가는 인스트럭션은 다음과 같이 0x0721에 있다.
```
ROM:0721  jr  nz, unk_743
```
여기에 연결된 함수를 끝까지 따라가면 0x0685 위치에서 함수가 시작되는 것을 알 수 있다.
```
ROM:0685                 ld      hl, 0C0D1h
ROM:0688                 ld      a, (hl)
ROM:0689                 cp      10h
ROM:068B                 jp      nc, loc_6C7
ROM:068E                 ld      a, 0A0h ; '
ROM:0690                 add     a, (hl)
ROM:0691                 ld      c, a
ROM:0692                 ld      a, 0C0h ; '
ROM:0694                 adc     a, 0
ROM:0696                 ld      b, a
ROM:0697                 ld      a, (bc)    //[C0A0:C0AF] 의 memory 참조
ROM:0698                 ld      c, a
ROM:0699                 cp      10h      //C0A0 + k 가 0x10인가?
ROM:069B                 jp      z, loc_6C0
ROM:069E                 call    sub_762  // print “INCORRECT”
ROM:06A1                 ld      hl, 71Eh
ROM:06A4                 push    hl
ROM:06A5                 call    sub_121E
ROM:06A8                 ret     pe
ROM:06A9                 ld      (bc), a
ROM:06AA                 ld      hl, 7D0h
ROM:06AD                 push    hl
ROM:06AE                 call    sub_1585
ROM:06B1                 ret     pe
ROM:06B2                 ld      (bc), a
ROM:06B3                 call    sub_20C
ROM:06B6                 ld      hl, 0C0D0h
ROM:06B9                 ld      (hl), 0
ROM:06BB                 ld      e, 0
ROM:06BD                 jp      loc_71B

ROM:06C0                 ld      hl, 0C0D1h
ROM:06C3                 inc     (hl)
ROM:06C4                 jp      loc_685 // k <= 0x10
```

python pseudo code로 간단히 나타내면 다음과 같다.

```
for I in range(0x10):
	if [0xc0a0 + I] == 0x10:
		counter+=1
	if counter == 0x10:
		get_flag()
```
따라서 0xc0a0 부분의 메모리를 참조한다. 지금 보니 내가 입력하는 글자 하나마다 0x1, 0x2, 0x4, 0x8, 0x10 이런식으로 저장이 된다. 예를 들어 “AAAAAAAAAAAAAAAA”를 입력하면 메모리가 101010101010...10이 된다. 이 때 총 16글자를 입력할 수 있고, 이 글자 모두가 어떤 조건에 맞아야 flag를 획득할 수 있다.
이 상황에서 0x0685에 breakpoint를 걸면 c0a0:c0af 가 다른 숫자들로 바뀌는 것을 알 수 있다. 입력했던 숫자들은 c0b0:c0bf로 옮겨진다. 이 때 black box라고 생각하고 게임보이로 넣을 수 있는 모든 입력들을 넣어보았다. 상하좌우 키, a,b, select 키를 넣을 수 있었다. 운이 좋게도 k번째 넣어준 입력과 c0a0 + k 의 값이 일대일 대응이 되었다.
최종적으로 c0a0 – c0af 위치의 메모리에 “04 04 10 40 08 02 02 20 01 08 01 20 01 20 10 20” 값을 넣어주면 flag를 구할 수 있다.
