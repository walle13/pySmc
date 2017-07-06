// pySmc.cpp : 定义 DLL 应用程序的导出函数。
//python没有指针，打包生产python使用的dll库 2017.5.24 周先军

#include "stdafx.h"
#include <iostream>
#include "smc6200.h"
#include "pySmc.h"
# include <stdlib.h>
# include <string>
using namespace std;


int __stdcall test1(int a, int  b, int c)
{
	
	SMCOpenEth("192.168.1.11", &g_handle);
	return a + b + c;
}

int __stdcall test2(int a, int b)
{
	return a - b;
}

/*************************************************************
说明：与控制器建立链接
输入：IP地址，字符串的方式输入
输出：卡链接handle
返回值：错误码
*************************************************************/

int len_x(int x)
{
	int len = 0;
	if (x)
	{
		while (x)
		{
			len++;
			x /= 10;
		}
	}
	else
		len = 1;
	return len;
}

int pySMCOpenEth(int ip_1, int ip_2, int ip_3, int ip_4)
{
	
	string s_ip_1, s_ip_2, s_ip_3, s_ip_4;
	string ip_addr;

	char *c_ip_1 = new char[len_x(ip_1) + 1];
	char *c_ip_2 = new char[len_x(ip_2) + 1];
	char *c_ip_3 = new char[len_x(ip_3) + 1];
	char *c_ip_4 = new char[len_x(ip_4) + 1];
	char *c_ip_addr;

	_itoa_s(ip_1, c_ip_1, len_x(ip_1) + 1, 10);
	_itoa_s(ip_2, c_ip_2, len_x(ip_2) + 1, 10);
	_itoa_s(ip_3, c_ip_3, len_x(ip_3) + 1, 10);

	_itoa_s(ip_4, c_ip_4, len_x(ip_4) + 1, 10);
	s_ip_1 = c_ip_1;
	s_ip_2 = c_ip_2;
	s_ip_3 = c_ip_3;
	s_ip_4 = c_ip_4;
	delete []c_ip_1;
	delete []c_ip_2;
	delete []c_ip_3;
	delete []c_ip_4;
	ip_addr = s_ip_1 + "." + s_ip_2 + "." + s_ip_3 + "." + s_ip_4;
	
	const int len = ip_addr.length();
	c_ip_addr = new char[len + 1];
	strcpy_s(c_ip_addr, len + 1, ip_addr.c_str());

	return SMCOpenEth(c_ip_addr, &g_handle);
	delete[]c_ip_addr;
}


/*************************************************************
说明：关闭控制器链接
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCClose()
{
	return(SMCClose(g_handle));
}

/*************************************************************
说明：写输出口
输入：卡链接handle io编号，从1开始 0-低电平， 1- 高电平
输出：
返回值：错误码
int32 __stdcall pySMCWriteOutBit(uint8  ioNum, uint8 IoState)
*************************************************************/
int32 __stdcall pySMCWriteOutBit(uint8  ioNum, uint8 IoState)
{
	//SMCPMove(g_handle,1,1000,1);
	return(SMCWriteOutBit(g_handle, ioNum, IoState));
}

/*

/*************************************************************
说明：暂停
输入：卡链接handle 文件名， 当为NULL的时候运行缺省文件
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCPause()
{
	
	return(SMCPause(g_handle));
} 


/*************************************************************
说明：停止
输入：卡链接handle 文件名， 当为NULL的时候运行缺省文件
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCStop()
{
	return(SMCStop(g_handle));
}


/*************************************************************
说明：点亮LED，或者灭掉
输入：卡链接handle led编号，从1开始
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCWriteLed( uint16 iLedNum, uint8 bifLighten)
{
	return(SMCWriteLed(g_handle, iLedNum, bifLighten));
}


/*************************************************************
说明：读取程序当前行
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetCurRunningLine( uint32 pLineNum)
{
	return(SMCGetCurRunningLine(g_handle, &pLineNum));
}


/*************************************************************
说明：暂停后继续运行
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCContinueRun()
{
	return(SMCContinueRun(g_handle));
}

/*************************************************************
说明：回零，回零模式通过参数指定
输入：卡链接handle 轴号， 方向
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCHomeMove(uint8 iaxis)
{
	return(SMCHomeMove(g_handle, iaxis));
}


/*************************************************************
说明：定速移动 不能用
输入：卡链接handle 轴号， 长度， 是否绝对移动
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCPMove( uint8 iaxis, int32 dlengthIn, uint8 bIfAbs)
{
	double dlength = double(dlengthIn / 1000);
	return(SMCPMove(g_handle, iaxis, dlength, bIfAbs));
}


/*************************************************************
说明：定长移动，单位脉冲
输入：卡链接handle 轴号， 长度， 是否绝对移动
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCPMovePluses( uint8 iaxis, int32 ilength, uint8 bIfAbs)
{
	return(SMCPMovePluses(g_handle, iaxis, ilength, bIfAbs));
}


/*************************************************************
说明：定速运动
输入：卡链接handle 轴号， 方向
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVMove( uint8 iaxis, uint8 bIfPositiveDir)
{
	return(SMCVMove(g_handle, iaxis, bIfPositiveDir));
}


/*************************************************************
说明：进入插补运动模式
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveStart()
{
	return(SMCVectMoveStart(g_handle));
}


/*************************************************************
说明：插补结束/我觉得不是这样
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveEnd()
{
	return(SMCVectMoveEnd(g_handle));
}


/*************************************************************
//  VECTMOVE_STATE_RUNING = 1,
    VECTMOVE_STATE_PAUSE = 2,
    VECTMOVE_STATE_STOP = 3,
说明：读取插补状态
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectMoveState()
{
	uint8 pstate[1];
	SMCGetVectMoveState(g_handle, pstate);
	uint8 apstate = pstate[0];
	return apstate;
}


/*************************************************************
说明：插补运动可以填入的线段数
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectMoveRemainSpace()
{
	uint32 pSpace[1];
	SMCGetVectMoveRemainSpace(g_handle, pSpace);
	uint32 pSpaceOut = pSpace[0];
	return pSpaceOut;
}


/*************************************************************
说明：插补，会修改速度设置	1轴插补
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveLine1( uint8 iaxis, double Distance, double dspeed, uint8 bIfAbs)
{
	double _tanceList;
	_tanceList = double(Distance / 1000);	//python 与 c++之间只完成int型传递，扩大1000倍去掉小数
	return(SMCVectMoveLine1(g_handle, iaxis, _tanceList, dspeed, bIfAbs));
}
/*************************************************************
说明：插补，会修改速度设置	2轴插补
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveLine2( uint8 iaxis1, double Distance1, uint8 iaxis2, double Distance2, double dspeed, uint8 bIfAbs)
{
	double _tanceList1 = double(Distance1 / 1000);	//python 与 c++之间只完成int型传递，扩大1000倍去掉小数
	double _tanceList2 = double(Distance2 / 1000);
	return(SMCVectMoveLine2(g_handle, iaxis1, _tanceList1, iaxis2, _tanceList2, dspeed, bIfAbs));
}

/*************************************************************
说明：插补，不会修改速度设置	N轴插补
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveLineN(uint8 itotalaxis, int32 DistanceList1, int32 DistanceList2, int32 DistanceList3, int32 DistanceList4, int32 dspeed, uint8 bIfAbs)
{
	//double _tanceList[] = { DistanceList1, DistanceList2, DistanceList3, DistanceList4 };
	double _tanceList[4];
	_tanceList[0] = double(DistanceList1 / 1000);	//python 与 c++之间只完成int型传递，扩大1000倍去掉小数
	_tanceList[1] = double(DistanceList2 / 1000);
	_tanceList[2] = double(DistanceList3 / 1000);
	_tanceList[3] = double(DistanceList4 / 1000);
	uint8 _axis_iaxis[] = { 0, 1, 2, 3 };
	double _dspeed = double(dspeed);
	return(SMCVectMoveLineN(g_handle, itotalaxis, _axis_iaxis, _tanceList, _dspeed, bIfAbs));

}


/*************************************************************
说明： 运行暂停, 插补暂停后仍然可以加入小段
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMovePause()
{
	return(SMCVectMovePause(g_handle));
}


/*************************************************************
说明： 插补运行停止
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveStop()
{
	return(SMCVectMoveStop(g_handle));
}

double dspeed[1];
double dmachine[1];
double dWCS[1];
/*************************************************************
说明：  读取当前机械坐标
输入：卡链接handle 轴号
输出：坐标
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetPosition(uint8 iaxis)
{
	SMCGetPosition(g_handle, iaxis, dmachine);		//机械坐标
	int32 machine = dmachine[0]*10000;
	return machine;
}


/*************************************************************
说明： 读取当前的工件坐标
输入：卡链接handle 轴号
输出：坐标
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetWorkPosition(uint8 iaxis)
{
	SMCGetWorkPosition(g_handle, iaxis, dWCS);		 //工件坐标
	int32 WCS = dWCS[0] * 10000;
	return WCS;
}


/*************************************************************
说明：检查轴停止
输入：卡链接handle 轴号， 方向
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCCheckDown( uint8 iaxis)
{
	uint8 pbIfDown[1];
	uint8 iaxisDown = pbIfDown[0];
	SMCCheckDown(g_handle, iaxis, pbIfDown);
	return iaxisDown;
}

/*************************************************************
说明： //读取当前插补  //python 与 c++之间只完成int型传递，扩大1000倍去掉小数
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCWaitVectLength( double vectlengthIn)
{
	double vectlength = double(vectlengthIn / 1000);	//python 与 c++之间只完成int型传递，扩大1000倍去掉小数
	SMCWaitVectLength(g_handle, vectlength);
	int32 vectlengthOut = int(vectlength);
	return  vectlength;
} 

/*************************************************************
说明：	//读取当前插补 已运行长度
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetCurRunVectLength()
{
	double pvectlengthIn[1];
	SMCGetCurRunVectLength(g_handle, pvectlengthIn);
	int32 pvectlength = int(pvectlengthIn[0]*1000);	//python 与 c++之间只完成int型传递，扩大1000倍去掉小数 返回：double pvectlength
	return pvectlength;
}

/*************************************************************
说明：检查是否回零中。
输入：卡链接handle 轴号
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCIfHomeMoveing( uint8 iaxis)
{
	uint8 pbIfHoming[1];
	SMCIfHomeMoveing(g_handle, iaxis, pbIfHoming);
	uint8 pbIfHomingOut = pbIfHoming[0];
	return pbIfHomingOut;
}

/*************************************************************
说明： 设置当前坐标
输入：卡链接handle 轴号 坐标
输出：
返回值：错误码
*************************************************************/
double __stdcall pySMCSetPosition( uint8 iaxis, double dpositionIn)
{
	//int32 dposition = int32(dpositionIn);
	//return(SMCSetPosition(g_handle,  iaxis,  dposition));
	if (dpositionIn == 1024.4)
	{	
		double double_buff = 1.11;
		return double_buff;
	}
	else
	{
		double double_buff = 0.11;
		return double_buff;
	}	
}


/*************************************************************
说明： 读取工件零点
输入：卡链接handle 轴号
输出：坐标
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetWorkOriginPosition( uint8 iaxis)
{
	double pposition[1];
	SMCGetWorkOriginPosition(g_handle, iaxis ,pposition);
	int ppositionOut = int(pposition[0]);
	return ppositionOut;
}


/************************************************************************************************************************
参数文件相关函数
/************************************************************************************************************************


/*************************************************************
说明：上传下载设置时， 通用的字符串接口。
输入：卡链接handle 发送字符串，接收字符串， 接收字符串长度, 当不想要应答时，把uiResponseLength = 0
输出：
handle 链接标识
pszCommand 命令字符串
psResponse 返回结果字符串
uiResponseLength 结果字符串缓冲的最大长度
返回值：错误码
***********************************************************
int32 __stdcall pySMCCommand( const char* pszCommand, char* psResponse, uint32 uiResponseLength)
{
	SMCCommand(g_handle, const char* pszCommand, char* psResponse, uiResponseLength);
}
**/

/*************************************************************
说明：当前设置存盘
输入：卡链接handle
输出：
返回值：错误码
***************************************************************/
int32 __stdcall pySMCBurnSetting()
{
	return(SMCBurnSetting(g_handle));
}


/*************************************************************
说明：修改 IP 地址设置。
输入：卡链接handle
输出：
handle 链接标识
sIpAddr IP 地址字符串
sGateAddr 网关地址字符串
sMask 掩码字符串
bifdhcp 是否采用 DHCP
返回值：错误码
*************************************************************
int32 __stdcall pySMCSetIpAddr( const char* sIpAddr, const char* sGateAddr, const char* sMask, uint8 bifdhcp)
{
	SMCSetIpAddr(g_handle, const char* sIpAddr, const char* sGateAddr, const char* sMask, bifdhcp);
}
**/
/*************************************************************
说明：读取 IP 地址设置。
输入：卡链接handle
输出：
handle 链接标识
sIpAddr 返回 IP 地址字符串
sGateAddr 返回网关地址字符串
sMask 返回掩码字符串
pbifdhcp 返回是否采用 DHCP
返回值：错误码
*************************************************************
int32 __stdcall pySMCGetIpAddr(char* sIpAddr, char* sGateAddr, char* sMask, uint8 *pbifdhcp)
{
	SMCGetIpAddr(g_handle, char* sIpAddr, char* sGateAddr, char* sMask, uint8 *pbifdhcp);
}**/

/*************************************************************
说明：读取当前控制器的IP地址, 注意:当设置dhcp以后，设置的IP与实际的不一致。
输入：卡链接handle
handle 链接标识
sIpAddr 返回 IP 地址字符串
输出：
返回值：错误码
*************************************************************
int32 __stdcall pySMCGetCurIpAddr( char* sIpAddr)
{
	SMCGetCurIpAddr(g_handle, char* sIpAddr);
}
** /

/*************************************************************
说明：修改回零速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetZeroSpeed( uint8 iaxis, uint32 uiSpeed)
{
	return(SMCSetZeroSpeed(g_handle, iaxis, uiSpeed));
}

/*************************************************************
说明：读取回零速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetZeroSpeed( uint8 iaxis)
{
	uint32 puiSpeed[1];
	SMCGetLocateSpeed(g_handle, iaxis, puiSpeed);
	uint32 puiSpeedOut = puiSpeed[0];
	return puiSpeedOut;
}

/*************************************************************
说明：修改单轴速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetLocateSpeed( uint8 iaxis, uint32 uiSpeed)
{
	return(SMCSetLocateSpeed(g_handle, iaxis, uiSpeed));
}

/*************************************************************
说明：读取单轴速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetLocateSpeed( uint8 iaxis)
{
	uint32 puiSpeed[1];
	SMCGetLocateSpeed(g_handle, iaxis, puiSpeed);
	uint32 puiSpeedOut = puiSpeed[0];
	return puiSpeedOut;
}

/*************************************************************
说明：修改单轴起始速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetLocateStartSpeed( uint8 iaxis, uint32 uiSpeed)
{
	return(SMCSetLocateStartSpeed(g_handle, iaxis, uiSpeed));
}

/*************************************************************
说明：读取单轴起始速度设置
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetLocateStartSpeed( uint8 iaxis)
{
	uint32 puiSpeed[1];
	SMCGetLocateStartSpeed(g_handle, iaxis, puiSpeed);
	uint32 puiSpeedOut = puiSpeed[0];
	return puiSpeedOut;
}


/*************************************************************
说明：修改单轴加速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetLocateAcceleration( uint8 iaxis, uint32 uiValue)
{
	return(SMCSetLocateAcceleration(g_handle, iaxis, uiValue));
}

/*************************************************************
说明：读取单轴加速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetLocateAcceleration( uint8 iaxis)
{
	uint32 puiValue[1];
	SMCGetLocateAcceleration(g_handle, iaxis, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}

/*************************************************************
说明：修改单轴减速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetLocateDeceleration( uint8 iaxis, uint32 uiValue)
{
	return(SMCSetLocateDeceleration(g_handle, iaxis, uiValue));
}

/*************************************************************
说明：读取单轴减速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetLocateDeceleration( uint8 iaxis)
{
	uint32 puiValue[1];
	SMCGetLocateDeceleration(g_handle, iaxis, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}

/*************************************************************
说明：修改脉冲当量设置（即用户单位对应脉冲数）。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetUnitPulses( uint8 iaxis, uint32 uiValue)
{
	return(SMCSetUnitPulses(g_handle, iaxis, uiValue));
}

/*************************************************************
说明：读取脉冲当量设置（即用户单位对应脉冲数）。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetUnitPulses( uint8 iaxis)
{
	uint32 puiValue[1];
	SMCGetUnitPulses(g_handle, iaxis, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;

}


/*************************************************************
说明：修改插补起始速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetVectStartSpeed( uint32 uiValue)
{
	return(SMCSetVectStartSpeed(g_handle, uiValue));
}

/*************************************************************
说明：读取插补起始速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectStartSpeed()
{
	uint32 puiValue[1];
	SMCGetVectStartSpeed(g_handle, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}

/*************************************************************
说明：修改插补最高速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetVectSpeed( uint32 uiValue)
{
	return(SMCSetVectSpeed(g_handle, uiValue));
}

/*************************************************************
说明：读取插补最高速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectSpeed()
{
	uint32 puiValue[1];
	SMCGetVectSpeed(g_handle, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}

/*************************************************************
说明：修改插补加速度设置
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetVectAcceleration( uint32 uiValue)
{
	return(SMCSetVectAcceleration(g_handle, uiValue));
}

/*************************************************************
说明：读取插补加速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectAcceleration()
{
	uint32 puiValue[1];
	SMCGetVectAcceleration(g_handle, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}


/*************************************************************
说明：修改插补减速度设置。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCSetVectDeceleration( uint32 uiValue)
{
	return(SMCSetVectDeceleration(g_handle, uiValue));
}

/*************************************************************
说明：读取插补减速度设置,返回 uint32 puiValueOut。
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectDeceleration()
{
	uint32 puiValue[1];
	SMCGetVectDeceleration(g_handle, puiValue);
	uint32 puiValueOut = puiValue[0];
	return puiValueOut;
}

