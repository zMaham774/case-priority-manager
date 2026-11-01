"""General tree for the police hierarchy (SP, DSP, SHO, officers). Escalation walks up. O(h)."""


class HierarchyTree:
    def __init__(self):
        # TODO: implement
        pass

    def add_child(self, *args, **kwargs):
        raise NotImplementedError

    def parent_of(self, *args, **kwargs):
        raise NotImplementedError

    def path_to_root(self, *args, **kwargs):
        raise NotImplementedError

    def escalate(self, *args, **kwargs):
        raise NotImplementedError
