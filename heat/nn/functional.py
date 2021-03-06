import torch
import sys


def func_getattr(name):
    # call through to the torch.nn.functional module
    try:
        return torch.nn.functional.__getattribute__(name)
    except AttributeError:
        if name is not None:
            raise AttributeError("module not implemented in Torch Functional")


if sys.version_info.minor == 6:

    class Wrapper(object):
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def __getattr__(self, name):
            # call through to the torch.nn.functional module
            try:
                return torch.nn.functional.__getattribute__(name)
            except AttributeError:
                if name is not None:
                    raise AttributeError("module not implemented in Torch Functional")

    sys.modules[__name__] = Wrapper(sys.modules[__name__])
