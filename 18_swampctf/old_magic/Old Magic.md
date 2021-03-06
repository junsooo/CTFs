<h1>Old Magic</h1>

[한국어](#한국어)
[English](#english)

### 한국어
KAIST GoN 짱짱

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
이제 0xc0a0 부분의 메모리를 참조해보자. 
![alt text](https://raw.githubusercontent.com/junsooo/CTFs/master/18_swampctf/secret_test.PNG)

지금 보니 내가 입력하는 글자 하나마다 0x1, 0x2, 0x4, 0x8, 0x10 이런식으로 저장이 된다. 예를 들어 “AAAAAAAAAAAAAAAA”를 입력하면 메모리가 101010101010...10이 된다. 이 때 총 16글자를 입력할 수 있고, 이 글자 모두가 어떤 조건에 맞아야 flag를 획득할 수 있다.

이 상황에서 0x0685에 breakpoint를 걸면 c0a0:c0af 가 다른 숫자들로 바뀌는 것을 알 수 있다. 입력했던 숫자들은 c0b0:c0bf로 옮겨진다. 이 때 black box라고 생각하고 게임보이로 넣을 수 있는 모든 입력들을 넣어보았다. 상하좌우 키, a,b, select 키를 넣을 수 있었다. 운이 좋게도 k번째 넣어준 입력과 c0a0 + k 의 값이 일대일 대응이 되었다.

최종적으로 c0a0 – c0af 위치의 메모리에 “04 04 10 40 08 02 02 20 01 08 01 20 01 20 10 20” 값을 넣어주면 flag를 구할 수 있다.

![alt text](https://raw.githubusercontent.com/junsooo/CTFs/master/18_swampctf/secret_correct.PNG)


### English

Given a secret.gb file that can be run as a gameboy emulator.
Because of the reversing problem, we used the bgb emulator to debug.

Once "Password:" is displayed and the Enter key is pressed, the INCORRECT string is displayed.

To solve the problem, we decided to search for the CORRECT string.
This string is located at 0x0744. The instruction to this location is at 0x0721 as follows.

```
ROM:0721  jr  nz, unk_743
```
You can see that the function starts at 0x0685 when you follow the function linked to it.
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

The python pseudo code is as follows.

```
for I in range(0x10):
	if [0xc0a0 + I] == 0x10:
		counter+=1
	if counter == 0x10:
		get_flag()
```
Now we refer to the memory in the 0xc0a0 part. 
![alt text](https://raw.githubusercontent.com/junsooo/CTFs/master/18_swampctf/secret_test.PNG)

Now I see that every character I type is stored in 0x1, 0x2, 0x4, 0x8, 0x10. For example, if you enter "AAAAAAAAAAAAAAAA", the memory will be 101010101010 ... 10. You can enter a total of 16 characters, and all of these letters can be used to obtain a flag.

In this situation, you can see that c0a0: c0af changes to another number when you breakpoint 0x0685. The numbers you entered are moved to c0b0: c0bf. At this time, I thought of a black box and tried to put all the inputs that could be put into the gameboy. 

It will be Up, down, left, and right keys, a, b, select key. Fortunately, there is a one-to-one correspondence between the k-th input and the value of c0a0 + k.

Finally, you can get the flag by putting "04 04 10 40 08 02 02 20 01 08 01 20 01 20 10 20" in the memory of c0a0 - c0af position.

![alt text](https://raw.githubusercontent.com/junsooo/CTFs/master/18_swampctf/secret_correct.PNG)
