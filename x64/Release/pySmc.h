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

extern "C++" _declspec(dllexport) int32 __stdcall pySMCIfHomeMoveing(uint8 iaxis);	//����Ƿ�����С�

//********************************************************************//
extern "C++" _declspec(dllexport) int32 __stdcall pySMCBurnSetting();	//��ǰ���ô��̣�������¼�� FLASH����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetZeroSpeed(uint8 iaxis, uint32 uiSpeed); //�޸Ļ����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetZeroSpeed(uint8 iaxis);	//��ȡ�����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateSpeed(uint8 iaxis, uint32 uiSpeed);	//�޸ĵ����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateSpeed(uint8 iaxis);	//��ȡ�����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateStartSpeed(uint8 iaxis, uint32 uiSpeed);	//�޸ĵ�����ʼ�ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateStartSpeed(uint8 iaxis);	//��ȡ������ʼ�ٶ�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateAcceleration(uint8 iaxis, uint32 uiValue);	//�޸ĵ�����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateAcceleration(uint8 iaxis);	//��ȡ������ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateDeceleration(uint8 iaxis, uint32 uiValue);	//�޸ĵ�����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateDeceleration(uint8 iaxis);	//�޸ĵ�����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetUnitPulses(uint8 iaxis, uint32 uiValue);	//�޸����嵱�����ã����û���λ��Ӧ����������

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetUnitPulses(uint8 iaxis);	//��ȡ���嵱�����ã����û���λ��Ӧ����������

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectStartSpeed(uint32 uiValue);		//�޸Ĳ岹��ʼ�ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectStartSpeed();	//��ȡ�岹��ʼ�ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectSpeed(uint32 uiValue);	//�޸Ĳ岹����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectSpeed();	//��ȡ�岹����ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectAcceleration(uint32 uiValue);	//�޸Ĳ岹���ٶ�����

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectAcceleration();	//��ȡ�岹���ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectDeceleration(uint32 uiValue);	//�޸Ĳ岹���ٶ����á�

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectDeceleration();	//��ȡ�岹���ٶ�����,���� uint32 puiValueOut��


/*
pySMCBurnSetting
pySMCSetZeroSpeed
pySMCGetZeroSpeed
pySMCSetLocateSpeed
pySMCGetLocateSpeed
pySMCSetLocateStartSpeed
pySMCGetLocateStartSpeed
pySMCSetLocateAcceleration
pySMCGetLocateAcceleration
pySMCSetLocateDeceleration
pySMCGetLocateDeceleration
pySMCSetUnitPulses
pySMCGetUnitPulses
pySMCSetVectStartSpeed
pySMCGetVectStartSpeed
pySMCSetVectSpeed
pySMCGetVectSpeed
pySMCSetVectAcceleration
pySMCGetVectAcceleration
pySMCSetVectDeceleration
pySMCGetVectDeceleration*/