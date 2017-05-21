'''
    QuickHull
'''

from typing import Tuple, List

try:
    from QuickHull import hull

except ImportError:
    pass


__all__ = ['quick_hull']


if False:
    def hull_quick_hull(*args) -> Tuple[List[Tuple[float, float, float]], List[int]]:
        '''
            hull_quick_hull
        '''
    
    hull.quick_hull = hull_quick_hull


def quick_hull(points, ccw=True):
    '''
        Create a hull.
    '''

    return hull.quick_hull(tuple(points), ccw)
