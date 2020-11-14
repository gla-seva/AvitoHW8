class ColorizeMixin:
    repr_color_code = 33  # yellow

    def __repr__(self):
        s = super().__repr__()
        return f"\033[0;{self.repr_color_code}m{s}"
