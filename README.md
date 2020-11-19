toutiao_signature

代码均可本地运行  
原作者 https://github.com/lateautumn4lin/Review_Reverse  
toutiao_api1.py 和 _get_as_cp_signature.js 配合使用，没有修改源码
  
原作者 https://github.com/Yang-Leon/JsExercise/tree/5e55ac69d837c3175fca0fd31d6f4741b53f2f16  
toutiao_api2.py 和 acrawler.js 配合使用，优化了获取流程，使用 nodejs 运行 acrawler.js 于 http://127.0.0.1:8888 端口，带 nonce 和 url 参数即可获得 signature ；通过 toutiao_api2.py 可以获得 nonce 参数然后带 signature 作为 cookie 一起访问即可得到文章内容，流程简单易懂