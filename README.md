# Crack-JS
🎯Python3爬虫实战、JS加解密、逆向教程

犀牛数据 | 美团美食 | 企名片 | 七麦数据 | 淘大象 | 梦幻西游藏宝阁 |

漫画柜 | 财联社 | 中国空气质量在线监测分析平台 | 66ip代理 | 零度ip | 国家企业信用信息公示系统

| Author  | 咸鱼 |
| --- | --- |
| Email | 872887042@qq.com |
| 微信公众号 | 咸鱼学Python |
| Introduce | 数据解密、反爬处理、逆向教程 |


## 一、代码配套说明
- [x] [【零度】IP页面token参数加密逆向](https://mp.weixin.qq.com/s/B5jAhpqKmdyw4Eo6q7f2Kw)
- [x] [【66ip】cookie生成加密逆向](https://mp.weixin.qq.com/s/B5jAhpqKmdyw4Eo6q7f2Kw)
- [x] [【中国空气质量在线监测分析平台解密】数据解密]()
- [x] [【财联社】sign加密逆向](https://mp.weixin.qq.com/s/8mV8B5SiPc0N2ZHJP4kxWQ)
- [x] [【漫画柜】解密数据下载漫画](https://mp.weixin.qq.com/s/RcZ0riXzVN0ywE3JKD9Bmg)
- [x] [【梦幻西游】游戏装备属性加密逆向](https://mp.weixin.qq.com/s/5pp1vd00O-JHeAf6loaYfg)
- [x] [【七麦数据】加密反混淆]()
- [x] [【淘大象】无限debugger破解与混淆加密逆向](https://mp.weixin.qq.com/s/HQDcrnxRMP9B--r4N8g-ZA)
- [x] [【企名片】加密逆向](https://mp.weixin.qq.com/s/Hxt39LSvNsqm17bgfrjddQ)
- [x] [【美团美食】 token 参数加密逆向]()
- [x] [【犀牛数据】 列表数据解密](https://mp.weixin.qq.com/s/llvoP-PYOoxuBzZxRbu1nQ)
---- ---

# 目录

```
JS解密案例
│
├── lingduip                           // -----零度ip-----
│   ├── lindu_ip.js                    // js解密逻辑
├── 66ip                               // -----66ip代理----
│   ├── ip66_1.js                      // 无cookie状态或cookie过期状态返回的js
│   ├── ip66_2.js                      // 解析页面返回的js中 生成cookie的js
│   ├── ip66_3.js                      // 解析页面返回的js中 生成cookie的js(测试于20190803)
│   ├── ip66.py                        // Python 版完整demo
│   ├── ip66-0803.py                   // Python 版完整demo(测试于20190803)
├── aqi                                // -----中国空气质量在线监测分析平台-----
│   ├── aqi.js                         // js加密逻辑
│   ├── aqi_spider.py                  // 中国空气质量在线监测分析平台爬取demo
├── cailianshe                         // -----财联社电报-----
│   ├── cls.py                         // sign加密参数实现逻辑
├── exam                               // -----一个很有意思的爬虫机试题-----
│   ├── datamining-exam-20190422.py    // 爬虫机试题答案
├── manhuagui                          // -----漫画柜-----
│   ├── manhuagui_spider_best.py       // 漫画柜爬取demo - 这个运行做了爬取效率的改进
│   ├── manhuagui_spider.py            // 漫画柜爬取demo
├── menghuanxiyou                      // -----梦幻西游藏宝阁-----
│   ├── menghuanxiyou.py               // 梦幻西游藏宝阁的装备属性加密逆向demo
│   ├── test.py                        // 梦幻西游藏宝阁的装备属性加密逆向js
├── qimai_data                         // -----七麦数据-----
│   ├── qimai.py                       // 七麦数据解密demo
│   ├── en.js                          // 七麦数据解密js
├── taodaxiang                         // -----淘大象-----
│   ├── taodaxiang.js                  // 淘大象查询参数加密混淆逆向 js
├── qimingpian                         // -----企名片-----
│   ├── qimingpian.js                  // 企名片查询结果加密逆向 js demo
├── meituanmeishi                      // -----美团美食-----
│   ├── meituan.js                     // 美团美食 token 参数加密逆向 js
│   ├── meituan.py                     // 美团美食 token 参数加密逆向 demo
├── xiniudata                          // -----犀牛数据-----
│   ├── xiniudata-param.js             // 犀牛数据 参数加密逆向 js
│   ├── xiniudata-parse.py             // 犀牛数据 数据加密逆向 js
├── gsxt_gg                            // -----国家企业信用信息公示系统-----
│   ├── jsl.js                         // 国家企业信用信息公示系统 cookie生成调试js
│   ├── gsxtgg.py                      // 国家企业信用信息公示系统公告 爬取demo
```
