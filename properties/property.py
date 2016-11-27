from typing import List


class Property(object):
    def process(self) -> List[str]:
        raise NotImplementedError()
