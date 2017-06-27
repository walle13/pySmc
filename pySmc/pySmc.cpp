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
int32 __stdcall pySMCPMove( uint8 iaxis, double dlength, uint8 bIfAbs)
{
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
说明：插补结束
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCVectMoveEnd()
{
	return(SMCVectMoveEnd(g_handle));
}


/*************************************************************
说明：读取插补状态
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectMoveState( uint8 pState)
{
	return(SMCGetVectMoveState(g_handle, &pState));
}


/*************************************************************
说明：插补运动可以填入的线段数
输入：卡链接handle
输出：
返回值：错误码
*************************************************************/
int32 __stdcall pySMCGetVectMoveRemainSpace( uint32 pSpace)
{
	return(SMCGetVectMoveRemainSpace(g_handle, &pSpace));
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
	return(SMCVectMoveLineN(g_handle, itotalaxis, _axis_iaxis, _tanceList, dspeed, bIfAbs));

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
/*
void CDMC6480d1Dlg::OnTimer(UINT nIDEvent)
{
	// TODO: Add your message handler code here and/or call default
	double dspeed[1];
	double dmachine[1];
	double dWCS[1];
	int32 iresult;
	CString string;
	unsigned char pbIfDown[1];
	if (NULL != g_handle)
	{
		iresult = SMCGetCurSpeed(g_handle, m_moveAxis, dspeed);
		if (ERR_OK == iresult)
		{
			string.Format("%.2lf", dspeed[0]);
			GetDlgItem(IDC_EDIT_SPEED)->SetWindowText(string);
		}

		iresult = SMCGetPosition(g_handle, m_moveAxis, dmachine);   //机械坐标
		if (ERR_OK == iresult)
		{
			string.Format("%.2lf", dmachine[0]);
			GetDlgItem(IDC_EDIT_COOR_MACHINE)->SetWindowText(string);
		}

		iresult = SMCGetWorkPosition(g_handle, m_moveAxis, dWCS);  //工件坐标
		if (ERR_OK == iresult)
		{
			string.Format("%.2lf", dWCS[0]);
			GetDlgItem(IDC_EDIT_POSE)->SetWindowText(string);
		}
		iresult = SMCCheckDown(g_handle, m_moveAxis, pbIfDown);
		if (ERR_OK == iresult)
		{
			if (pbIfDown[0] == 1)
			{
				GetDlgItem(IDC_EDIT_STATE)->SetWindowText("停止");
			}
			else
			{
				GetDlgItem(IDC_EDIT_STATE)->SetWindowText("运动中");
			}
		}
	}
	*/
