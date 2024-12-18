const vscode = require('vscode');
const path = require('path');
const { spawn } = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('compress-backup.compressFolder', async (uri) => {
        try {
            // 如果没有选中文件夹，提示用户选择
            if (!uri) {
                const folderUri = await vscode.window.showOpenDialog({
                    canSelectFiles: false,
                    canSelectFolders: true,
                    canSelectMany: false,
                    title: '选择要压缩的文件夹'
                });
                
                if (!folderUri || folderUri.length === 0) {
                    return;
                }
                uri = folderUri[0];
            }

            // 直接在同目录下保存
            const targetPath = path.dirname(uri.fsPath);

            // 获取Python脚本的路径
            const pythonScriptPath = path.join(__dirname, 'auto_compress.py');
            
            // 显示开始压缩的提示
            vscode.window.showInformationMessage('正在压缩...');
            
            // 运行Python脚本
            const pythonProcess = spawn('python', [
                pythonScriptPath,
                uri.fsPath,
                targetPath,
                path.basename(uri.fsPath)
            ], { encoding: 'utf8' });

            // 处理Python脚本的输出
            pythonProcess.stdout.on('data', (data) => {
                if (data.includes('完成：')) {
                    vscode.window.showInformationMessage('压缩完成');
                }
            });

            pythonProcess.stderr.on('data', (data) => {
                vscode.window.showErrorMessage('压缩失败');
            });

            pythonProcess.on('close', (code) => {
                if (code !== 0) {
                    vscode.window.showErrorMessage('压缩失败');
                }
            });

        } catch (error) {
            vscode.window.showErrorMessage('压缩出错');
        }
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
} 