from types import ModuleType
from flask import Blueprint


class RouterHelper:
    def __init__(self):
        self.router = Blueprint("router", __name__)

    def get_blueprint(self):
        return self.router

    @staticmethod
    def get_endpoint(module_name: str, func_name: str = 'ctx'):
        module_name = module_name.replace('.', '_')
        endpoint_name = '_'.join([module_name, func_name])
        return endpoint_name

    def use(self, url: str, module, func_name='ctx', **kwargs):
        self.router.add_url_rule(url,
                                 view_func=self.route(module, func_name),
                                 **kwargs)

    @classmethod
    def route(cls, module: ModuleType, func_name: str = 'ctx'):
        """主要是处理引入的函数的 __name__ 属性

        :param module: 具体处理逻辑的模块
        :type module: ModuleType
        :param func_name: 要引入的模块内的函数名, 默认为 'ctx'
        :type func_name: str, optional
        """
        try:
            func = getattr(module, func_name)
            module_name = module.__name__
            # 构造不同的 endpoint
            func.__name__ = cls.get_endpoint(module_name, func_name)
            return func

        except Exception as e:
            raise e
