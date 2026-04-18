# 3.1 项目初始化步骤

## 目标

在本节中，你将：
- 学习如何在线完成项目初始化（推荐，适合零基础用户）
- 了解如何在本地完成项目初始化（可选）
- 了解项目的基本结构
- 掌握Git版本控制的基本操作
- 为后续的网页制作做好准备

---

## 为什么需要项目初始化？

项目初始化是任何开发项目的第一步，它为我们的工作奠定基础：

### 项目初始化的重要性：
- 📁 建立清晰的目录结构
- 🔄 启用版本控制，便于追踪变更
- 📋 为后续的开发工作做好准备
- 🎯 确保项目的可维护性

---

## 在线完成项目初始化（推荐，适合零基础用户）

对于零基础用户，我们推荐使用在线方式完成项目初始化，这样不需要安装任何软件，直接在浏览器中操作即可。

### 操作步骤：

1. **打开Solo Trae Web Code**
   - 访问 [https://solo.trae.cn/](https://solo.trae.cn/)
   - 登录你的账号

2. **创建新项目**
   - 在Solo Trae Web Code界面中，点击「新建项目」按钮
   - 输入项目名称，例如 `tutorial-project`
   - 选择「空白项目」模板
   - 点击「创建」按钮

3. **创建项目结构**
   - 在左侧文件管理器中，点击「新建文件夹」按钮
   - 创建以下文件夹：
     - `project/` - 存放实际的网页项目代码
     - `docs/` - 存放教程文档
     - `docs/images/` - 存放教程截图

4. **创建基本文件**
   - 在 `project` 文件夹中，创建 `index.html` 文件：
     ```html
     <!DOCTYPE html>
     <html lang="zh-CN">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>我的第一个网页</title>
         <link rel="stylesheet" href="css/style.css">
     </head>
     <body>
         <h1>欢迎来到我的网页！</h1>
         <p>这是一个使用Solo Trae Web Code制作的网页。</p>
         <script src="js/script.js"></script>
     </body>
     </html>
     ```

   - 在 `project` 文件夹中创建 `css` 子文件夹，然后创建 `style.css` 文件：
     ```css
     body {
         font-family: Arial, sans-serif;
         margin: 0;
         padding: 20px;
         background-color: #f0f0f0;
     }
     
     h1 {
         color: #333;
     }
     
     p {
         color: #666;
     }
     ```

   - 在 `project` 文件夹中创建 `js` 子文件夹，然后创建 `script.js` 文件：
     ```javascript
     console.log("Hello, Solo Trae!");
     
     // 简单的交互功能
     document.addEventListener("DOMContentLoaded", function() {
         console.log("网页加载完成！");
     });
     ```

5. **创建README.md文件**
   - 在根目录创建 `README.md` 文件：
     ```markdown
     # 教程项目
     
     这是一个关于如何使用Solo Trae Web Code制作网页并发布的教程项目。
     ```

6. **创建.gitignore文件**
   - 在根目录创建 `.gitignore` 文件：
     ```
     # 忽略文件
     node_modules/
     .DS_Store
     *.log
     ```

7. **初始化Git仓库**
   - 在Solo Trae Web Code的终端中执行：
     ```bash
     git init
     git add .
     git commit -m "初始化项目：创建基本目录结构和文件"
     ```

8. **验证项目结构**
   你的项目结构应该如下所示：
   ```
   tutorial-project/
   ├── project/
   │   ├── index.html
   │   ├── css/
   │   │   └── style.css
   │   └── js/
   │       └── script.js
   ├── docs/
   │   └── images/
   ├── README.md
   └── .gitignore
   ```

---

## 本地完成项目初始化（可选）

如果你希望在本地完成项目初始化，可以按照以下步骤操作。

### 步骤1：创建项目目录结构

让我们开始创建项目的基本目录结构。

### 操作步骤：

1. **创建主项目目录**
   - 在你的电脑上选择一个合适的位置
   - 创建一个名为 `tutorial-project` 的目录

2. **创建子目录**
   在 `tutorial-project` 目录内，创建以下子目录：
   - `project/` - 存放实际的网页项目代码
   - `docs/` - 存放教程文档
   - `docs/images/` - 存放教程截图

3. **验证目录结构**
   你的目录结构应该如下所示：
   ```
   tutorial-project/
   ├── project/
   ├── docs/
   │   └── images/
   └── README.md
   ```

---

## 步骤2：初始化Git版本控制

Git是一个强大的版本控制工具，它可以帮助我们追踪代码的变更。

### 操作步骤：

1. **打开终端**
   - Windows：按 `Win+R`，输入 `cmd`，按回车
   - Mac：按 `Cmd+Space`，输入 `Terminal`，按回车
   - Linux：使用快捷键 `Ctrl+Alt+T`

2. **进入项目目录**
   ```bash
   cd path/to/tutorial-project
   ```
   （将 `path/to/` 替换为实际的路径）

3. **初始化Git仓库**
   ```bash
   git init
   ```
   你会看到类似的输出：
   ```
   Initialized empty Git repository in /path/to/tutorial-project/.git/
   ```

4. **创建.gitignore文件**
   这个文件用于告诉Git哪些文件不需要追踪：
   ```bash
   echo "# 忽略文件\nnode_modules/\n.DS_Store\n*.log\n" > .gitignore
   ```

5. **创建README.md文件**
   ```bash
   echo "# 教程项目\n\n这是一个关于如何使用Solo Trae Web Code制作网页并发布的教程项目。" > README.md
   ```

---

## 步骤3：创建基本的项目文件

现在让我们创建一些基本的项目文件。

### 操作步骤：

1. **创建HTML文件**
   在 `project` 目录中创建 `index.html` 文件：
   ```bash
   mkdir -p project
   echo '<!DOCTYPE html>
   <html lang="zh-CN">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>我的第一个网页</title>
   </head>
   <body>
       <h1>欢迎来到我的网页！</h1>
       <p>这是一个使用Solo Trae Web Code制作的网页。</p>
   </body>
   </html>' > project/index.html
   ```

2. **创建CSS目录和文件**
   ```bash
   mkdir -p project/css
   echo 'body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 20px;
       background-color: #f0f0f0;
   }
   
   h1 {
       color: #333;
   }
   
   p {
       color: #666;
   }' > project/css/style.css
   ```

3. **创建JavaScript目录和文件**
   ```bash
   mkdir -p project/js
   echo 'console.log("Hello, Solo Trae!");
   
   // 简单的交互功能
   document.addEventListener("DOMContentLoaded", function() {
       console.log("网页加载完成！");
   });' > project/js/script.js
   ```

---

## 步骤4：更新HTML文件，引入CSS和JavaScript

让我们更新 `index.html` 文件，引入我们刚刚创建的CSS和JavaScript文件。

### 操作步骤：

1. **编辑index.html文件**
   使用文本编辑器打开 `project/index.html` 文件，修改为：
   ```html
   <!DOCTYPE html>
   <html lang="zh-CN">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>我的第一个网页</title>
       <link rel="stylesheet" href="css/style.css">
   </head>
   <body>
       <h1>欢迎来到我的网页！</h1>
       <p>这是一个使用Solo Trae Web Code制作的网页。</p>
       <script src="js/script.js"></script>
   </body>
   </html>
   ```

---

## 步骤5：验证项目结构

让我们检查一下我们创建的项目结构是否正确。

### 操作步骤：

1. **查看目录结构**
   在终端中执行：
   ```bash
   ls -la tutorial-project/
   ```

2. **查看文件内容**
   确认所有文件都已创建并包含正确的内容。

---

## 步骤6：提交初始代码到Git

现在让我们将初始代码提交到Git仓库。

### 操作步骤：

1. **添加文件到暂存区**
   ```bash
   git add .
   ```

2. **提交更改**
   ```bash
   git commit -m "初始化项目：创建基本目录结构和文件"
   ```

3. **查看提交历史**
   ```bash
   git log
   ```
   你会看到类似的输出：
   ```
   commit 1234567890abcdef1234567890abcdef12345678
   Author: Your Name <your.email@example.com>
   Date:   Today's date

       初始化项目：创建基本目录结构和文件
   ```

---

## 项目结构说明

现在我们已经创建了一个基本的项目结构，让我们来了解一下每个部分的作用：

| 目录/文件 | 作用 |
|-----------|------|
| `project/` | 存放实际的网页项目代码 |
| `project/index.html` | 网页的主文件 |
| `project/css/` | 存放CSS样式文件 |
| `project/js/` | 存放JavaScript脚本文件 |
| `docs/` | 存放教程文档 |
| `docs/images/` | 存放教程截图 |
| `.git/` | Git版本控制目录 |
| `.gitignore` | Git忽略文件配置 |
| `README.md` | 项目说明文件 |

---

## 常见问题与解答

### Q: 我没有Git怎么办？
**A:** 如果你使用在线方式完成项目初始化，Solo Trae Web Code已经内置了Git功能，不需要单独安装。如果你选择本地方式，则需要从 [Git官网](https://git-scm.com/downloads) 下载并安装Git。

### Q: 我不会使用终端命令怎么办？
**A:** 推荐使用在线方式完成项目初始化，Solo Trae Web Code提供了图形化界面，不需要使用终端命令。如果你选择本地方式，可以使用文件管理器手动创建目录和文件，然后使用图形化Git客户端（如GitHub Desktop）来管理版本控制。

### Q: 项目结构可以根据需要调整吗？
**A:** 当然可以！这只是一个基本的结构，你可以根据项目的具体需求进行调整。

### Q: 我需要创建其他文件吗？
**A:** 目前的文件已经足够开始基本的网页制作。随着项目的进展，你可以根据需要添加更多文件。

### Q: 在线方式和本地方式有什么区别？
**A:** 
- **在线方式**：不需要安装任何软件，直接在浏览器中操作，适合零基础用户
- **本地方式**：需要在本地安装Git和其他工具，适合有一定技术基础的用户

### Q: 我可以在在线方式和本地方式之间切换吗？
**A:** 可以！你可以先使用在线方式完成初始化，然后将项目下载到本地进行进一步开发，或者反之。

### Q: 在线方式的项目数据安全吗？
**A:** Solo Trae Web Code会保存你的项目数据，你也可以定期将项目下载到本地进行备份。

### Q: 我需要网络连接才能使用在线方式吗？
**A:** 是的，在线方式需要网络连接。如果你需要离线工作，可以选择本地方式。

---

## 练习时间！

### 在线方式练习（推荐）

#### 练习1：在线创建项目
1. 打开 [https://solo.trae.cn/](https://solo.trae.cn/)
2. 登录你的账号
3. 创建一个名为 `tutorial-project` 的新项目

#### 练习2：创建项目结构
1. 在Solo Trae Web Code中创建以下文件夹：
   - `project/`
   - `docs/`
   - `docs/images/`
2. 验证目录结构是否正确

#### 练习3：创建基本文件
1. 在 `project` 文件夹中创建 `index.html` 文件
2. 在 `project/css` 文件夹中创建 `style.css` 文件
3. 在 `project/js` 文件夹中创建 `script.js` 文件
4. 在根目录创建 `README.md` 和 `.gitignore` 文件

#### 练习4：初始化Git仓库
1. 在Solo Trae Web Code的终端中执行：
   ```bash
   git init
   git add .
   git commit -m "初始化项目：创建基本目录结构和文件"
   ```
2. 查看提交历史

### 本地方式练习（可选）

#### 练习1：创建项目目录结构
1. 按照步骤创建 `tutorial-project` 目录及其子目录
2. 验证目录结构是否正确

#### 练习2：初始化Git仓库
1. 在项目目录中初始化Git仓库
2. 创建 `.gitignore` 文件
3. 创建 `README.md` 文件

#### 练习3：创建基本文件
1. 创建 `index.html`、`style.css` 和 `script.js` 文件
2. 更新 `index.html` 文件，引入CSS和JavaScript

#### 练习4：提交代码
1. 将所有文件添加到Git
2. 提交初始代码
3. 查看提交历史

---

## 总结

在本节中，你学会了：

✅ 如何在线完成项目初始化（推荐，适合零基础用户）
✅ 如何在本地完成项目初始化（可选）
✅ 如何创建项目的基本目录结构
✅ 如何初始化Git版本控制
✅ 如何创建基本的HTML、CSS和JavaScript文件
✅ 如何将初始代码提交到Git仓库
✅ 了解了项目结构的各个部分及其作用

**现在你的项目已经初始化完成，为后续的网页制作做好了准备！**

---

**下一步**：让我们进入[3.2 项目配置与设置](section02-project-config.html)，进一步完善我们的项目！