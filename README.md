<<<<<<< HEAD
# compress-backup
VSCode 一键压缩备份扩展
=======
 # VSCode 一键压缩备份

一个简单的 VSCode 扩展，可以通过右键菜单快速将文件夹压缩为 7z 格式，并自动添加时间戳。

## 功能特点

- 在资源管理器中右键点击文件夹即可压缩
- 自动使用"文件夹名_年月日_时分.7z"格式命名
- 压缩文件保存在源文件夹同级目录
- 使用 7z 格式，提供高压缩率

## 安装要求

1. 安装 [Visual Studio Code](https://code.visualstudio.com/)
2. 安装 [Python](https://www.python.org/downloads/)
3. 安装 [7-Zip](https://www.7-zip.org/)
   - Windows: 下载并安装 7-Zip
   - Linux: `sudo apt-get install p7zip-full`
   - Mac: `brew install p7zip`

## 安装扩展

### 方法一：从 VSIX 文件安装

1. 下载 [compress-backup-0.0.1.vsix](https://github.com/实际用户名/compress-backup/releases)
2. 在 VSCode 中按 `Ctrl+Shift+P`
3. 输入 "Install from VSIX"
4. 选择下载的 .vsix 文件

### 方法二：从源码安装 
+
+ ```bash
+ # 克隆仓库
+ git clone https://github.com/实际用户名/compress-backup.git
+ 
+ # 进入目录
+ cd compress-backup
+ 
+ # 安装依赖
+ npm install
+ 
+ # 打包扩展
+ npm install -g vsce
+ vsce package
+ 
+ # 然后按方法一安装生成的 .vsix 文件
+ ```
+ 
+ ## 使用方法
+ 
+ 1. 在 VSCode 的资源管理器中找到要压缩的文件夹
+ 2. 右键点击文件夹
+ 3. 选择 "压缩备份" 选项
+ 4. 等待提示 "压缩完成"
+ 
+ 压缩文件将保存在源文件夹的同级目录下，文件名格式为：`文件夹名_YYYYMMDD_HHMM.7z`
+ 
+ ## 项目结构
+ 
+ ```
+ compress-backup/
+ ├── package.json          # 扩展配置文件
+ ├── extension.js          # 扩展主程序
+ └── auto_compress.py      # Python压缩脚本
+ ```
+ 
+ ## 源码说明
+ 
+ ### package.json
+ ```json
+ {
+     "name": "compress-backup",
+     "displayName": "Compress Backup",
+     "description": "一键压缩备份文件夹",
+     "version": "0.0.1",
+     "publisher": "yourname",
+     "engines": {
+         "vscode": "^1.95.0"
+     }
+ }
+ ```
+ 
+ ### extension.js
+ ```javascript
+ // 主要功能：
+ // 1. 注册右键菜单命令
+ // 2. 调用Python脚本进行压缩
+ // 3. 处理压缩结果并显示提示
+ ```
+ 
+ ### auto_compress.py
+ ```python
+ # 主要功能：
+ # 1. 检查7z是否已安装
+ # 2. 生成带时间戳的文件名
+ # 3. 调用7z命令进行压缩
+ ```
+ 
+ ## 开发说明
+ 
+ 1. 克隆仓库后，确保已安装所需软件：
+    - VSCode
+    - Node.js
+    - Python
+    - 7-Zip
+ 
+ 2. 安装开发依赖：
+    ```bash
+    npm install
+    npm install -g vsce
+    ```
+ 
+ 3. 调试：
+    - 在 VSCode 中按 F5 启动调试
+    - 在新窗口中测试功能
+ 
+ ## 问题反馈
+ 
+ 如果遇到问题或有建议，请在 [GitHub Issues](https://github.com/实际用户名/compress-backup/issues) 提出。
+ 
+ ## 许可证
+ 
+ [MIT](LICENSE)
+ 
+ ## 更新日志
+ 
+ ### v0.0.1 (2024-03-18)
+ - 初始版本
+ - 实现基本压缩功能
+ - 添加右键菜单支持
>>>>>>> f70c1c0 (Initial commit: VSCode compress backup extension)
