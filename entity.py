class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self._context = context # 1개는 default의미, __2개는 rivate 접근 의미
        # 나머지는 완성하세요

    # get, set을 만든다.

    @property
    def context(self) -> str:
        return self._context

    @context
    def context(self, context):
        self.context = context

    # frame get, set을 만든다.

    # train get, set을 만든다.

    # test get, set을 만든다.

    # id get, set을 만든다.

    # label get, set을 만든다.



