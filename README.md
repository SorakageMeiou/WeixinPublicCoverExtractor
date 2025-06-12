# 🌟 微信公众号封面图提取工具
> 一键提取微信公众号文章的封面图链接，并自动下载保存到本地。适用于快速获取公众号推送文章的高质量封面图片
---

## 📦 简介
本工具是一个基于 Python 编写的命令行程序，用于从微信公众号文章页面中提取封面图（`msg_cdn_url` 或 `og:image`）并将其下载保存为 `.jpg` 文件。同时支持复制图片链接至剪贴板，方便快捷使用。
适用于：
- 运营人员、内容创作者
- 需要批量整理公众号封面图素材
- 学习网络爬虫与正则表达式应用
---

## 🔍 功能亮点
- 自动识别微信公众号文章页封面图链接  
- 支持两种提取方式（JS变量匹配 + Open Graph 标签）  
- 自动命名保存文件（时间戳命名，避免重复）  
- 复制图片链接至剪贴板（便于粘贴使用）  
- 可打包为 `.exe` 程序，无 Python 环境也可运行  
---

## 🧰 使用说明

### ✅ 安装依赖
```bash
pip install requests pyperclip
```
### ✅ 运行脚本
```bash
python extract_wechat_cover.py
```
然后输入微信公众号文章链接（如：“https://mp.weixin.qq.com/s/xxxxxx”），程序会自动提取封面图并下载保存。

---

## ⚙️ EXE（已在Release中上传）
[最新版本exe文件](https://github.com/SorakageMeiou/WeixinPublicCoverExtractor/releases/tag/WeixinWorks)

---

## 📝 协议 & 贡献

- 本项目采用 MIT 开源协议
- 欢迎提交 Issue 和 Pull Request，共同优化功能或修复问题！

---

## 👤 作者信息

GitHub: [SorakageMeiou]  
邮箱：[SorakageMo@qq.com]  
B站页：「[空影メイオウ](https://space.bilibili.com/366462635)」
