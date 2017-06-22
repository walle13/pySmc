#pragma once
SMCHANDLE   g_handle = NULL;

extern "C++" _declspec(dllexport) int __stdcall test1(int a, int b, int c);

extern "C++" _declspec(dllexport) int __stdcall test2(int a, int b);
//extern "C++" _declspec(dllexport) int32 __stdcall SMCOpenEth();
extern "C++" _declspec(dllexport) int  pySMCOpenEth(int ip_1, int ip_2, int ip_3, int ip_4);	//建立连接

extern "C++" _declspec(dllexport) int32 __stdcall pySMCClose();//断开连接

extern "C++" _declspec(dllexport) int32 __stdcall pySMCWriteOutBit(uint8 ioNum, uint8 IoState);		//OUT口输出

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPause();	// 暂停 

extern "C++" _declspec(dllexport) int32 __stdcall pySMCStop();	// 停止

extern "C++" _declspec(dllexport) int32 __stdcall pySMCContinueRun();	//暂停后继续

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMove(uint8 iaxis, double dlength, uint8 bIfAbs);	//说明：定速移动 

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMovePluses(uint8 iaxis, int32 ilength, uint8 bIfAbs);	//说明：定长移动,单位脉冲

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVMove(uint8 iaxis, uint8 bIfPositiveDir);	//说明：定速运动

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStart();	//进入插补模式

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveEnd();	//插补运动结束

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveState(uint8 pState);//说明：读取插补状态

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveRemainSpace(uint32 pSpace);	//说明：插补运动可以填入的线段数

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine1(uint8 iaxis, double Distance, double dspeed, uint8 bIfAbs);	//说明：插补，会修改速度设置	1轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine2(uint8 iaxis1, double Distance1, uint8 iaxis2, double Distance2, double dspeed, uint8 bIfAbs);	//说明：插补，会修改速度设置,2轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLineN(uint8 itotalaxis, uint8 piaxisList, double DistanceList, double dspeed, uint8 bIfAbs);//说明：插补，不会修改速度设置	N轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMovePause(); //说明： 运行暂停, 插补暂停后仍然可以加入小段

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStop();//说明： 插补运行停止

extern "C++" _declspec(dllexport) int32 __stdcall pySMCHomeMove(uint8 iaxis); //回零运用

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetPosition(uint8 iaxis); //读取当前机械坐标

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetWorkPosition(uint8 iaxis); //读取当前的工件坐标