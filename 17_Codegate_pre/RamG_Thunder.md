한국어

RamG_Thunder는 Win32 실행 파일이다.

실행시키면 suspicious calculator가 뜨는데 input을 1,2,3,0 을 받는다.
그런데 여기서 4를 입력하면 hidden menu로 가는 걸 알 수 있다.

Hidden menu에서는 stage 1~5를 진행한 후에 ‘c’라는 파일에 어떤 값들을 저장하게 된다.
우리의 목적은 저장하는 값들을 어떻게 어떻게 잘 바꿔서 c파일을 읽는 것으로 추측된다.

이제 stage 1부터 어떤 일을 하는지 알아보자.
Stage 1에서는 User의 key1을 input으로 받고 input과 “4745947459”를 xor한 한 값을 “MVYLXYUARJ”과 같은지 비교한 후 이 두 값이 같으면 if문의 내부로 들어가게 된다.

if문의 내부로 들어가기 위한 key1은 ‘yamyambugs’ 이다.
(중간에 나오는 IsDebuggerPresent는 ret 0으로 쉽게 우회할 수 있다)

넘어가서 stage 5에서도 stage 1과 비슷한 행동을 한다. 
if문의 내부로 들어가기 위한 key5는 ‘hellowfish’ 이다.

User가 바꿀 수 있는 값이 key1과 key5뿐이라고 생각해 이 과정을 마치고 output인 ‘c’ 파일을 보았는데 복구가 덜 된 png파일이 만들어졌다. 뭔가 더 남았다는 것을 알 수 있었다.

다시 바이너리를 보니 stage 2, 3, 4에서도 내부적으로 뭔가 해주는 것을 알 수 있다.

먼저 stage 2에서는 GetAdaptersInfo 함수의 반환값들과 어떤 값들을 또 비교한 후에 if문으로 들어갈지 말지를 결정하게 된다.
GetAdaptersInfo함수는 윈도우의 ipconfig같은 역할을 해주어 각종 네트워크 정보를 가져온다.
if문을 보면 컴퓨터의 ip 주소 세자리와 200,89,120을 비교하게 된다.
왠지 if문의 값을 0으로 만들고 else문 내부로 들어가야 할 것 같은 느낌적인 느낌이 들기 때문에 ollydbg에서 실시간으로 ip주소를 바꿔준 후 stage 3으로 간다.

Stage 3에서는 HKEY_CURRENT_USER의 “Hellow”라는 레지스트리 key를 연 후에 이 key의 문자열 값인 “hellow_FishWorld”를 읽으려 시도한다. 성공하면 if문 내부로 들어간다.

마찬가지로 else문 내부로 가기 위해 regedit을 통해 키들을 만들어주었다.

Stage 4에서는 stage2와 똑같은 행동을 한다.
이번에는 ip를 0.12.41...으로 바꿔주면 된다.

Stage 1,2,3,4,5에서 모든 분기를 변경해주었으니 이제 c.png 파일이 열린다.


Flag : ThANk_yOu_my_PeOP1E


