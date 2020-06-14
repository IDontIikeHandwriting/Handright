# coding: utf-8
import numbers

from handright._template import Template


class FontPool(object):
    """A pool for caching the font with different font size"""

    __slots__ = (
        "_font",
        "_font_pool",
    )

    _FONT_POOL_SIZE_KEY = "font_pool_size"
    _DEFAULT_FONT_POOL_SIZE = 1

    def __init__(self, template: Template):
        font = template.get_font()
        font_size = template.get_font_size()
        font_pool_size = template.get_ext().get(
            FontPool._FONT_POOL_SIZE_KEY, FontPool._DEFAULT_FONT_POOL_SIZE
        )
        if not isinstance(font_pool_size, numbers.Integral) or font_pool_size <= 0:
            raise ValueError('ext["{}"] must be a positive Integral.'.format(FontPool._FONT_POOL_SIZE_KEY))
        self._font_pool = dict()
        if template.get_font_size_sigma() == 0:
            self._font_pool[font_size] = font.font_variant(size=font_size)
        else:
            # TODO
            ...
        self._font = font

    def get_font(self, font_size: int):
        return self._font_pool.get(
            font_size, self._font.font_variant(size=font_size)
        )
