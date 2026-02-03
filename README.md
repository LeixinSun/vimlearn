# VimLearn

一个交互式 Vim 学习工具。不同于传统的文档教程，VimLearn 让你在**真实的 Vim 编辑器**中完成练习，边学边练，即时验证。

## 为什么选择 VimLearn？

- **真实练习** - 每个练习都在真正的 Vim 中完成，不是模拟器
- **即时反馈** - 完成后自动验证结果，对比你的输出和期望输出
- **循序渐进** - 从 hjkl 到宏录制，10 个模块 27 节课由浅入深
- **理解原理** - 每个命令都解释"为什么这样设计"
- **进度保存** - 自动保存学习进度，随时继续

## 课程内容

```
模块 1: 基础移动      hjkl、w/b/e、0/$、数字前缀
模块 2: 编辑操作      i/a/o、d/x、c
模块 3: 复制粘贴      y/p、u/Ctrl+r
模块 4: 文本对象      iw/aw、ci"/da(
模块 5: 可视模式      v/V/Ctrl-v
模块 6: 搜索替换      /、f/t、:s
模块 7: 跳转与窗口    gg/G、标记、分割窗口
模块 8: 实用配置      行号、搜索、缩进
模块 9: 宏与重复      点命令、宏录制
模块 10: 插件进阶     vim-plug、常用插件、vimrc
```

## 安装

需要：Python 3.11+、[uv](https://github.com/astral-sh/uv)、Vim

```bash
git clone https://github.com/yourusername/vimlearn.git
cd vimlearn
uv sync
```

## 使用

```bash
# 开始学习
uv run vimlearn start

# 指定用户
uv run vimlearn start -u <用户名>

# 从指定课程开始（如从 3.1 开始）
uv run vimlearn start -l 3.1

# 查看所有课程
uv run vimlearn lessons

# 查看进度
uv run vimlearn progress <用户名>

# 重置进度
uv run vimlearn reset <用户名>
```

## 学习流程

```
1. 阅读讲解，理解命令用法
2. 查看练习：初始内容 → 目标内容
3. 按 1 启动 Vim
4. 在 Vim 中完成编辑，:wq 保存退出
5. 自动验证结果
```

## 操作说明

**练习前：**
| 按键 | 操作 |
|------|------|
| 1 | 开始练习 |
| 2 | 显示提示 |
| 3 | 查看设计原因 |
| 4 | 跳过 |
| 0 | 退出 |

**练习失败后：**
| 按键 | 操作 |
|------|------|
| 1 | 重试 |
| 2 | 显示提示 |
| 4 | 跳过 |
| 5 | 强制通过 |
| 0 | 退出 |

## License

MIT
