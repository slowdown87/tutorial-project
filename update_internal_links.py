#!/usr/bin/env python3
import os
import re

# 遍历docs目录，更新所有Markdown和HTML文件中的内部链接
def update_internal_links(docs_dir):
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(('.md', '.html')):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 更新内部链接，将.md改为.html
                # 匹配相对路径的链接，如 [text](section02.md) 或 [text](./section02.md)
                updated_content = re.sub(r'(\[.+?\]\()([^:]+?)\.md(\))', r'\1\2.html\3', content)
                
                # 如果内容有变化，写入更新后的内容
                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f'更新了文件中的链接: {file_path}')

if __name__ == '__main__':
    docs_dir = 'docs'
    update_internal_links(docs_dir)
    print('所有内部链接已更新！')