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

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMove(uint8 iaxis, int32 dlengthIn, uint8 bIfAbs);	//说明：定速移动 

extern "C++" _declspec(dllexport) int32 __stdcall pySMCPMovePluses(uint8 iaxis, int32 ilength, uint8 bIfAbs);	//说明：定长移动,单位脉冲

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVMove(uint8 iaxis, uint8 bIfPositiveDir);	//说明：定速运动

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStart();	//进入插补模式

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveEnd();	//插补运动结束

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveState();//说明：读取插补状态

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectMoveRemainSpace();	//说明：插补运动可以填入的线段数

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine1(uint8 iaxis, int32 Distance, int32 dspeed, uint8 bIfAbs);	//说明：插补，会修改速度设置	1轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLine2(uint8 iaxis1, int32 Distance1, uint8 iaxis2, int32 Distance2, int32 dspeed, uint8 bIfAbs);	//说明：插补，会修改速度设置,2轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveLineN(uint8 itotalaxis, int32 DistanceList1, int32 DistanceList2, int32 DistanceList3, int32 DistanceList4, int32 dspeed, uint8 bIfAbs);//说明：插补，不会修改速度设置	N轴插补

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMovePause(); //说明： 运行暂停, 插补暂停后仍然可以加入小段

extern "C++" _declspec(dllexport) int32 __stdcall pySMCVectMoveStop();//说明： 插补运行停止

extern "C++" _declspec(dllexport) int32 __stdcall pySMCHomeMove(uint8 iaxis); //回零运用

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetPosition(uint8 iaxis); //读取当前机械坐标

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetWorkPosition(uint8 iaxis); //读取当前的工件坐标

extern "C++" _declspec(dllexport) int32 __stdcall pySMCCheckDown(uint8 iaxis);	//检查轴停止

extern "C++" _declspec(dllexport) int32 __stdcall pySMCWaitVectLength(double vectlengthIn);	//读取当前插补 未完成长度 //python 与 c++之间只完成int型传递，扩大1000倍去掉小数

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetCurRunVectLength();	//读取当前插补 已运行长度  返回：double pvectlength

extern "C++" _declspec(dllexport) int32 __stdcall pySMCIfHomeMoveing(uint8 iaxis);	//检查是否回零中。

//********************************************************************//
extern "C++" _declspec(dllexport) int32 __stdcall pySMCBurnSetting();	//当前设置存盘（设置烧录到 FLASH）。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetZeroSpeed(uint8 iaxis, uint32 uiSpeed); //修改回零速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetZeroSpeed(uint8 iaxis);	//读取回零速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateSpeed(uint8 iaxis, uint32 uiSpeed);	//修改单轴速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateSpeed(uint8 iaxis);	//读取单轴速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateStartSpeed(uint8 iaxis, uint32 uiSpeed);	//修改单轴起始速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateStartSpeed(uint8 iaxis);	//读取单轴起始速度设置

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateAcceleration(uint8 iaxis, uint32 uiValue);	//修改单轴加速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateAcceleration(uint8 iaxis);	//读取单轴加速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetLocateDeceleration(uint8 iaxis, uint32 uiValue);	//修改单轴减速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetLocateDeceleration(uint8 iaxis);	//修改单轴减速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetUnitPulses(uint8 iaxis, uint32 uiValue);	//修改脉冲当量设置（即用户单位对应脉冲数）。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetUnitPulses(uint8 iaxis);	//读取脉冲当量设置（即用户单位对应脉冲数）。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectStartSpeed(uint32 uiValue);		//修改插补起始速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectStartSpeed();	//读取插补起始速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectSpeed(uint32 uiValue);	//修改插补最高速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectSpeed();	//读取插补最高速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectAcceleration(uint32 uiValue);	//修改插补加速度设置

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectAcceleration();	//读取插补加速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCSetVectDeceleration(uint32 uiValue);	//修改插补减速度设置。

extern "C++" _declspec(dllexport) int32 __stdcall pySMCGetVectDeceleration();	//读取插补减速度设置,返回 uint32 puiValueOut。


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