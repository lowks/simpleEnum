with open (".version", "rb") as fo:
    __version__ = fo.read ().decode ("utf-8")
__all__ = ['simpleEnum']
