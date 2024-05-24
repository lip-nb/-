# Topyra如何调整插入图片的大小和位置

Topyra是一款非常好用，外观美观度的MarkDown文本编辑器和阅读器，但是你是否也遇到过插入图片总是插入到奇怪的位置？最后因为不会调整位置，只能委曲求全写出一篇篇排版混乱，外观粗糙的笔记。如果你也有这方面的困扰，那么这篇文档就是为你定制的了！！！ 

## 一.调整图片大小

### 明明想放个示例代码，图片小到连字都看不清，谁懂啊？？？

![image-20240524233018432](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524233018432.png)

如何调整呢？**第一步**右键点击左上角的`小图标`

![image-20240524233302160](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524233302160.png)

现在就可以看到缩放图片的菜单栏啦，**第二步**选择你喜欢的图片比例就大功告成了

<img src="https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20240524_233426.png" alt="屏幕截图_20240524_233426" style="zoom:25%;" />

## 二.调整图片的位置

### 想在图片旁边加点文字，文字排版却乱七八糟，谁懂啊？？？

<img src="https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240525002042391.png" alt="image-20240525002042391" style="zoom:50%;" />

### 方法一：修改改图片链接中的html标签

![image-20240524234131446](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524234131446.png)

这这种方法的**缺陷**也很明显:就是调整的范围很有限。只能是居中,靠左或靠右。对应的属性值分别是"center","left","right"

还有一个**缺陷**，有时候直接复制图片不是html标签，而是显示的图片文件路径，例如这个样子：

![](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524234636671.png)

### 方法二：用开发者工具直接修改CSS和HTML标签

- 从菜单栏中点击上方的视图，再点击开发者工具。 或者使用快捷键`Shift+F12`

<img src="https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524235150439.png" alt="image-20240524235150439" style="zoom: 50%;" />

- 进入到开发者工具

![image-20240524235945354](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240524235945354.png)





- 右键代码区域，进入编辑属性

![image-20240525000128340](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240525000128340.png)

- 跟上面一样，进入编辑后加入align(位置)属性

![PixPin_2024-05-25_00-02-50](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/PixPin_2024-05-25_00-02-50.png)

- 接下来我们进行更加精细的调整，在下面可以看到两个属性调整左右边距`border-left`和`border-right`

<img src="https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/PixPin_2024-05-25_00-04-51.png" style="zoom: 67%;" />

- 可以看到这里我写了`200px`

![PixPin_2024-05-25_00-06-01](https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/PixPin_2024-05-25_00-06-01.png)

- 回到文档我们发现这张图片距离左边有200个像素点，这样我们就调整好了。是不是比之前美观多啦？如果觉得博主的教程还不错的话，就留下你的赞鼓励一下吧！博主还会制作更多精心的教程哒！

<img src="https://reyes-typora.oss-cn-guangzhou.aliyuncs.com/image-20240525001329227.png" alt="image-20240525001329227" style="zoom: 67%;" />
