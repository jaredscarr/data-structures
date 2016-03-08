# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, data, point_to=None):
        """Initialize node object."""
        self.data = data
        self.point_to = point_to
