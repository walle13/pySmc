#pragma once
SMCHANDLE   g_handle = NULL;

extern "C++" _declspec(dllexport) int __stdcall test1(int a, int b, int c);

extern "C++" _declspec(dllexport) int __stdcall test2(int a, int b);
//extern "C++" _declspec(dllexport) int32 __stdcall SMCOpenEth();
extern "C++" _declspec(dllexport) int  pySMCOpenEth(int ip_1, int ip_2, int ip_3, int ip_4);	//��������

extern "C++" _declspec(dllexport) int32 __stdcall pySMCClose();//�Ͽ�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCWriteOutBit(uint8 ioNum, uint8 IoState);		//OUT�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPause();	// ��ͣ 

extern "C++" _declspec(dllexport) int32 __stdcall pySMCStop();	// ֹͣ

extern "C++" _declspec(dllexport) int32 __stdcall pySMCContinueRun();	//��ͣ�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMove(uint8 iaxis, int32 dlengthIn, uint8 bIfAbs);	//˵���������ƶ� 

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMovePluses(uint8 iaxis, int32 ilength, uint8 bIfAbs);	//˵���������ƶ�,��λ����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVMove(uint8 iaxis, uint8 bIfPositiveDir);	//˵���������˶�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStart();	//����岹ģʽ

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveEnd();	//�岹�˶�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveState();//˵������ȡ�岹״̬

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveRemainSpace();	//˵�����岹�˶�����������߶���

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine1(uint8 iaxis, int32 Distance, int32 dspeed, uint8 bIfAbs);	//˵�����岹�����޸��ٶ�����	1��岹

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine2(uint8 iaxis1, int32 Distance1, uint8 iaxis2, int32 Distance2, int32 dspeed, uint8 bIfAbs);	//˵�����岹�����޸��ٶ�����,2��岹

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLineN(uint8 itotalaxis, int32 DistanceList1, int32 DistanceList2, int32 DistanceList3, int32 DistanceList4, int32 dspeed, uint8 bIfAbs);//˵�����岹�������޸��ٶ�����	N��岹

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMovePause(); //˵���� ������ͣ, �岹��ͣ����Ȼ���Լ���С��

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStop();//˵���� �岹����ֹͣ

extern "C++" _declspec(dllexport) int32 __stdcall pySMCHomeMove(uint8 iaxis); //��������

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetPosition(uint8 iaxis); //��ȡ��ǰ��е����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetWorkPosition(uint8 iaxis); //��ȡ��ǰ�Ĺ�������

extern "C++" _declspec(dllexport) int32 __stdcall pySMCCheckDown(uint8 iaxis);	//�����ֹͣ

extern "C++" _declspec(dllexport) int32 __stdcall pySMCWaitVectLength(double vectlengthIn);	//��ȡ��ǰ�岹 δ��ɳ��� //python �� c++֮��ֻ���int�ʹ��ݣ�����1000��ȥ��С��

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetCurRunVectLength();	//��ȡ��ǰ�岹 �����г���  ���أ�double pvectlength
