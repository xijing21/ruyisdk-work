import subprocess
import re
from collections import defaultdict
from datetime import datetime
import os

# 软件包类型与说明的映射
package_type_mapping = {
    "board-image": "系统镜像",
    "emulator": "模拟器",
    "toolchain": "工具链",
    "analyzer": "分析工具",
    "extra": "其它",
    "source": "源代码",
    "board-util": "板级工具"
}

# 细分类型的关键词映射
subtype_keywords = {
    "toolchain": {
        "gnu": "GNU",
        "llvm": "LLVM"
    },
    "emulator": {
        "qemu": "Qemu",
        "box64": "Box64"
    },
    "analyzer": {
        "dynamorio": "Dynamorio"
    }
}

def get_subtype(package_type, package_name):
    """根据软件包类型和名称获取细分类型"""
    if package_type not in subtype_keywords:
        return package_type  # 修改这里：直接返回英文软件包类型
    
    keywords = subtype_keywords[package_type]
    for key, value in keywords.items():
        if key.lower() in package_name.lower():
            return value
    
    return package_type  # 修改这里：直接返回英文软件包类型

def parse_ruyi_output(output):
    """解析ruyi命令输出"""
    packages = defaultdict(list)
    current_package = None
    
    for line in output.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # 检测包名行
        if line.startswith('* '):
            parts = line[2:].split('/')
            if len(parts) == 2:
                package_type = parts[0]
                package_name = parts[1]
                current_package = (package_type, package_name)
                packages[current_package] = []
        
        # 检测版本行
        elif line.startswith('- ') and current_package:
            version_info = line[2:].strip()
            packages[current_package].append(version_info)
    
    return packages

def generate_package_stats(packages):
    """生成软件包详细统计数据"""
    statistics = []
    type_stats = defaultdict(int)
    
    for (package_type, package_name), versions in packages.items():
        # 获取软件包类型说明
        type_description = package_type_mapping.get(package_type, package_type)
        
        # 获取细分类型（现在始终返回英文类型）
        subtype = get_subtype(package_type, package_name)
        
        # 版本数量
        version_count = len(versions)
        
        # 版本列表
        version_list = ", ".join(versions)
        
        # 添加到详细统计
        statistics.append([
            package_type,
            type_description,
            subtype,  # 这里现在会显示英文类型
            package_name,
            str(version_count),
            version_list
        ])
        
        # 使用元组作为键来统计类型
        type_key = (package_type, type_description, subtype)
        type_stats[type_key] += version_count
    
    return statistics, type_stats

def run_ruyi_command():
    """执行ruyi命令并获取输出"""
    try:
        result = subprocess.run(
            ["ruyi", "list", "--name-contains", ""],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"执行ruyi命令出错: {e}")
        return None
    except FileNotFoundError:
        print("未找到ruyi命令，请确保已安装并配置好ruyi")
        return None

def save_to_file(data, filename):
    """将数据保存到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"结果已保存到文件: {os.path.abspath(filename)}")
    except IOError as e:
        print(f"保存文件时出错: {e}")

def generate_type_stats_output(type_stats):
    """生成类型统计输出内容"""
    # 转换为列表并排序
    stats_list = []
    for (p_type, p_desc, subtype), count in type_stats.items():
        stats_list.append([p_type, p_desc, subtype, str(count)])
    
    # 按软件包类型和细分类型排序
    stats_list.sort(key=lambda x: (x[0], x[2]))
    
    # 表头
    headers = ["软件包类型", "软件包类型说明", "细分类型", "版本数量"]
    
    # 计算每列最大宽度
    if stats_list:
        col_widths = [max(len(str(item)) for item in col) 
                     for col in zip(*([headers] + stats_list))]
    else:
        col_widths = [len(h) for h in headers]
    
    # 构建输出内容
    output_lines = ["\n按类型统计版本总数:"]
    
    # 添加表头
    header_row = " | ".join(f"{header:{width}}" for header, width in zip(headers, col_widths))
    output_lines.append(header_row)
    output_lines.append("-" * len(header_row))
    
    # 添加数据行
    for row in stats_list:
        output_lines.append(" | ".join(f"{item:{width}}" for item, width in zip(row, col_widths)))
    
    return "\n".join(output_lines)

def generate_package_stats_output(statistics):
    """生成软件包详细统计输出内容"""
    # 表头
    headers = ["软件包类型", "软件包类型说明", "细分类型", "软件包名", "版本数量", "软件包版本列表"]
    
    # 计算每列最大宽度
    col_widths = [max(len(str(item)) for item in col) for col in zip(*([headers] + statistics))]
    
    # 构建输出内容
    output_lines = ["软件包详细统计:"]
    
    # 添加表头
    header_row = " | ".join(f"{header:{width}}" for header, width in zip(headers, col_widths))
    output_lines.append(header_row)
    output_lines.append("-" * len(header_row))
    
    # 添加数据行
    for row in statistics:
        output_lines.append(" | ".join(f"{item:{width}}" for item, width in zip(row, col_widths)))
    
    return "\n".join(output_lines)

def main():
    # 执行ruyi命令获取输出
    output = run_ruyi_command()
    if not output:
        return
    
    # 解析输出
    packages = parse_ruyi_output(output)
    
    # 生成统计数据
    package_stats, type_stats = generate_package_stats(packages)
    
    # 按软件包类型和名称排序
    package_stats.sort(key=lambda x: (x[0], x[3]))
    
    # 生成输出内容
    output_content = generate_package_stats_output(package_stats)
    output_content += "\n\n" + generate_type_stats_output(type_stats)
    
    # 生成带时间戳的文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ruyi_package_stats_{timestamp}.txt"
    
    # 保存到文件
    save_to_file(output_content, filename)
    
    # 同时在控制台输出
    print("\n统计结果:")
    print(output_content)

if __name__ == "__main__":
    main()
