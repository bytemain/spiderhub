from .utils.router import RouterHelper

from src.routes import baidu_search
from src.routes import test

router = RouterHelper()

# 路由列表
router.use("/baidu_search/<q>/", baidu_search)
router.use("/baidu_search/<q>/<int:number>/", baidu_search)
router.use("/test", test)

# 前置
# scrapy
