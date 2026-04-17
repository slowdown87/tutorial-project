#!/usr/bin/env python3
import os
import re

# 定义基本的HTML模板
html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1, h2, h3, h4 {{
            color: #667eea;
        }}
        a {{
            color: #667eea;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            margin-left: 20px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        p {{
            margin-bottom: 15px;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 5px 10px;
            background: #f0f0f0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back-link">返回教程目录</a>
        {content}
    </div>
</body>
</html>'''

# 简单的Markdown到HTML的转换函数
def markdown_to_html(markdown):
    # 标题
    markdown = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^## (.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^### (.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    
    # 列表
    markdown = re.sub(r'^- (.*)$', r'<li>\1</li>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', markdown, flags=re.DOTALL)
    
    # 段落
    markdown = re.sub(r'^(?!<h[1-6]>)(?!<ul>)(?!<li>)(.*)$', r'<p>\1</p>', markdown, flags=re.MULTILINE)
    
    # 链接
    markdown = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', markdown)
    
    return markdown

# 遍历docs目录，转换所有Markdown文件
def convert_all_markdown(docs_dir):
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                html_path = os.path.join(root, file.replace('.md', '.html'))
                
                # 读取Markdown文件
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取标题
                title_match = re.search(r'^# (.*)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else '教程文档'
                
                # 转换为HTML
                html_content = markdown_to_html(content)
                
                # 生成完整的HTML文件
                full_html = html_template.format(title=title, content=html_content)
                
                # 写入HTML文件
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(full_html)
                
                print(f'转换完成: {md_path} -> {html_path}')

# 更新docs/index.html中的链接，将.md改为.html
def update_links():
    index_html_path = os.path.join('docs', 'index.html')
    if os.path.exists(index_html_path):
        with open(index_html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 将.md链接改为.html
        content = re.sub(r'(href="[^"]+)\.md"', r'\1.html"', content)
        
        with open(index_html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print('更新了index.html中的链接')

if __name__ == '__main__':
    docs_dir = 'docs'
    convert_all_markdown(docs_dir)
    update_links()
    print('所有Markdown文件已转换为HTML！')