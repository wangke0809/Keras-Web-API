# Keras-Web-API

吐槽：老师让参加的一个[校内比赛](https://cloud.tencent.com/developer/contest/AI-marathon-bjut)，宿舍四人组队参加，由学校创业指导中心和PNP举办，参赛的绝大多数是创业指导中心训练营的成员，只有两队是报名参加的，去了才发现就是创业指导中心训练营自娱自乐的活动吧，受到了种种不公平的待遇。最后拿了2000块钱溜了。

直接用的Keras InceptionResNetV2的训练模型做分类，然后把分类结果翻译为中文，然后拿着结果爬营养数据。

用了不到一天时间完成，中间遇到了tf后端静态图加载问题，采用了先前向传播一次比较low的思路，以及上传图片经磁盘保存后再送入模型，很多可以优化的地方,后来发现[Keras博客有篇文章](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)，可供学习参考。

# 依赖

 - flask
 - flask_upload
 - keras
 - reuqests

# 使用

    python app.py

# 客户端

舍友做的安卓客户端。

![图1](https://github.com/wangke0809/Keras-Web-API/raw/master/readimg/figure1.png)

![图2](https://github.com/wangke0809/Keras-Web-API/raw/master/readimg/figure2.png)