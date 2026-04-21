import subprocess
from pathlib import Path

# 需要打包的文件列表
TO_ZIP_FILES = [
    "build32/Release/ChanlunX.dll",
    "build64/Release/ChanlunX.dll",
    "缠论主图.txt",
    "效果图.png",
    "效果图2.png",
    "README.md",
]

# 公式文件
FORMULA_FILES = [
    "三浪下跌.txt",
    "五彩K线.txt",
    "五浪下跌.txt",
    "日线线段选股.txt",
]


def main():
    # 版本号：年月日
    date_str = "20260421"

    # 输出文件名
    filename = f"ChanlunX-{date_str}.zip"

    # 删除已有压缩包
    for f in Path(".").glob("*.zip"):
        f.unlink()

    # 收集所有要打包的文件
    files_to_zip = []
    for pattern in TO_ZIP_FILES:
        files_to_zip.extend(Path(".").glob(pattern))

    for pattern in FORMULA_FILES:
        p = Path(pattern)
        if p.exists():
            files_to_zip.append(p)

    # 转换为相对路径字符串
    file_paths = [str(f) for f in files_to_zip]

    # 构建 7z 命令（无密码）
    cmd = ["C:/Program Files/7-Zip/7z", "a", filename] + file_paths
    print(cmd)

    # 执行压缩
    subprocess.run(cmd, check=True)

    # 输出结果
    print(f"\n输出文件: {filename}")


if __name__ == "__main__":
    main()