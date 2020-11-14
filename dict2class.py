class Dict2Class:
    """
    Преобразует dict в class и допускает обращение через отрибуты
    """
    def __init__(self, content: dict):
        self.content = content

    def __getattr__(self, item):
        val = self.content.get(item)
        if not val:
            raise AttributeError(f"No {item} attribute")
        if isinstance(val, dict):
            return Dict2Class(val)
        else:
            return val

    def __repr__(self):
        return str(self.content)
