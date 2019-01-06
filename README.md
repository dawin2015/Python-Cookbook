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

