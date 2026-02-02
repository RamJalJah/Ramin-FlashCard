# 🎴 中文学习卡片 - Chinese Flashcard App

一个功能强大的中文学习卡片网页应用，帮助你高效学习中文词汇。

A powerful web-based Chinese flashcard application to help you learn Chinese vocabulary efficiently.

## ✨ 特性 Features

- 📱 **响应式设计** - 支持手机、平板和电脑 / Responsive design - works on mobile, tablet, and desktop
- 🔄 **双向学习** - 支持英文到中文或中文到英文 / Bidirectional learning - English to Pinyin or Pinyin to English
- 🎯 **智能重复** - 不记得的单词会再次出现 / Smart repetition - words you don't know will appear again
- 📊 **学习统计** - 实时追踪学习进度 / Learning statistics - track your progress in real-time
- ⌨️ **键盘快捷键** - 快速操作 / Keyboard shortcuts for fast operation
- 💾 **本地处理** - 所有数据在浏览器中处理，保护隐私 / Local processing - all data processed in browser, privacy protected
- 🎨 **美观界面** - 现代化设计，学习更愉快 / Beautiful interface - modern design for enjoyable learning

## 🚀 快速开始 Quick Start

### 在线使用 Online Usage

1. 访问 / Visit: [GitHub Pages链接]
2. 上传你的 `Chinese.xlsx` 文件 / Upload your `Chinese.xlsx` file
3. 选择学习模式 / Choose learning mode
4. 开始学习！/ Start learning!

### 本地使用 Local Usage

1. 下载或克隆此仓库 / Download or clone this repository:
   ```bash
   git clone https://github.com/yourusername/chinese-flashcard-app.git
   ```

2. 在浏览器中打开 `index.html` 文件 / Open `index.html` in your browser

3. 上传你的 `Chinese.xlsx` 文件 / Upload your `Chinese.xlsx` file

## 📝 Excel 文件格式 Excel File Format

你的 `Chinese.xlsx` 文件应该有以下格式：

Your `Chinese.xlsx` file should have the following format:

| Column A (拼音 Pinyin) | Column B (英文 English) |
|------------------------|-------------------------|
| nǐ hǎo | hello |
| xiè xie | thank you |
| zài jiàn | goodbye |

- **第一列** / **Column 1**: 拼音 (Pinyin)
- **第二列** / **Column 2**: 英文翻译 (English translation)
- 第一行可以是标题行，会自动跳过 / First row can be headers, will be auto-skipped

## 🎮 使用方法 How to Use

### 1. 上传文件 Upload File
- 点击上传区域选择文件 / Click upload area to select file
- 或拖放文件到上传区域 / Or drag and drop file to upload area

### 2. 选择模式 Choose Mode
- **英文 ➡️ 中文** / **English ➡️ Pinyin**: 显示英文，猜拼音 / Show English, guess Pinyin
- **中文 ➡️ 英文** / **Pinyin ➡️ English**: 显示拼音，猜英文 / Show Pinyin, guess English

### 3. 学习 Learn
- 点击卡片翻转查看答案 / Click card to flip and see answer
- 选择 "再来一次" 如果不记得 / Choose "Again" if you don't remember
- 选择 "记住了" 如果已掌握 / Choose "Got it!" if you've mastered it

### 4. 键盘快捷键 Keyboard Shortcuts
- `空格键 Space` - 翻转卡片 / Flip card
- `左箭头 ← 或 1` - 再来一次 / Again
- `右箭头 → 或 2` - 记住了 / Got it!

## 🎯 学习算法 Learning Algorithm

- 选择"再来一次"的单词会在几张卡片后重新出现 / Words marked "Again" will reappear after a few cards
- 选择"记住了"的单词会从队列中移除 / Words marked "Got it!" will be removed from the queue
- 所有单词学完后会显示祝贺信息 / Completion message shown when all words are learned

## 🛠️ 技术栈 Tech Stack

- **纯HTML/CSS/JavaScript** - 无需安装，直接使用 / Pure HTML/CSS/JavaScript - no installation needed
- **SheetJS (xlsx.js)** - Excel文件解析 / Excel file parsing
- **响应式设计** - 适配所有设备 / Responsive design - works on all devices

## 📱 兼容性 Compatibility

- ✅ Chrome, Firefox, Safari, Edge (最新版本 latest versions)
- ✅ iOS Safari, Chrome Mobile
- ✅ 支持 .xlsx 和 .xls 文件格式 / Supports .xlsx and .xls file formats

## 🤝 贡献 Contributing

欢迎提交 Issue 和 Pull Request！

Issues and Pull Requests are welcome!

## 📄 许可证 License

MIT License - 自由使用和修改 / Free to use and modify

## 💡 提示 Tips

- 建议每次学习20-30个单词 / Recommend learning 20-30 words per session
- 定期复习以加强记忆 / Review regularly to strengthen memory
- 可以创建多个Excel文件按主题分类学习 / Create multiple Excel files to learn by topic

## 🌟 截图 Screenshots

(在这里添加应用截图 / Add app screenshots here)

---

**开始你的中文学习之旅吧！ Start your Chinese learning journey today! 🚀**
