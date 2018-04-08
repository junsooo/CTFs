window of opportunity(swampctf 2018)

v3 = &unk_6020C0;                             // [4,6,8,11,15,7,31,5,14]
v18 = (__int64 (__fastcall *)())sub_400C70;   // print("Not Authorized")
sigaction(v4, (const struct sigaction *)&v18, 0LL);

sigaction에서 v3에 해당하는 element에 대해 action을 한다.
저거 보면 illigal instruction, alarm 등이 있는데 그 상황이 오면 print “Not Authorized”를 출력해주는거임

Get time. 으로 token을 만들어주고
마지막에 v8에 이상한 값을 대입해주는데 이걸 실행해줌.
v9(2)로 
여기서 token으로 xor해주는데 이거 보면 이부분 코드를 실행해주는 것을 알 수 있음.

다른 사람들은 token 만드는 식 보고 key를 한정했다는데 이부분은 잘 모르겠음