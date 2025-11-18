# -*- coding: utf-8 -*-

import requests

def get_total_download_count(owner, repo):
    """
    通过 GitHub API 获取指定仓库所有 Release 的总下载量。

    Args:
        owner (str): GitHub 仓库的所有者或组织名。
        repo (str): GitHub 仓库名。

    Returns:
        int: 总下载量。如果出错返回 0。
    """
    print(f"开始统计仓库 {owner}/{repo} 的下载量...")
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    all_download_counts = []
    page = 1

    while True:
        try:
            # GitHub API 分页获取，每页最多100个
            params = {'per_page': 100, 'page': page}
            response = requests.get(url, params=params)
            
            # 将 HTTP 状态码转为整数，方便比较
            response.raise_for_status()  # 如果请求失败 (例如 404, 500), 这会抛出异常
            
            releases = response.json()
            if not releases:  # 如果没有更多数据了，就停止循环
                print("所有 Release 页面已获取完毕。")
                break
                
            for release in releases:
                for asset in release.get('assets', []):
                    count = asset.get('download_count', 0)
                    all_download_counts.append(count)
            
            print(f"已处理第 {page} 页，当前累计下载量: {sum(all_download_counts)}")
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"请求 GitHub API 时出错: {e}")
            return 0
        except Exception as e:
            print(f"发生未知错误: {e}")
            return 0

    total_downloads = sum(all_download_counts)
    return total_downloads

# 这是脚本的主入口
if __name__ == "__main__":
    # 在这里配置你的目标仓库
    # 格式：仓库所有者/仓库名
    target_repo = "ruyisdk/riscv-gnu-toolchain-rv64ilp32"
    
    # 分割 owner 和 repo
    owner, repo = target_repo.split('/')
    
    # 调用函数并获取结果
    total_downloads = get_total_download_count(owner, repo)
    
    # 打印最终结果
    if total_downloads > 0:
        print("\n======================================")
        print(f"✅ 统计完成！")
        print(f"📦 仓库 '{target_repo}' 的总下载量为: {total_downloads:,}")
        print("======================================")
    else:
        print("\n❌ 统计失败，请检查仓库地址或网络连接。")

