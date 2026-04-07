# ChanlunX

## 如何编译

### 编译 32 位版本

适用于通达信 32 位版本：

```cmd
mkdir build
cd build
cmake -A Win32 ..
cmake --build . --config Release
```

### 编译 64 位版本

适用于通达信 64 位版本：

```cmd
mkdir build
cd build
cmake -A x64 ..
cmake --build . --config Release
```

> **注意**: 请根据通达信软件的位数选择对应的 DLL 版本。32 位通达信需使用 32 位 DLL，64 位通达信需使用 64 位 DLL。

## 主图代码

把编译好的DLL放到通达信的T0002\dlls目录，绑定为2号函数，下面的代码做成通达信主图公式。

```text
FRAC:=TDXDLL2(2,H,L,0);{标准笔}
NOTEXT画上升笔2:DRAWLINE(FRAC=-1,L,FRAC=+1,H,0), DOTLINE,COLORYELLOW;
NOTEXT画下降笔2:DRAWLINE(FRAC=+1,H,FRAC=-1,L,0), DOTLINE, COLORYELLOW;

BIZG:=TDXDLL2(5,FRAC,H,L);{输出BI中枢高}
BIZD:=TDXDLL2(6,FRAC,H,L);{输出BI中枢低}
BISE:=TDXDLL2(7,FRAC,H,L);{输出BI中枢开始和结束}

NOTEXT_BIZG:IF(BIZG,BIZG,DRAWNULL),COLORYELLOW;{画BI中枢高}
NOTEXT_BIZD:IF(BIZD,BIZD,DRAWNULL),COLORYELLOW;{画BI中枢低}
NOTEXT_BISE:STICKLINE(BISE,BIZD,BIZG,0,0),COLORYELLOW;{画BI中枢起始结束};

DUAN1:=TDXDLL2(3,FRAC,H,L);{计算段的端点,3改成4是1+1终结画法}
NOTEXT画上升段1:DRAWLINE(DUAN1=-1,L,DUAN1=+1,H,0), COLORFF8000;
NOTEXT画下降段1:DRAWLINE(DUAN1=+1,H,DUAN1=-1,L,0), COLORFF8000;

DUANZG1:=TDXDLL2(5,DUAN1,H,L);{输出段中枢高}
DUANZD1:=TDXDLL2(6,DUAN1,H,L);{输出段中枢低}
DUANSE1:=TDXDLL2(7,DUAN1,H,L);{输出段中枢开始和结束}

NOTEXT_DDUANZG1:IF(DUANZG1,DUANZG1,DRAWNULL),COLORFF8000;{画段中枢高}
NOTEXT_DDUANZD1:IF(DUANZD1,DUANZD1,DRAWNULL),COLORFF8000;{画段中枢低}
NOTEXT_DDUANSE1:STICKLINE(DUANSE1,DUANZD1,DUANZG1,0,0),COLORFF8000;{画段中枢起始结束};
```

## 社区

如果开源版不知道自己怎么动手搞定的，可以参与我的社区，我会协助你安装。

### 安装指南

- [番茄缠论插件 FqChan04 TDX 安装指南 20260405 更新](https://mp.weixin.qq.com/s/v3uchXfQLACdeEoV6CN65Q)

并且我也有全能的量化版本开发计划，可以一起研究冲浪。

### 更多

- 支持作者：https://mp.weixin.qq.com/s/xKBIlmBp9iyYg7wpLc5bPw
- 给作者充电：http://s.a0c.top/lJ1c8WZ/4KHZ
- 缠论X星球: https://t.zsxq.com/0aDUuhQC5
- 纷传圈子：http://s.a0c.top/uHvyCEy/4KHZ
- WeChat: kldcty
- QQ: 1106628276
- 微信公众号: kldctymp
