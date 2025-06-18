import requests
import os
import json
from datetime import datetime
import pandas as pd
import time

def get_org_contributors(org_name, token):
    """获取组织所有贡献者（Members + Outside collaborators）"""
    headers = {"Authorization": f"token {token}"}
    contributors = set()
    
    for endpoint in ['members', 'outside_collaborators']:
        url = f"https://api.github.com/orgs/{org_name}/{endpoint}?per_page=100"
        while url:
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                if isinstance(data, dict) and 'message' in data:
                    print(f"警告: {data['message']}")
                    break
                    
                contributors.update(user['login'] for user in data if isinstance(user, dict))
                url = response.links.get('next', {}).get('url')
                time.sleep(0.5)
            except Exception as e:
                print(f"获取贡献者时出错: {str(e)}")
                break
    
    return sorted(contributors)

def get_org_repos_stats(org_name, token):
    headers = {"Authorization": f"token {token}"}
    session = requests.Session()
    session.headers.update(headers)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("=== 开始统计 ===")
    
    # 1. 获取组织贡献者
    print("\n[1/3] 获取组织贡献者列表...")
    org_contributors = get_org_contributors(org_name, token)
    print(f"找到 {len(org_contributors)} 位组织贡献者")
    
    # 2. 获取所有仓库基础信息
    print("\n[2/3] 获取仓库列表...")
    repos = []
    page = 1
    while True:
        try:
            url = f"https://api.github.com/orgs/{org_name}/repos?page={page}&per_page=100"
            response = session.get(url)
            data = response.json()
            
            if not data:
                break
                
            repos.extend([{
                'name': repo['name'],
                'forks': repo['forks_count'],
                'stars': repo['stargazers_count'],
                'watchers': repo['watchers_count']
            } for repo in data if isinstance(repo, dict)])
            
            page += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"获取仓库列表出错: {str(e)}")
            break
    
    print(f"共找到 {len(repos)} 个仓库")
    
    # 3. 处理仓库数据（不再获取contributors）
    print("\n[3/3] 处理仓库统计...")
    repo_stats = []
    for i, repo in enumerate(repos, 1):
        repo_name = repo['name']
        print(f"  [{i}/{len(repos)}] 处理: {repo_name}")
        
        # 获取Issues和PRs
        issues = prs = 0
        issues_url = f"https://api.github.com/repos/{org_name}/{repo_name}/issues?state=all&per_page=100"
        
        while issues_url:
            try:
                response = session.get(issues_url)
                data = response.json()
                
                if isinstance(data, dict) and 'message' in data:
                    print(f"    获取issues/PRs失败: {data['message']}")
                    break
                    
                for item in data:
                    if isinstance(item, dict):
                        if 'pull_request' in item:
                            prs += 1
                        else:
                            issues += 1
                            
                issues_url = response.links.get('next', {}).get('url')
                time.sleep(0.5)
            except Exception as e:
                print(f"    处理issues/PRs时出错: {str(e)}")
                break
        
        repo_stats.append({
            "RepoName": repo_name,
            "Forks": repo['forks'],
            "Stars": repo['stars'],
            "Watchers": repo['watchers'],
            "Issues": issues,
            "PRs": prs
        })
        
        time.sleep(1)

    # 4. 生成汇总数据
    summary_stats = {
        "TotalRepos": len(repos),
        "TotalForks": sum(repo.get('forks', 0) for repo in repos),
        "TotalStars": sum(repo.get('stars', 0) for repo in repos),
        "TotalWatchers": sum(repo.get('watchers', 0) for repo in repos),
        "TotalIssues": sum(repo.get('Issues', 0) for repo in repo_stats),
        "TotalPRs": sum(repo.get('PRs', 0) for repo in repo_stats),
        "TotalContributors": len(org_contributors),
        "StatTime": current_time,
        "AllContributors": ", ".join(org_contributors) if org_contributors else "无"
    }

    # 5. 保存到Excel
    excel_filename = f"github_stats_{org_name}_{current_time}.xlsx"
    try:
        with pd.ExcelWriter(excel_filename) as writer:
            pd.DataFrame(repo_stats).to_excel(
                writer, 
                sheet_name='Repositories', 
                index=False,
                columns=["RepoName", "Forks", "Stars", "Watchers", "Issues", "PRs"]
            )
            pd.DataFrame([summary_stats]).to_excel(
                writer,
                sheet_name='Summary',
                index=False,
                columns=["TotalRepos", "TotalForks", "TotalStars", "TotalWatchers", 
                         "TotalIssues", "TotalPRs", "TotalContributors", "StatTime", "AllContributors"]
            )
        
        print(f"\n=== 统计完成 ===")
        print(f"结果已保存到: {excel_filename}")
    except Exception as e:
        print(f"保存Excel文件时出错: {str(e)}")
        raise
    
    return repo_stats, summary_stats

if __name__ == "__main__":
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("请设置GITHUB_TOKEN环境变量")
    
    org_name = "ruyisdk"
    try:
        repos, summary = get_org_repos_stats(org_name, token)
        print("\n汇总统计:")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"主程序出错: {str(e)}")
