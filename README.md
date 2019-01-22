# Python-Cookbook
供平时学习查询使用,中文为简单提示，代码详见源码对应的题号，如1.3对应1_3.py
## 第一章 数据结构和算法
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
## 第二章 字符串和文本
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
## 第三章 数字、日期和时间
TODO</br>
## 第四章 迭代器和生成器
4.1 手动访问迭代器中的元素</br>
要手动访问可迭代对象中的元素，可以使用next()函数。</br>
4.2 委托迭代</br>
一般来说，要做的就是定义一个__iter__()方法，将迭代请求委托到对象内部持有的容器上即可，实际上由该对象内部实现的__next__()方法完成实际的迭代。</br>
4.3 用生成器创建新的迭代模式</br>
函数中只要出现了yield语音就会将其转换成一个生成器。</br>
4.4 实现迭代协议</br>
要在对象上实现可迭代功能，最简单的方式就是使用生成器函数，如下实现深度优先遍历。</br>
....</br>
def __iter__(self):</br>
　　return iter(self\.\_childer)</br>

def depth_first(self):</br>
　　yield self</br>
　　for c in self:</br>
　　　　yield from c.depth_first()</br>
....</br>      
4.5 反向迭代</br>
可以使用内建的reversed()函数实现反向迭代，但注意将可迭代对象转换成列表可能会消耗大量内存；在对象中实现__reverse__()方法，就可以在自定义的类中上实现反向迭代。</br>
4.6 定义带有额外状态的生成器函数</br>
如果想让生成器将状态暴露给用户，可以将其实现为一个类，然后把生成器函数的代码放到__iter__()方法中即可。</br>
4.7 对迭代器做切片操作</br>
使用itertools.islice()函数，如：</br>
for x in itertools.islice(c, 10, 20)</br>
重点强调的是islice()会消耗掉所提供的迭代器中的数据。由于迭代器中的元素只能访问一次，没法倒回去，因此如果往后还需要倒回去访问前面的数据，需要先将数据转到列表中去。</br>
4.8 跳过可迭代对象中的前一部分元素</br>
第一种办法是使用itertools。dropwhile()函数，要提供一个函数和一个可迭代对象，该函数返回的迭代器会丢弃掉序列中的前面几个元素，只要它们在所提供的函数中返回True即可：</br>
for line in dropwhile(lambda line: line.startwith('#'), f):</br>
第二种办法是，如果知道要跳过多少个函数，可以使用itertools.islice()函数：</br>
for x in islice(item, 3, None):</br>
最后一个参数None表示想要前3个元素之外的所有元素，即表示切片\[3:\]</br>
4.9 迭代所有可能的组合或排列</br>
排列使用itertools.permutations()</br>
组合使用itertools.combinations()</br>
4.10 以索引-值对的形式迭代序列</br>
当在元组序列上应用enumerate()时，如果元组本身也被分解展开的话就会出错，要正确处理其对应关系。</br>
4.11 同时迭代多个序列</br>
可以使用zip()函数同时迭代多个序列，整个迭代的长度和其中最短的输入序列长度相同；如果这种行为不是所需要的，可以使用itertools.zip_longest()来代替。</br>
4.12 在不同的容器中进行迭代</br>
需要对许多对象执行相同的操作，但是这些对象包含在不同的容器内，要避免嵌套循环处理，保持代码的可读性，itertools.chain()方法可以用来简化这个任务，对多个容器进行迭代。</br>
4.13 创建处理数据的管道</br>
import os</br>
4.14 扁平化处理嵌套型的序列</br>
from collections import Iterable</br>
4.15 合并多个有序序列，再对整个有序序列进行迭代</br>
import heapq</br>
重点强调的是，heapq.merge()要求所有的输入序列都是有序的。特别是，它不会首先将所有的数据读取到堆中，或者预先做任何排序的操作。它也不会对输入做任何验证，以检查它们是否满足有序的要求。相反，它只是简单的检查每个输入序列中的第一个元素，将最小的那个发送出去。然后再从之前选择的序列中读取一个新的元素，再重复执行这个步骤，直到所有的输入序列都耗尽为止。</br>
4.16 用迭代器取代while循环</br>
用iter()替代while，其中使用lambda可以创建一个不带参数的可调用对象。</br>
## 第五章 文件和IO
5.1 读写文本数据</br>
t是windows平台特有的所谓text mode(文本模式）,区别在于会自动识别windows平台的换行符。rt模式下，python在读取文本时会自动把\r\n转换成\n；wt模式下，Python写文件时会用\r\n来表示换行。</br>
默认情况下，文件的读取和写入采用的都是系统默认的文本编码方式，可以通过sys.getdefaulttencoding()来查询；open()函数提供一个可选的errors参数来处理错误</br>
5.2 将输出重定向到文件中</br>
将print()函数的输出重定向到一个文件中，只要加上file关键字参数即可。</br>
5.3 以不同的分隔符或行结尾符完成打印</br>
在print()函数中使用seq和end关键字参数来根据需要修改输出，而str.join()方法只能处理字符串，故前者更通用。</br>
5.4 读写二进制数据</br>
需要在二进制文件中读取或写入文本内容，确保要进行编码或解码操作，读取->解码decode，写入->编码encode</br>
5.5 对已不存在的文件执行写入操作</br>
通过使用open()函数中鲜为人知的x模式替代常见的w模式来解决。</br>
5.6 在字符串上执行I/O操作</br>
当出于某种原因需要模拟出一个普通文件时，使用io.StringIO()和io.BytesIO()来创建一个文件型对象，请注意io.StringIO()和io.BytesIO()实例是没有真正的文件描述符来对应的，因此无法工作在需要一个真正的系统级文件的代码环境中。</br>
5.7 读写压缩的数据文件</br>
类似open()函数，gzip.open()和bz2.open()所接受的参数与open()一样，也支持encoding、errors、newline等关键字参数；当写入压缩数据时，压缩级别可以通过compresslevel关键字参数指定。</br>
5.8 对固定大小的记录进行迭代</br>
利用iter()和functools.parital()来完成，对于文本文件，更多的是按行读取。</br>
5.9 将二进制数据读取到可变缓冲区中</br>
import
将二进制数据直接读取到一个可变缓冲区中，中间不经过任何拷贝环节，使用文件对象的readinto()方法即可；使用f.readinto()需要注意的是，必须总是检查它的返回值，即实际读取的字节数，如果字节数小于所提供的缓冲区大小，这可能表述数据被截断或遭到了破坏。使用内存映象(memoryview)，使得可以对存在的缓冲区做切片操作，但是中间不涉及任何拷贝操作。</br>
5.10 对二进制文件做内存映射</br>
import os</br>
import mmap</br>
通过mmap将文件映射到内存后，能够以高效和优雅的方式对文件的内容进行随机访问，优于通过组合各种seek()、read()和write()调用来访问。</br>
5.11 处理路径名</br>
要操纵路径名，可以使用os.path模块中的函数。</br>
5.12 检测文件是否存在</br>
利用os.path模块来对文件做检测简单而直接，唯一需要注意的是关于权限的问题。</br>
5.13 获取目录内容的列表</br>
可以使用os.listdir()函数来获取目录中的文件列表；文件名的匹配，可以用glob或者fnmatch模块。</br>
5.14 绕过文件名编码</br>
os.listdir('.')和os.listdir(b'.')使用原始字节串列出文件名。</br>
5.15 打印无法解码的文件名</br>
def bad_filename(filename)</br>
5.16 为已经打开的文件添加或修改编码方式</br>
这么做可能会破坏终端上的输出。</br>
5.17 将字节数据写入文本文件</br>
I/O系统是以不同的层次来构建的。文本文件是通过在缓冲的二进制模式文件上添加一个Unicode编码/解码层来构建的。buffer属性简单地指向底层的文件。如果访问该属性，就可以绕开文本编码/解码层了。</br>
5.18 将已有的文件描述符包装为文件对象</br>
并非所有的文件模式都可以得到支持。</br>
5.19 创建临时文件和目录</br>
from tempfile import TemporaryFile</br>
由TemporaryFile()创建的文件都是未命名的，而且在目录中也没有对应的条目，如果想解放这种限制，可以使用NamedTemporaryFile()函数来替代；要创建一个临时目录，可以使用tempfile.TemporaryDirectory()来实现。</br>
5.20 同串口进行通信</br>
对于串口通信来说，最好是使用pySerial包比较好import serial，请记住所有涉及串口的I/O操作都是二进制的，因此确保在代码中使用的字节而不是文本。</br>
5.21 序列化Python对象</br>
 要将Python对象序列化为字节流，就可以保存到文件中、存储到数据库中或者通过网络连接进行传输，最常见的做法是使用pickle模块：</br>
 将某个对象存储到文件中：</br>
 data = ....</br>
 f = open('somefile', 'wb')</br>
 pickle.dump(data, f)</br>
 要将对象存储为字符串，可以使用pickle.dumps():</br>
 s = pickle.dumps(data)</br>
 要从字节流中重新创建出对象，使用pickle.load()或pickle.loads()函数。</br>
 某些特定类型的对象是无法进行pickle操作的。这些对象一般来说都会涉及某种外部系统状态，用户自定义的类有时候可以通过提供__getstate__()和__setstate__()方法来规避这些限制。</br>
## 第六章 数据编码与处理（略读）
6.1 读写CSV数据</br>
6.2 读写JSON数据</br>
6.3 解析简单的XML文档</br>
6.4 以增量方式解析大型XML文件</br>
6.5 将字典转换为XML</br>
6.6 解析、修改和重写XML</br>
6.7 用命名空间来解析XML文档</br>
6.8 同关系型数据库进行交互</br>
6.9 编码和解码十六进制数字</br>
6.10 Base64编码和解码</br>
6.11 读写二进制结构的数组</br>
6.12 读取嵌套型和大小可变的二进制结构</br>
6.13 数据汇总和统计</br>
## 第十三章 实用脚本和系统管理
13.1 通过重定向、管道或输入文件来作为脚本的输入</br>
Python内置的fileinpute模块使得这一切变得简单</br>
13.2 终止程序并显示错误信息</br>
要让程序以这种方式终止，可以发出一个SystemExit异常，但要提供错误信息作为参数。</br>
raise SystemExit('It failed!')</br>
13.3 解析命令行选项</br>
可以用argparse模块来解析命令行选型。</br>
13.4 在运行时提供密码输入提示</br>
Python的getpass模块可以使用。</br>
13.5 获取终端大小</br>
可以使用os.get_terminal_size()函数来办到</br>
13.6 执行外部命令并获取输出</br>
可以使用函数subprocess.check_output()来完成。</br>
13.7 拷贝或移动文件和目录</br>
shutil模块中有着可移植的函数实现。</br>
13.8 创建和解包归档文件</br>
shutil模块中有两个函数——make_archive()和unpack_archive()。</br>
13.9 通过名称来查找文件</br>
搜索文件可使用os.walk()函数；为了避免出现可能像././foo//bar这样的诡异路径，还要用到两个额外的函数来修正结果。第一个是os.path.abspath()，它接受一个可能是相对的路径并将其组成绝对路径的形式。第二个是os.path。normpath()，它会将路径修正为标准化形式，从而帮助解决像双反斜、多当前目录的多次引用等问题。</br>
13.10 读取配置文件</br>
想要读取以常见的.ini格式所编写的配置文件，可以使用configparser模块来读取配置文件。</br>
13.11 给脚本添加日志记录</br>
使用logging模块。</br>
13.12 给库添加日志记录</br>
给一个库添加日志功能，但又不希望它影响那些没有使用日志功能的程序：创建一个专用的日志对象并将其初始化。</br>
13.13 创建一个秒表计时器</br>
使用time模块。</br>
13.14 给内存和CPU使用量设定限制</br>
resource模块可以用来执行这样的任务，但只适用于UNIX系统。</br>
13.15 加载Web浏览器</br>
webbrowser模块可用来以独立于平台的方式加载浏览器。</br>

## 第十五章 C语言扩展（比较复杂，略读）
TODO























