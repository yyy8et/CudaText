# 椰甲三角洲地块 3D 示意查看器

Windows 原生 Python + Ursina 的最小可运行示意项目，显示 Lot 2063、Lot 774、Lot 618 和 Lot 619 四个可点击色块。使用鼠标拖动旋转视角、滚轮缩放；左键点击地块时，会在启动程序的 PowerShell 窗口输出地块编号、场景 XYZ 和 WGS84 坐标状态。

## 坐标与证据状态

四块地的场景位置只是为了便于查看的示意布局，不代表测绘位置、相邻关系或地块形状。当前没有随项目提供、且可核验地对应这四个 Lot 编号的 GPS 坐标，因此脚本将 WGS84 留空，点击时明确报告“待核实”。不要把场景 XYZ 当作经纬度或产权边界。

添加经核实的地理坐标时，在 `main_3d.py` 对应地块的数据项中，将 `gps: None` 改为 `(纬度, 经度)`，例如 `gps: (2.0435, 111.4953)`；请先确认这组坐标确实对应该 Lot。

## 部署与运行（PowerShell）

在 PowerShell 中进入本目录：

```powershell
cd C:\Users\yyy8e\Github\CudaText\jakar_lots_3d
```

确认安装了 Windows Python 3.10 或更新版本，并允许当前 PowerShell 会话激活虚拟环境：

```powershell
py --version
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main_3d.py
```

运行后可用鼠标拖动观察，滚轮调整距离。左键点击任一色块，地块信息将打印在同一个 PowerShell 窗口中。关闭 3D 窗口即可退出。

## 文件

- `main_3d.py`：Ursina 场景、EditorCamera、地块标签和点击输出。
- `requirements.txt`：运行库及 lint、类型检查、测试工具。
- `.gitignore`：忽略虚拟环境和 Python 工具缓存。
