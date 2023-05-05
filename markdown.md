Visual Stuido Code - Preview markdown - Shotcut(macOS): command + shift + p

>Markdown:Open Preview to the Side

# This is a MarkDown Demo File - Markdown语法

Markdown是一种轻量级标记语言，排版语法简洁，让人们更多地关注内容本身而非排版。它使用易读易写的纯文本格式编写文档，可与HTML混编，可导出 HTML、PDF 以及本身的 .md 格式的文件。因简洁、高效、易读、易写，Markdown被大量使用，如Github、Wikipedia、简书等。

在线体验一下 Markdown在线编辑器。
https://markdown.com.cn/editor/

千万不要被「标记」、「语言」吓到，Markdown的语法十分简单，常用的标记符号不超过十个，用于日常写作记录绰绰有余，不到半小时就能完全掌握。

就是这十个不到的标记符号，却能让人优雅地沉浸式记录，专注内容而不是纠结排版，达到「心中无尘，码字入神」的境界。

让我们从 Markdown 标题语法开始学习吧。
https://markdown.com.cn/basic-syntax/headings.html



# 1.标题语法
不同的 Markdown 应用程序处理 # 和标题之间的空格方式并不一致。为了兼容考虑，请用一个空格在 # 和标题之间进行分隔。


## Heading level 2	

### Heading level 3	

#### Heading level 4	

Heading level 1
===============

Heading level 2
---------------


# 2.段落语法

要创建段落，请使用空白行将一行或多行文本进行分隔。
不要用空格（spaces）或制表符（ tabs）缩进段落。



	
I really like using Markdown.

I think I'll use it to format all of my documents from now on.

# 3.换行语法
几乎每个 Markdown 应用程序都支持两个或多个空格进行换行，称为 结尾空格（trailing whitespace) 的方式，但这是有争议的，因为很难在编辑器中直接看到空格，并且很多人在每个句子后面都会有意或无意地添加两个空格。由于这个原因，你可能要使用除结尾空格以外的其它方式来换行。幸运的是，几乎每个 Markdown 应用程序都支持另一种换行方式：HTML 的 <br> 标签。

为了兼容性，请在行尾添加“结尾空格”或 HTML 的 <br> 标签来实现换行。



This is the first line.  
And this is the second line.  



And this is the 3rd line.  


# 4.强调语法

## 加粗文本（Bold）
要加粗文本，请在单词或短语的前后各添加两个星号（asterisks）或下划线（underscores）。如需加粗一个单词或短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加2个星号（asterisks）。


I just love **bold text**.  
I just love __bold text__.    
  


Markdown 应用程序在如何处理单词或短语中间的下划线上并不一致。为兼容考虑，在单词或短语中间部分加粗的话，请使用星号（asterisks）。

Love **is** bold	



## 斜体（Italic）


斜体显示文本，请在单词或短语的前后各添加1个星号（asterisks）或下划线

I just love *bold text*.  


同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加3个星号（asterisks）或下划线

I just love ***bold text***.  

This is really ***very*** important text.


# 5.引用

## 要创建块引用，请在段落前添加一个 > 符号。

> Dorothy followed her through many of the beautiful rooms in her castle.



## 块引用可以包含多个段落。为段落之间的空白行添加一个 > 符号。

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.


## 块引用可以嵌套。在要嵌套的段落前添加一个 >> 符号。

> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.


块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.


# 6.有序列表

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 1 起始。

1. First item
2. Second item
3. Third item
4. Fourth item  
5. 


1. First item
1. Second item
1. Third item
1. Fourth item   
2. 




1. First item
3. Second item
4. Third item
5. Fourth item
6. 


1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
       1. Indented item
       2. Indented item
4. Fourth item


# 7.代码语法
## 要将单词或短语表示为代码，请将其包裹在反引号 (`) 中。

At the command prompt, type `nano`.

## 转义反引号
如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(``)中。

``Use `code` in your Markdown file.``	  




### This is a code line: ```Hello world```

### 

    This is a code block:



## 代码块
### 要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。

    <html>
      <head>
      </head>
    </html>
  


### 围栏代码块
Markdown基本语法允许您通过将行缩进四个空格或一个制表符来创建代码块。如果发现不方便，请尝试使用受保护的代码块。根据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个反引号（(```）或三个波浪号（~~~）。


    Hello World


```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
### 语法高亮
许多Markdown处理器都支持受围栏代码块的语法突出显示。使用此功能，您可以为编写代码的任何语言添加颜色突出显示。
要添加语法突出显示，请在受防护的代码块之前的反引号旁边指定一种语言。

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


# 8.分隔线
要创建分隔线，请在单独一行上使用3个或多个星号 (***)、破折号 (---) 或下划线 (___) ，并且不能包含其他内容。

***

---

_________________
以上三个分隔线的渲染效果看起来都一样。


Try to put a blank line before...

---

...and after a horizontal rule.


# 9.链接语法
链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。

超链接Markdown语法代码：[超链接显示名](超链接地址 "超链接title")

对应的HTML代码：<a href="超链接地址" title="超链接title">超链接显示名</a>



这是一个链接 [Markdown语法](https://markdown.com.cn)。

这是 [toby 的 网站](https://www.tobyday.site)。


## 链接title是当鼠标悬停在链接上时会出现的文字，这个title是可选的
这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。


## 网址和Email地址
使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

<https://markdown.com.cn>  

<fake@example.com>


## 带格式化的链接
I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](#code).


不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。


[link](https://www.example.com/my%20great%20page)
  
# 10.图片语法

要添加图像，请使用感叹号 (!), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

插入图片Markdown语法代码：![图片alt](图片链接 "图片title")。

对应的HTML代码：<img src="图片链接" alt="图片alt" title="图片title">

![这是图片](/assets/img/philly-magic-garden.jpg "Magic Gardens")

# 11.转义字符
要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 \ 。

\* Without the backslash, this would be a bullet in an unordered list.


很多字符都可以通过使用反斜杠字符从而达到转义目的。


## 特殊字符自动转义
在 HTML 文件中，有两个字符需要特殊处理： < 和 & 。


 < 符号用于起始标签，  

 & 符号则用于标记 HTML 实体，  

 如果你只是想要使用这些符号，你必须要使用实体的形式，像是 &lt; 和 &amp;。

& 符号其实很容易让写作网页文件的人感到困扰，如果你要打「AT&T」 ，你必须要写成「AT&amp;T」 ，还得转换网址内的 & 符号，如果你要链接到：

http://images.google.com/images?num=30&q=larry+bird
你必须要把网址转成：

http://images.google.com/images?num=30&amp;q=larry+bird
才能放到链接标签的 href 属性里。


# 12.内嵌 HTML 标签
对于 Markdown 涵盖范围之外的标签，都可以直接在文件里面用 HTML 本身。如需使用 HTML，不需要额外标注这是 HTML 或是 Markdown，只需 HTML 标签添加到 Markdown 文本中即可。

# 行级别的內联标签
HTML 的行级內联标签如 \<span>、\<cite>、\<del>   

不受限制，可以在 Markdown 的段落、列表或是标题里任意使用。依照个人习惯，甚至可以不用 Markdown 格式，而采用 HTML 标签来格式化。  

例如：如果比较喜欢 HTML 的  

\<a>   或 
\<img>   标签，  

可以直接使用这些标签，而不用 Markdown 提供的链接或是图片语法。当你需要更改元素的属性时（例如为文本指定颜色或更改图像的宽度），使用 HTML 标签更方便些。

HTML 行级的內联标签和区块标签不同，在內联标签的范围内， Markdown 的语法是可以解析的。

This **word** is bold. This <em>word</em> is italic.



## 区块级别的标签
区块元素──比如 \<div>、\<table>、\<pre>、\<p> 等标签，必须在前后加上空行，以便于内容区分。而且这些元素的开始与结尾标签，不可以用 tab 或是空白来缩进。Markdown 会自动识别这区块元素，避免在区块标签前后加上没有必要的 \<p> 标签。

例如，在 Markdown 文件里加上一段 HTML 表格：

This is a regular paragraph.

<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

This is another regular paragraph.

请注意，Markdown 语法在 HTML 区块标签中将不会被进行处理。例如，你无法在 HTML 区块内使用 Markdown 形式的*强调*。



