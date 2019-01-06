# Python-Cookbook
供平时学习查询使用,中文为简单提示，代码详见源码对应的题号，如1.3对应1_3.py
## 第一章
1.1 将序列分解为单独的变量</br>
任何序列（可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量，唯一的要求是变量的总数和结构要和序列相吻合。</br>
1.2 从任意长度的可迭代对象中分解元素</br>
"\*表达式"</br>
1.3 保存最后N个元素</br>
from collections import deque</br>
1.4 找出最大或最小的N个元素</br>
import heapd</br>
返回nums中前三个最大值heap.nlargest(3, nums)</br>
返回nums中前三个最小值heap.nsmallest(3, nums)</br>
生成小端堆heap.heapify(nums)</br>
讲第一个元素（最小的）弹出heap.heappop()</br>
1.5 实现优先级队列
实现一个队列，能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的那个元素</br>
import heapq</br>
1.6 在字典中将键映射到多个值上</br>
from collections import defaultdict</br>
1.7 让字典保持有序</br>
创建一个字典，同时当对字典做迭代或序列化操作时，也能控制其中元素的顺序；当构建一个映射结构以便稍后对其做序列化或编码成另一个格式时，OrderedDict(双向链表)显得特别有用,请注意OrderedDict的大小是普通字典的两倍</br>
from collections import OrderedDict</br>
1.8 与字典有关的计算问题</br>
利用zip()将字典的键和值反转，如果碰巧多个条目拥有相同的value值时，key将用来作为判定结果的依据</br>
1.9 在两个字典中寻找相同点</br>
通过keys()或items()方法执行常见的集合操作即可</br>
如: a.keys() & b.keys()</br>
    a.keys() - b.keys()</br>
    a.items() & b.items()</br>
1.10 从序列中移除重复项且保持元素间顺序不变</br>
def dedupe()</br>
1.11 对切片命名</br>
内置的slice()函数会创建一个切片对象，可以用在任何允许进行切片操作的地方；如果有一个slice对象的实例s，可以分别通过s.start, s.stop, s.step属性得到关于该对象的信息；可以通过使用indices(size)方法将切片映射到特定大小的序列上，返回一个(start, stop, step)元祖，所有的值都已经恰当地限制在边界以内，避免出现IndexError异常。</br>
1.12 找出序列中出现次数最多的元素</br>
from collections import Counter</br>
1.13 通过公共键对字典列表排序</br>
from operator import itemgetter</br>
1.14 对不原生支持比较操作的对象排序</br>
from operator import attrgetter</br>
1.15 根据字段将记录分组</br>
from itertools import groupby</br>
from collections import defaultdict</br>
1.16 筛选序列中的元素</br>
filter</br>
如果想把对一个序列的筛选结果施加到另一个相关的序列上时，使用itertools.compress()，输出时会给出所有在相应的布尔选择器中为True的可迭代对象元素。</br>
from itertools import compress
1.17 从字典中提取子集</br>
利用字典推导式：p = {key:value for key, value in prices.items() if value > 200}</br>
1.18 将名称映射到序列的元素中</br>
from collections import namedtuple</br>
1.19 同时对数据做转换和换算</br>
在函数参数中使用生成器表达式。</br>
1.20 将多个映射合并为单个映射</br>
from collections import ChainMap</br>
## 第二章
2.1 针对任意多的分隔符拆分字符串</br>
import re</br>
2.2 在字符串的开头或结尾处做文本匹配</br>
用来检查字符串的开头或结尾，使用str.startswith()和str.endswith()方法即可。</br>
2.3 利用Shell通配符做字符串匹配</br>
fnmatch模块提供了两个函数——fnmatch()和fnmatchcase()，可用来执行这样的匹配。fnmatch所完成的匹配操作有点介乎于简单的字符串方法和全功能的正则表达式之间，在处理数据时提供一种简单的机制以允许使用通配符。</br>
from fnmatch import fnmatch, fnmatchcase</br>
2.4 文本模式的匹配和查找</br>
re.match()方法总是尝试在字符串的开头找到匹配项；re.findall()方法针对整个文本搜索出所有的匹配项；当定义正则表达时，将部分模式用括号包起来的方式引入捕获组，从而每个组的内容都可以单独提取出来；re.finditer()方法以迭代的方式找出匹配项</br>
2.5 查找和替换文本</br>
import re</br>
使用re.sub()方法，第一个参数的要匹配的模式，第二个参数的要替换上的模式</br>
2.6 以不区分大小写的方式对文本做查找和替换</br>
import re</br>
若待替换的文本与匹配的文本大小写不吻合，需要用到一个支撑函数</br>
2.7 定义实现最短匹配的正则表达式</br>
\*操作符在正则表达式中的采用的是贪心策咯，所以匹配过程是基于找出最长的可能匹配来进行的，要解决这个问题，只要在模式中的\*操作符后加上\?修饰符即可。</br>
2.8 编写多行模式的正则表达式</br>
re.complie()函数可接受一个有用的标记——re.DOTALL，使得正则表达式中的句点(.)可以匹配所有的字符，也包括换行符。</br>
2.9 将Unicode文本统一表示为规范形式</br>
import unicodedata</br>
2.10 用正则表达式处理Unicode字符</br>
Unicode和正则表达式混在一起使用绝对是个能让人头痛欲裂的办法，建议考虑安装第三方的正则表达式库regex</br>
2.11 从字符串中去掉不需要的字符</br>
strip()方法可用来从字符串的开始和结尾处去掉字符；lstrip()和rstrip()可分别从左或从右侧开始执行去除字符的操作；默认情况下这些方法去除的是空格符，但也可以指定其他的字符。</br>
2.12 文本过滤和清理
复杂的文本过滤和清理可以考虑使用str.translate()方法</br>
2.13 对齐文本字符串</br>
基本的字符串对齐要求，可以使用字符串的ljust()、rjust()、center()方法；建议使用format()方法，该方法更通用，可作用于任意类型的对象。</br>
2.14 字符串连接及合并</br>
想要合并的字符串在一个序列或可迭代对象中，最快的方法是使用join()方法；如果只是想连接一些字符串，一般使用+操作符就足够了，但不适用在大量的字符串连接；打印的时候可以用</br>printf(a, b, c, sep=':')</br>避免使用</br>printf(a + ':' + b + ':' + c )</br>
2.15 给字符串中的变量名做插值处理</br>
通过format()方法近似模拟：</br>
 s = '{name} has {n} message.'</br>
 s.format(name='Guido', n=37)</br>
或format_map()和vars()联合使用。</br>
2.16 以固定的列数重新格式化文本</br>
可以使用textwarp模块来重新格式化文本的输出；可以通过os.get_terminal_size()来获取终端的大小。</br>
2.17 在文本中处理HTML和XML实体</br>
如果要生成文本，使用html.escape()函数来完成替换<or>这样的特殊字符相对来说是比较容易的；如果实际上是在处理HTML或XML，首先应该尝试使用一个合适的HTML或XML解释器。</br>
2.18 文本分词</br>
(非常复杂，涉及正则表达式，而且比较容易出错)关注下一节的PLY。</br>
2.19 编写一个简单的递归下降解析器</br>
(详见教材，比较复杂)</br>
2.20 在字节串上执行文本操作</br>
如果要同文本打交道，在程序中使用普通的文本字符串就好，不要用字符串。</br>
