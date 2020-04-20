# spiderhub

一个被动的返回 JSON 格式的爬虫。

## 通用参数

所有通用参数可以使用 & 连接组合使用, 效果叠加

### 内容过滤

可以使用以下 URL query 过滤内容, 支持正则

#### filter 选出想要的内容

- filter: 过滤标题和描述
- filter_title: 过滤标题
- filter_description: 过滤描述
- filter_author: 过滤作者
- filter_time: 过滤时间，仅支持数字，单位为秒。返回指定时间范围内的内容。如果条目没有输出pubDate或者格式不正确将不会被过滤

#### filterout 去掉不要的内容

filterout: 过滤标题和描述
filterout_title: 过滤标题
filterout_description: 过滤描述
filterout_author: 过滤作者

### 条数限制

可以使用 limit 参数限制最大条数, 主要用于排行榜类 RSS

举例: ?limit=10

### mode 参数

可以使用 mode 参数来开启自动提取全文内容功能

举例: ?mode=fulltext
