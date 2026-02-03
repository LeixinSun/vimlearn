"""Lesson data for VimLearn."""

from typing import Optional
from .lesson import Lesson, Exercise, Module


# Module 1: 基础移动
MODULE_1_LESSONS = [
    Lesson(
        id="1.1",
        title="hjkl 基础移动",
        module="基础移动",
        module_num=1,
        description="学习 Vim 最基本的光标移动方式",
        explanation="""
在 Vim 中，我们使用 h、j、k、l 四个键来移动光标：

  h - 左移一个字符
  j - 下移一行
  k - 上移一行
  l - 右移一个字符

这四个键位于键盘主行，让你的手指无需离开打字位置就能移动光标。

记忆技巧：
- h 在最左边，所以向左移动
- l 在最右边，所以向右移动
- j 像一个向下的钩子，所以向下移动
- k 像一个向上的指针，所以向上移动
""",
        why="""
为什么不用方向键？

1. 效率：hjkl 键在主键盘区，手指不需要移动到方向键区域
2. 速度：减少手指移动距离，提高编辑速度
3. 组合：可以与数字组合，如 5j 向下移动5行
4. 历史：Vim 的前身 vi 诞生时，很多键盘没有方向键
""",
        exercises=[
            Exercise(
                instruction="使用 j 键将光标移动到最后一行，然后保存退出 (:wq)",
                initial="第一行\n第二行\n第三行\n目标行",
                expected="第一行\n第二行\n第三行\n目标行",
                hint="按 j 三次到达最后一行，然后输入 :wq 保存退出",
                commands_to_learn=["j", ":wq"],
            ),
            Exercise(
                instruction="使用 l 键将光标移动到行尾的 X 处，将 X 改为 Y (使用 r 命令替换字符)",
                initial="找到这个X",
                expected="找到这个Y",
                hint="按 l 移动到 X，然后按 r 再按 Y 替换字符",
                commands_to_learn=["l", "r"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="1.2",
        title="单词移动 w/b/e",
        module="基础移动",
        module_num=1,
        description="学习按单词移动光标",
        explanation="""
按字符移动太慢了，Vim 提供了按单词移动的方式：

  w - 移动到下一个单词的开头 (word)
  b - 移动到上一个单词的开头 (back)
  e - 移动到当前/下一个单词的结尾 (end)

大写版本 W、B、E 以空格为分隔符，忽略标点：
  W - 移动到下一个空格分隔的单词
  B - 移动到上一个空格分隔的单词
  E - 移动到当前/下一个空格分隔单词的结尾
""",
        why="""
为什么区分 w 和 W？

在编程中，我们经常遇到 snake_case 或 camelCase 这样的标识符。
- w 会把 hello_world 当作两个单词
- W 会把 hello_world 当作一个单词

这让你可以根据需要选择合适的移动粒度。
""",
        exercises=[
            Exercise(
                instruction="使用 w 移动到 'world' 单词，将其改为 'vim' (使用 cw 命令)",
                initial="hello world",
                expected="hello vim",
                hint="按 w 移动到 world，然后按 cw 输入 vim，按 Esc 退出插入模式",
                commands_to_learn=["w", "cw"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 2w 一次跳过两个单词，到达 'third' 并删除它",
                initial="first second third",
                expected="first second",
                hint="按 2w 跳到 third，按 dw 删除",
                commands_to_learn=["2w", "dw"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="1.3",
        title="行内移动 0/$/^",
        module="基础移动",
        module_num=1,
        description="学习在行内快速移动",
        explanation="""
在一行内快速移动：

  0 - 移动到行首（第0列）
  $ - 移动到行尾
  ^ - 移动到行首第一个非空白字符

这些命令让你能快速到达行的关键位置。
""",
        why="""
为什么用这些符号？

- 0 表示第0列，即行的最开始
- $ 在正则表达式中表示行尾，Vim 沿用了这个约定
- ^ 在正则表达式中表示行首，这里表示第一个非空字符
""",
        exercises=[
            Exercise(
                instruction="使用 $ 移动到行尾，添加感叹号",
                initial="Hello World",
                expected="Hello World!",
                hint="按 $ 到行尾，按 a 追加，输入 !，按 Esc",
                commands_to_learn=["$", "a"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 0 移动到行首，删除前导空格（使用 dw）",
                initial="    Hello",
                expected="Hello",
                hint="按 0 到行首，按 dw 删除空格",
                commands_to_learn=["0", "dw"],
                cursor_position=4,
            ),
        ],
    ),
    Lesson(
        id="1.4",
        title="数字前缀",
        module="基础移动",
        module_num=1,
        description="学习使用数字倍增命令",
        explanation="""
几乎所有 Vim 命令都可以加数字前缀来重复执行：

移动命令：
  5j - 向下移动 5 行
  3w - 向前移动 3 个单词
  10l - 向右移动 10 个字符

编辑命令：
  3dd - 删除 3 行
  2dw - 删除 2 个单词
  5x - 删除 5 个字符

这是 Vim 效率的重要来源！
""",
        why="""
为什么数字前缀这么重要？

配合相对行号使用效果最佳：
- 看到目标在第 8 行，当前在第 3 行
- 不用算 8-3=5，直接看相对行号显示 5
- 按 5j 直接到达

数字前缀让你用最少的按键完成操作。
""",
        exercises=[
            Exercise(
                instruction="使用 3dd 一次删除三行",
                initial="删除1\n删除2\n删除3\n保留",
                expected="保留",
                hint="按 3dd 删除三行",
                commands_to_learn=["3dd"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 4x 删除前四个字符",
                initial="abcdefgh",
                expected="efgh",
                hint="按 4x 删除四个字符",
                commands_to_learn=["4x"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 2: 编辑操作
MODULE_2_LESSONS = [
    Lesson(
        id="2.1",
        title="插入模式 i/a/o",
        module="编辑操作",
        module_num=2,
        description="学习进入插入模式的多种方式",
        explanation="""
Vim 有多种方式进入插入模式：

  i - 在光标前插入 (insert)
  a - 在光标后追加 (append)
  I - 在行首插入
  A - 在行尾追加
  o - 在下方新建一行并插入
  O - 在上方新建一行并插入

按 Esc 或 Ctrl+[ 退出插入模式回到普通模式。
""",
        why="""
为什么有这么多进入插入模式的方式？

每种方式都针对特定场景优化：
- i/a 用于精确位置插入
- I/A 用于行首/行尾快速编辑
- o/O 用于快速新建行

这避免了"移动光标 + 进入插入模式"的组合操作。
""",
        exercises=[
            Exercise(
                instruction="使用 A 在行尾添加 ' World'",
                initial="Hello",
                expected="Hello World",
                hint="按 A 到行尾进入插入模式，输入 ' World'，按 Esc",
                commands_to_learn=["A"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 o 在下方新建一行，输入 '第二行'",
                initial="第一行",
                expected="第一行\n第二行",
                hint="按 o 在下方新建行，输入 '第二行'，按 Esc",
                commands_to_learn=["o"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="2.2",
        title="删除操作 d/x",
        module="编辑操作",
        module_num=2,
        description="学习删除文本的各种方式",
        explanation="""
删除命令：

  x - 删除光标下的字符
  X - 删除光标前的字符
  dd - 删除整行
  dw - 删除到下一个单词开头
  de - 删除到单词结尾
  d$ 或 D - 删除到行尾
  d0 - 删除到行首

d 命令可以与移动命令组合：d + 移动 = 删除到移动目标位置
""",
        why="""
为什么 d 要和移动命令组合？

这是 Vim 的"动词 + 名词"语法：
- d 是动词（删除）
- w、e、$ 等是名词（移动范围）

这种组合方式让你只需学习少量命令，就能组合出大量操作。
""",
        exercises=[
            Exercise(
                instruction="使用 dd 删除第二行",
                initial="保留这行\n删除这行\n保留这行",
                expected="保留这行\n保留这行",
                hint="按 j 移动到第二行，按 dd 删除整行",
                commands_to_learn=["dd"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 dw 删除第一个单词",
                initial="delete this word",
                expected="this word",
                hint="按 dw 删除第一个单词（包括空格）",
                commands_to_learn=["dw"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="2.3",
        title="修改操作 c",
        module="编辑操作",
        module_num=2,
        description="学习修改（删除并进入插入模式）",
        explanation="""
c 命令 = 删除 + 进入插入模式：

  cw - 修改单词（删除到单词尾并进入插入模式）
  cc 或 S - 修改整行
  c$ 或 C - 修改到行尾
  ci" - 修改引号内的内容
  ci( - 修改括号内的内容

c 命令的语法和 d 命令相同，但会进入插入模式。
""",
        why="""
为什么需要 c 命令？

c 命令是 d + i 的快捷方式。比如：
- dw + i 需要两步
- cw 只需一步

在实际编辑中，"删除后立即输入新内容"是非常常见的操作。
""",
        exercises=[
            Exercise(
                instruction="使用 cw 将 'old' 改为 'new'",
                initial="old text",
                expected="new text",
                hint="按 cw 删除 'old' 并进入插入模式，输入 'new'，按 Esc",
                commands_to_learn=["cw"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 cc 将整行替换为 '新的一行'",
                initial="旧的内容",
                expected="新的一行",
                hint="按 cc 删除整行并进入插入模式，输入 '新的一行'，按 Esc",
                commands_to_learn=["cc"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 3: 复制粘贴与撤销
MODULE_3_LESSONS = [
    Lesson(
        id="3.1",
        title="复制粘贴 y/p",
        module="复制粘贴与撤销",
        module_num=3,
        description="学习复制和粘贴操作",
        explanation="""
复制（yank）和粘贴（put）：

  yy - 复制整行
  yw - 复制单词
  y$ - 复制到行尾
  p - 在光标后粘贴
  P - 在光标前粘贴

y 命令的语法和 d、c 相同，可以与移动命令组合。

注意：Vim 中删除的内容也会被复制到寄存器，所以 dd 后可以用 p 粘贴。
""",
        why="""
为什么叫 yank 而不是 copy？

在 Vim 的历史中，y 代表 yank（猛拉），这个术语来自更早的编辑器。
虽然不太直观，但 y 键位置好，而且 c 已经被 change 占用了。
""",
        exercises=[
            Exercise(
                instruction="使用 yy 复制第一行，然后用 p 粘贴到下方",
                initial="复制我",
                expected="复制我\n复制我",
                hint="按 yy 复制当前行，按 p 在下方粘贴",
                commands_to_learn=["yy", "p"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 dd 删除第一行，然后用 p 粘贴到第二行下方（交换两行）",
                initial="第二行\n第一行",
                expected="第一行\n第二行",
                hint="按 dd 删除第一行（会自动复制），按 p 粘贴到当前行下方",
                commands_to_learn=["dd", "p"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="3.2",
        title="撤销与重做 u/Ctrl+r",
        module="复制粘贴与撤销",
        module_num=3,
        description="学习撤销和重做操作",
        explanation="""
撤销和重做：

  u - 撤销上一次操作 (undo)
  Ctrl+r - 重做被撤销的操作 (redo)
  U - 撤销当前行的所有修改

Vim 的撤销是基于操作的，每次从普通模式进入插入模式到退出算一次操作。
""",
        why="""
为什么 Vim 的撤销这么强大？

Vim 支持无限撤销，而且有撤销树（undo tree）功能。
即使你撤销后又做了新修改，之前的历史也不会丢失。
可以使用 :earlier 和 :later 命令按时间回溯。
""",
        exercises=[
            Exercise(
                instruction="先用 dd 删除第一行，再用 u 撤销，最后删除第二行",
                initial="保留这行\n删除这行",
                expected="保留这行",
                hint="按 dd 删除，按 u 撤销，按 j 到第二行，按 dd 删除",
                commands_to_learn=["u", "dd"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 4: 文本对象
MODULE_4_LESSONS = [
    Lesson(
        id="4.1",
        title="内部文本对象 i",
        module="文本对象",
        module_num=4,
        description="学习使用内部文本对象精确选择",
        explanation="""
文本对象让你可以操作结构化的文本块。内部文本对象 (i = inner)：

  iw - 内部单词（不含周围空格）
  i" - 引号内的内容（不含引号）
  i' - 单引号内的内容
  i( 或 ib - 括号内的内容
  i{ 或 iB - 花括号内的内容
  i[ - 方括号内的内容
  it - HTML/XML 标签内的内容
  ip - 段落内容
  is - 句子内容

用法：操作符 + i + 对象，如 di" 删除引号内内容
""",
        why="""
为什么文本对象这么强大？

文本对象让你可以从任意位置操作整个结构：
- 光标在引号内任意位置，ci" 就能修改整个引号内容
- 不需要先移动到开头，再选择到结尾

这是 Vim 效率的核心秘密之一。
""",
        exercises=[
            Exercise(
                instruction="使用 ci\" 修改引号内的内容为 'Vim'",
                initial='Hello "World"',
                expected='Hello "Vim"',
                hint="将光标移到引号内，按 ci\" 然后输入 Vim，按 Esc",
                commands_to_learn=["ci\""],
                cursor_position=7,
            ),
            Exercise(
                instruction="使用 di( 删除括号内的内容",
                initial="function(delete this)",
                expected="function()",
                hint="将光标移到括号内，按 di(",
                commands_to_learn=["di("],
                cursor_position=10,
            ),
        ],
    ),
    Lesson(
        id="4.2",
        title="外部文本对象 a",
        module="文本对象",
        module_num=4,
        description="学习使用外部文本对象（包含边界）",
        explanation="""
外部文本对象 (a = around) 包含边界字符或周围空格：

  aw - 一个单词（含周围空格）
  a" - 引号及其内容
  a' - 单引号及其内容
  a( 或 ab - 括号及其内容
  a{ 或 aB - 花括号及其内容
  a[ - 方括号及其内容
  at - HTML/XML 标签及其内容
  ap - 段落（含周围空行）

i 和 a 的区别：
  di" - 删除引号内内容，保留引号
  da" - 删除引号和内容
""",
        why="""
什么时候用 i，什么时候用 a？

- 想保留容器（引号、括号等），用 i
- 想连容器一起操作，用 a
- 删除单词时，用 daw 会更干净（连空格一起删）
""",
        exercises=[
            Exercise(
                instruction="使用 daw 删除单词 'bad'（包括周围空格）",
                initial="this is bad text",
                expected="this is text",
                hint="移动到 bad 单词上，按 daw",
                commands_to_learn=["daw"],
                cursor_position=8,
            ),
            Exercise(
                instruction="使用 da\" 删除整个引号字符串",
                initial='keep "delete this" keep',
                expected="keep  keep",
                hint="移动到引号内，按 da\"",
                commands_to_learn=["da\""],
                cursor_position=6,
            ),
        ],
    ),
]


# Module 5: 可视模式
MODULE_5_LESSONS = [
    Lesson(
        id="5.1",
        title="可视模式基础 v/V/Ctrl-v",
        module="可视模式",
        module_num=5,
        description="学习三种可视模式",
        explanation="""
Vim 有三种可视模式用于选择文本：

  v - 字符可视模式（逐字符选择）
  V - 行可视模式（整行选择）
  Ctrl-v - 块可视模式（矩形选择）

选择后可以执行操作：
  d - 删除选中内容
  y - 复制选中内容
  c - 修改选中内容
  > - 增加缩进
  < - 减少缩进
  u - 转小写
  U - 转大写

按 Esc 或再按一次相同键退出可视模式。
""",
        why="""
什么时候用可视模式？

虽然 Vim 高手更多使用 动词+名词 的方式（如 d2w），
但可视模式在以下场景很有用：
- 不确定要选多少内容时，可以先看着选
- 需要对不规则区域操作时
- 块模式编辑多行时
""",
        exercises=[
            Exercise(
                instruction="使用 V 选中两行，然后按 d 删除",
                initial="保留\n删除1\n删除2\n保留",
                expected="保留\n保留",
                hint="按 j 到第二行，按 V 进入行可视模式，按 j 选中下一行，按 d 删除",
                commands_to_learn=["V", "d"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 v 选中 'select' 单词，然后按 U 转大写",
                initial="please select this",
                expected="please SELECT this",
                hint="移动到 s，按 v 进入可视模式，按 e 选到词尾，按 U",
                commands_to_learn=["v", "U"],
                cursor_position=7,
            ),
        ],
    ),
    Lesson(
        id="5.2",
        title="块可视模式",
        module="可视模式",
        module_num=5,
        description="学习块可视模式的强大功能",
        explanation="""
块可视模式 (Ctrl-v) 可以选择矩形区域：

选择后的特殊操作：
  I - 在块前插入（所有行）
  A - 在块后追加（所有行）
  c - 修改块内容（所有行）
  r - 替换块内所有字符

这对于编辑表格数据、批量添加前缀等非常有用。

技巧：选择后按 I 或 A 输入文本，按 Esc 后会应用到所有行。
""",
        why="""
块模式的实际应用场景：

1. 给多行代码添加注释前缀 //
2. 删除多行的相同前缀
3. 在多行末尾添加分号
4. 编辑对齐的表格数据
""",
        exercises=[
            Exercise(
                instruction="使用 Ctrl-v 选中三行开头，按 I 添加 '# ' 注释",
                initial="line 1\nline 2\nline 3",
                expected="# line 1\n# line 2\n# line 3",
                hint="按 Ctrl-v，按 jj 选中三行，按 I 输入 '# '，按 Esc",
                commands_to_learn=["Ctrl-v", "I"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 6: 搜索与替换
MODULE_6_LESSONS = [
    Lesson(
        id="6.1",
        title="搜索 /和?",
        module="搜索与替换",
        module_num=6,
        description="学习在文件中搜索文本",
        explanation="""
搜索命令：

  /pattern - 向下搜索 pattern
  ?pattern - 向上搜索 pattern
  n - 跳到下一个匹配
  N - 跳到上一个匹配
  * - 搜索光标下的单词（向下）
  # - 搜索光标下的单词（向上）

搜索支持正则表达式。按 Enter 确认搜索，按 Esc 取消。
""",
        why="""
为什么用 / 和 ?

这是从 ed 和 sed 编辑器继承的传统。
/ 向下搜索很直观（像是在文档中向下翻找）。
? 是 / 的反向版本。
""",
        exercises=[
            Exercise(
                instruction="使用 /vim 搜索 'vim'，然后按 n 跳到下一个匹配",
                initial="学习 vim 很有趣\nvim 是最好的编辑器\n我爱 vim",
                expected="学习 vim 很有趣\nvim 是最好的编辑器\n我爱 vim",
                hint="输入 /vim 然后按 Enter，按 n 跳到下一个",
                commands_to_learn=["/", "n"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="6.2",
        title="行内搜索 f/t",
        module="搜索与替换",
        module_num=6,
        description="学习在行内快速跳转到字符",
        explanation="""
行内搜索命令：

  f{char} - 向右跳到字符 char（光标在字符上）
  F{char} - 向左跳到字符 char
  t{char} - 向右跳到字符 char 前一个位置
  T{char} - 向左跳到字符 char 后一个位置
  ; - 重复上次 f/t 搜索（同方向）
  , - 重复上次 f/t 搜索（反方向）

这是行内移动最快的方式！
""",
        why="""
f 和 t 的区别？

- f 落在目标字符上，适合删除到某字符（df,）
- t 落在目标字符前，适合删除到某字符之前（dt,）

技巧：寻找行内不常见的字符（如 x、z、标点）作为跳转目标。
""",
        exercises=[
            Exercise(
                instruction="使用 f, 跳到逗号，然后用 dt. 删除到句号前的内容",
                initial="Hello, delete this part.",
                expected="Hello,.",
                hint="按 f, 跳到逗号，按 dt. 删除到句号前",
                commands_to_learn=["f", "dt"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="6.3",
        title="替换 :s",
        module="搜索与替换",
        module_num=6,
        description="学习搜索替换命令",
        explanation="""
替换命令：

  :s/old/new/ - 替换当前行第一个 old 为 new
  :s/old/new/g - 替换当前行所有 old 为 new
  :%s/old/new/g - 替换整个文件所有 old 为 new
  :%s/old/new/gc - 替换前逐个确认

常用标志：
  g - 全局替换（一行内多次）
  c - 确认每次替换
  i - 忽略大小写
""",
        why="""
为什么替换命令这么复杂？

:s 命令来自 sed，是一个非常强大的工具。
它支持正则表达式，可以进行复杂的文本转换。
虽然语法看起来复杂，但掌握后效率极高。
""",
        exercises=[
            Exercise(
                instruction="使用 :%s/cat/dog/g 将所有 'cat' 替换为 'dog'",
                initial="I have a cat.\nMy cat is cute.\ncat cat cat",
                expected="I have a dog.\nMy dog is cute.\ndog dog dog",
                hint="输入 :%s/cat/dog/g 然后按 Enter",
                commands_to_learn=[":%s"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 7: 高级移动与跳转
MODULE_7_LESSONS = [
    Lesson(
        id="7.1",
        title="文件内跳转 gg/G/%",
        module="高级移动与跳转",
        module_num=7,
        description="学习在文件内快速跳转",
        explanation="""
文件级跳转命令：

  gg - 跳到文件开头
  G - 跳到文件末尾
  {n}G 或 {n}gg - 跳到第 n 行
  % - 跳到匹配的括号 (){}[]

屏幕内跳转：
  H - 跳到屏幕顶部 (High)
  M - 跳到屏幕中间 (Middle)
  L - 跳到屏幕底部 (Low)

滚动屏幕：
  Ctrl-f - 向下翻页 (forward)
  Ctrl-b - 向上翻页 (backward)
  Ctrl-d - 向下半页 (down)
  Ctrl-u - 向上半页 (up)
  zz - 将当前行置于屏幕中央
""",
        why="""
为什么需要这么多跳转方式？

不同场景需要不同粒度的移动：
- 编辑代码时，% 跳转括号配对非常有用
- 浏览长文件时，Ctrl-d/u 比逐行滚动快得多
- zz 让你专注于当前编辑的代码
""",
        exercises=[
            Exercise(
                instruction="使用 G 跳到文件末尾，然后用 gg 回到开头",
                initial="第一行\n第二行\n第三行\n第四行\n最后一行",
                expected="第一行\n第二行\n第三行\n第四行\n最后一行",
                hint="按 G 到末尾，按 gg 回到开头",
                commands_to_learn=["G", "gg"],
                cursor_position=0,
            ),
            Exercise(
                instruction="使用 3G 跳到第3行，将 'three' 改为 'THREE'",
                initial="one\ntwo\nthree\nfour",
                expected="one\ntwo\nTHREE\nfour",
                hint="按 3G 跳到第3行，按 cw 输入 THREE",
                commands_to_learn=["3G", "cw"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="7.2",
        title="标记与跳转 m/'",
        module="高级移动与跳转",
        module_num=7,
        description="学习使用标记保存位置",
        explanation="""
标记（Mark）让你保存位置并快速返回：

设置标记：
  m{a-z} - 设置本地标记（当前文件）
  m{A-Z} - 设置全局标记（跨文件）

跳转到标记：
  '{a-z} - 跳到标记所在行
  `{a-z} - 跳到标记的精确位置（行和列）

特殊标记：
  '' - 跳回上次跳转前的位置
  `. - 跳到上次修改的位置
  `^ - 跳到上次插入的位置

跳转列表：
  Ctrl-o - 跳到上一个位置 (older)
  Ctrl-i - 跳到下一个位置 (newer)
""",
        why="""
标记的实际用途：

1. 在长文件中标记重要位置，快速来回跳转
2. 用 `` 快速返回上次位置（非常常用！）
3. 全局标记可以跨文件跳转
4. Ctrl-o/i 让你在跳转历史中导航
""",
        exercises=[
            Exercise(
                instruction="用 ma 在第一行设置标记，跳到最后一行后用 'a 返回",
                initial="标记这里\n中间行\n最后一行",
                expected="标记这里\n中间行\n最后一行",
                hint="按 ma 设置标记，按 G 到末尾，按 'a 返回",
                commands_to_learn=["m", "'"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="7.3",
        title="窗口分割",
        module="高级移动与跳转",
        module_num=7,
        description="学习分割窗口同时查看多个文件",
        explanation="""
窗口分割命令：

  :sp [file] - 水平分割窗口 (split)
  :vs [file] - 垂直分割窗口 (vertical split)
  Ctrl-w s - 水平分割当前窗口
  Ctrl-w v - 垂直分割当前窗口

窗口间移动：
  Ctrl-w h/j/k/l - 移动到左/下/上/右窗口
  Ctrl-w w - 循环切换窗口
  Ctrl-w Ctrl-w - 同上

窗口操作：
  Ctrl-w c - 关闭当前窗口
  Ctrl-w o - 只保留当前窗口
  Ctrl-w = - 平均分配窗口大小
""",
        why="""
窗口分割的用途：

1. 同时查看代码和测试文件
2. 对比两个文件的差异
3. 一边看文档一边写代码
4. 查看同一文件的不同部分
""",
        exercises=[
            Exercise(
                instruction="这是了解性课程，直接 :wq 保存退出",
                initial="窗口分割让你同时查看多个文件\n试试 :vs 和 Ctrl-w w",
                expected="窗口分割让你同时查看多个文件\n试试 :vs 和 Ctrl-w w",
                hint="输入 :wq 保存退出",
                commands_to_learn=[":sp", ":vs", "Ctrl-w"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 8: 实用配置
MODULE_8_LESSONS = [
    Lesson(
        id="8.1",
        title="行号与相对行号",
        module="实用配置",
        module_num=8,
        description="学习配置行号显示",
        explanation="""
行号配置命令（在 Vim 中输入）：

  :set number - 显示绝对行号
  :set nonumber - 隐藏行号
  :set relativenumber - 显示相对行号
  :set norelativenumber - 隐藏相对行号

推荐组合：
  :set number relativenumber

这会显示当前行的绝对行号，其他行显示相对行号。

永久配置（写入 ~/.vimrc）：
  set number
  set relativenumber
""",
        why="""
为什么用相对行号？

相对行号让你一眼就能看出目标行距离多远：
- 看到目标在 5 行下方，直接按 5j
- 想删除到 8 行下方，直接按 d8j

不需要心算 "81 - 73 = 8"，大大提高效率！
""",
        exercises=[
            Exercise(
                instruction="输入 :set number relativenumber 开启混合行号，然后 :wq 保存退出",
                initial="第一行\n第二行\n第三行",
                expected="第一行\n第二行\n第三行",
                hint="输入 :set number relativenumber 然后回车，再 :wq",
                commands_to_learn=[":set number", ":set relativenumber"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="8.2",
        title="搜索配置",
        module="实用配置",
        module_num=8,
        description="学习优化搜索体验的配置",
        explanation="""
搜索相关配置：

  :set hlsearch - 高亮所有搜索匹配
  :set nohlsearch - 关闭搜索高亮
  :noh - 临时清除当前高亮（不关闭功能）

  :set incsearch - 增量搜索（边输入边搜索）
  :set ignorecase - 搜索忽略大小写
  :set smartcase - 智能大小写（有大写时区分）

推荐配置组合：
  set hlsearch
  set incsearch
  set ignorecase
  set smartcase
""",
        why="""
smartcase 是什么？

当 ignorecase 和 smartcase 都开启时：
- 搜索 /hello 会匹配 Hello、HELLO、hello
- 搜索 /Hello 只匹配 Hello（因为包含大写）

这样既方便又灵活！
""",
        exercises=[
            Exercise(
                instruction="输入 :set hlsearch incsearch 然后搜索 /vim",
                initial="vim is great\nI love vim\nVIM is powerful",
                expected="vim is great\nI love vim\nVIM is powerful",
                hint="输入 :set hlsearch incsearch 回车，然后 /vim 回车",
                commands_to_learn=[":set hlsearch", ":set incsearch"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="8.3",
        title="缩进与制表符",
        module="实用配置",
        module_num=8,
        description="学习配置缩进行为",
        explanation="""
缩进相关配置：

  :set tabstop=4 - Tab 显示为 4 个空格宽
  :set shiftwidth=4 - 自动缩进的宽度
  :set expandtab - 将 Tab 转换为空格
  :set noexpandtab - 保留真正的 Tab
  :set autoindent - 新行继承上一行缩进
  :set smartindent - 智能缩进（识别代码结构）

缩进操作：
  >> - 增加当前行缩进
  << - 减少当前行缩进
  = - 自动格式化缩进
  gg=G - 格式化整个文件的缩进
""",
        why="""
Tab vs 空格之争？

这是程序员永恒的话题。建议：
- 遵循项目已有的风格
- Python 推荐 4 空格
- 很多项目用 2 空格
- expandtab 可以避免 Tab/空格混用的问题
""",
        exercises=[
            Exercise(
                instruction="使用 >> 增加第二行的缩进（会添加一个 Tab 或空格）",
                initial="if true:\nprint('hi')",
                expected="if true:\n\tprint('hi')",
                hint="按 j 到第二行，按 >> 增加缩进",
                commands_to_learn=[">>"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 9: 宏与重复
MODULE_9_LESSONS = [
    Lesson(
        id="9.1",
        title="点命令重复",
        module="宏与重复",
        module_num=9,
        description="学习使用点命令重复操作",
        explanation="""
点命令 (.) 是 Vim 最强大的命令之一：

  . - 重复上一次修改操作

什么算"修改操作"？
- 从进入插入模式到退出的所有输入
- 删除操作（d、x 等）
- 修改操作（c、r、s 等）
- 粘贴操作（p）

技巧：设计你的操作，让它可以被 . 重复
例如：ciw 修改单词后，可以用 n. 找下一个并重复修改
""",
        why="""
为什么点命令这么重要？

点命令体现了 Vim 的哲学：
1. 做一次操作
2. 移动到下一个位置
3. 按 . 重复

这比录制宏更轻量，比手动重复更高效。
""",
        exercises=[
            Exercise(
                instruction="用 x 删除第一个字符，然后按 . 两次删除后面两个",
                initial="abcdef",
                expected="def",
                hint="按 x 删除 a，按 . 删除 b，再按 . 删除 c",
                commands_to_learn=[".", "x"],
                cursor_position=0,
            ),
            Exercise(
                instruction="用 cw 将 'aa' 改为 'xx'，然后用 w. 修改其他的",
                initial="aa bb aa",
                expected="xx bb xx",
                hint="按 cw 输入 xx，按 Esc，按 w 跳过 bb，按 w 到第二个 aa，按 .",
                commands_to_learn=[".", "cw", "w"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="9.2",
        title="宏录制与播放",
        module="宏与重复",
        module_num=9,
        description="学习录制和使用宏",
        explanation="""
宏可以录制一系列操作并重复播放：

录制宏：
  q{a-z} - 开始录制到寄存器（如 qa）
  q - 停止录制

播放宏：
  @{a-z} - 播放寄存器中的宏（如 @a）
  @@ - 重复上次播放的宏
  {n}@{a-z} - 播放宏 n 次

技巧：
1. 录制前先想好完整流程
2. 从行首开始（按 0）确保位置一致
3. 用 j 移动到下一行，方便重复
""",
        why="""
什么时候用宏？

当你需要对多行/多处做相同的复杂操作时：
- 格式化多行数据
- 批量重命名
- 重复的代码修改

宏比点命令更强大，可以包含移动和多个操作。
""",
        exercises=[
            Exercise(
                instruction="录制宏：qa 开始，I# <Esc>j 添加注释并下移，q 结束。然后 2@a 应用到剩余行",
                initial="line 1\nline 2\nline 3",
                expected="# line 1\n# line 2\n# line 3",
                hint="按 qa 开始录制，I# <Esc>j，按 q 停止，按 2@a",
                commands_to_learn=["q", "@"],
                cursor_position=0,
            ),
        ],
    ),
]


# Module 10: 插件与进阶
MODULE_10_LESSONS = [
    Lesson(
        id="10.1",
        title="插件管理器",
        module="插件与进阶",
        module_num=10,
        description="了解 Vim 插件生态",
        explanation="""
Vim 有丰富的插件生态。常用插件管理器：

vim-plug（推荐，简单易用）：
  安装：curl -fLo ~/.vim/autoload/plug.vim --create-dirs \\
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

在 ~/.vimrc 中配置：
  call plug#begin('~/.vim/plugged')
  Plug 'tpope/vim-surround'      " 快速修改包围符号
  Plug 'preservim/nerdtree'      " 文件树
  Plug 'junegunn/fzf.vim'        " 模糊搜索
  call plug#end()

安装插件：:PlugInstall
更新插件：:PlugUpdate
删除插件：:PlugClean
""",
        why="""
为什么需要插件？

Vim 本身已经很强大，但插件可以：
- 添加新功能（文件树、Git 集成）
- 增强现有功能（更好的补全、语法高亮）
- 提高特定语言的开发体验

建议：先熟悉原生 Vim，再逐步添加插件。
""",
        exercises=[
            Exercise(
                instruction="这是一个了解性课程，直接 :wq 保存退出即可",
                initial="# Vim 插件让编辑更高效\n# 但先掌握基础更重要",
                expected="# Vim 插件让编辑更高效\n# 但先掌握基础更重要",
                hint="输入 :wq 保存退出",
                commands_to_learn=[":PlugInstall"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="10.2",
        title="常用插件推荐",
        module="插件与进阶",
        module_num=10,
        description="了解最实用的 Vim 插件",
        explanation="""
强烈推荐的插件：

1. vim-surround - 快速操作包围符号
   cs"' - 将双引号改为单引号
   ds" - 删除双引号
   ysiw" - 给单词加双引号

2. vim-commentary - 快速注释
   gcc - 注释/取消注释当前行
   gc{motion} - 注释移动范围

3. fzf.vim - 模糊搜索文件
   :Files - 搜索文件
   :Rg - 搜索文件内容

4. NERDTree - 文件树
   :NERDTreeToggle - 开关文件树

5. coc.nvim - 智能补全（需要 Node.js）
   提供 VSCode 级别的自动补全
""",
        why="""
如何选择插件？

1. 解决实际痛点，不要为了装而装
2. 选择活跃维护的项目
3. 阅读文档，了解所有功能
4. 一次只添加一个，熟悉后再加下一个
""",
        exercises=[
            Exercise(
                instruction="这是一个了解性课程，直接 :wq 保存退出即可",
                initial="# 推荐先尝试 vim-surround\n# 它能大大提高编辑效率",
                expected="# 推荐先尝试 vim-surround\n# 它能大大提高编辑效率",
                hint="输入 :wq 保存退出",
                commands_to_learn=["vim-surround", "vim-commentary"],
                cursor_position=0,
            ),
        ],
    ),
    Lesson(
        id="10.3",
        title="vimrc 配置建议",
        module="插件与进阶",
        module_num=10,
        description="学习配置你自己的 vimrc",
        explanation="""
推荐的 ~/.vimrc 基础配置：

" 基础设置
set nocompatible          " 不兼容 vi
set encoding=utf-8        " UTF-8 编码
set number relativenumber " 混合行号
set cursorline            " 高亮当前行
set showmatch             " 显示匹配括号
set wildmenu              " 命令行补全菜单

" 搜索设置
set hlsearch incsearch    " 高亮和增量搜索
set ignorecase smartcase  " 智能大小写

" 缩进设置
set tabstop=4 shiftwidth=4
set expandtab             " Tab 转空格
set autoindent smartindent

" 其他实用设置
set clipboard=unnamed     " 使用系统剪贴板
set mouse=a               " 启用鼠标
set scrolloff=5           " 光标距边缘5行
syntax on                 " 语法高亮
""",
        why="""
vimrc 的哲学：

1. 从简单开始，逐步添加
2. 理解每一行配置的作用
3. 不要盲目复制别人的配置
4. 定期清理不用的配置

你的 vimrc 应该是为你自己定制的！
""",
        exercises=[
            Exercise(
                instruction="这是最后一课！输入 :wq 完成整个课程",
                initial="恭喜你完成了 VimLearn 的所有课程！\n现在你已经掌握了 Vim 的核心技能。\n继续练习，Vim 会成为你最强大的工具！",
                expected="恭喜你完成了 VimLearn 的所有课程！\n现在你已经掌握了 Vim 的核心技能。\n继续练习，Vim 会成为你最强大的工具！",
                hint="输入 :wq 保存退出，完成课程！",
                commands_to_learn=["~/.vimrc"],
                cursor_position=0,
            ),
        ],
    ),
]


# 构建模块列表
MODULES = [
    Module(
        num=1,
        title="基础移动",
        description="学习 Vim 中的光标移动方式",
        lessons=MODULE_1_LESSONS,
    ),
    Module(
        num=2,
        title="编辑操作",
        description="学习插入、删除、修改文本",
        lessons=MODULE_2_LESSONS,
    ),
    Module(
        num=3,
        title="复制粘贴与撤销",
        description="学习复制、粘贴和撤销操作",
        lessons=MODULE_3_LESSONS,
    ),
    Module(
        num=4,
        title="文本对象",
        description="学习使用文本对象精确操作",
        lessons=MODULE_4_LESSONS,
    ),
    Module(
        num=5,
        title="可视模式",
        description="学习可视模式选择和操作",
        lessons=MODULE_5_LESSONS,
    ),
    Module(
        num=6,
        title="搜索与替换",
        description="学习搜索和替换文本",
        lessons=MODULE_6_LESSONS,
    ),
    Module(
        num=7,
        title="高级移动与跳转",
        description="学习文件内跳转和标记",
        lessons=MODULE_7_LESSONS,
    ),
    Module(
        num=8,
        title="实用配置",
        description="学习常用的 Vim 配置选项",
        lessons=MODULE_8_LESSONS,
    ),
    Module(
        num=9,
        title="宏与重复",
        description="学习点命令和宏录制",
        lessons=MODULE_9_LESSONS,
    ),
    Module(
        num=10,
        title="插件与进阶",
        description="了解插件生态和配置建议",
        lessons=MODULE_10_LESSONS,
    ),
]


def get_all_lessons() -> list[Lesson]:
    """Get all lessons in order."""
    lessons = []
    for module in MODULES:
        lessons.extend(module.lessons)
    return lessons


def get_lesson(lesson_id: str) -> Optional[Lesson]:
    """Get a lesson by its ID."""
    for lesson in get_all_lessons():
        if lesson.id == lesson_id:
            return lesson
    return None


def get_module_lessons(module_num: int) -> list[Lesson]:
    """Get all lessons in a module."""
    for module in MODULES:
        if module.num == module_num:
            return module.lessons
    return []
