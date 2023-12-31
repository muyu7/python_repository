class GlobalVariables:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalVariables, cls).__new__(cls)
            cls._instance.root = None
            cls._instance.canvas = None
            cls._instance.gap = 20
            # Put any initialization here.
        return cls._instance
    def set_root(self, value):
        self.root = value

    def get_root(self):
        return self.root

    def set_canvas(self, value):
        self.canvas = value

    def get_canvas(self):
        return self.canvas
    def get_gap(self):
        return self.gap