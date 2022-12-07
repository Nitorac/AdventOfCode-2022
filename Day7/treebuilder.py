from collections import defaultdict


class dotteddict(defaultdict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val


class TreeBuilder:
    """Returns mutable trees structure, allowing for the following:
    tree_builder = utils.TreeBuilder()
    tree_builder["harold"]["username"] = "hrldcpr"
    tree_builder['handler']['username'] = 'matthandlersux'
    users = tree_builder.to_dict()

    See https://gist.github.com/hrldcpr/2012250.
    """

    def __init__(self):
        self._builder = self._tree()
        self._dir_size = {}
        self._total_size = 0

    def __getitem__(self, key):
        return self._builder[key]

    def get_dir_sizes(self):
        res = self._dir_size.copy()
        res['/'] = self._total_size
        return res

    def add_dir(self, path):
        res = self._builder
        for e in path:
            res = res[e]

    def add_file(self, path, size):
        res = self._builder
        pathForNow = ""
        for e in path[:-1]:
            pathForNow += e + "/"
            if not pathForNow in self._dir_size:
                self._dir_size[pathForNow] = 0
            self._dir_size[pathForNow] += size
            res = res[e]
        res[path[-1]] = size
        self._total_size += size

    @classmethod
    def _tree(cls) -> dict:
        return dotteddict(cls._tree)

    @classmethod
    def _to_dict(cls, node):
        if isinstance(node, dict):
            return {k: cls._to_dict(node[k]) for k in node}
        return node

    def to_dict(self) -> dict:
        """Returns trees are either values or a builtin python dict."""
        return self._to_dict(self._builder)
