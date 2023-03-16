from ai.model import *
from ai.config import PRUNE_AMOUNT
import torch.nn.utils.prune as prune


class ConvBlockPruned(ConvBlock):
    def __init__(self, in_channels, out_channels, discriminator=False, use_act=True, use_bn=True, **kwargs):
        super().__init__(in_channels, out_channels, discriminator, use_act, use_bn, **kwargs)
        prune.random_unstructured(self.cnn, name='weight', amount=PRUNE_AMOUNT)
        prune.random_unstructured(self.act, name='weight', amount=PRUNE_AMOUNT)
        if use_bn:
           prune.random_unstructured(self.bn, name='weight', amount=PRUNE_AMOUNT)


class UpsampleBlockPruned(UpsampleBlock):
    def __init__(self, in_c, scale_factor):
        super().__init__(in_c, scale_factor)
        prune.random_unstructured(self.conv, name='weight', amount=PRUNE_AMOUNT)
        prune.random_unstructured(self.act, name='weight', amount=PRUNE_AMOUNT)


class ResidualBlockPruned(ResidualBlock):
    def __init__(self, in_channels):
        super().__init__(in_channels)
        self.block1 = ConvBlockPruned(
            in_channels,
            in_channels,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.block2 = ConvBlockPruned(
            in_channels,
            in_channels,
            kernel_size=3,
            stride=1,
            padding=1,
            use_act=False,
        )


class GeneratorPruned(Generator):
    def __init__(self, in_channels=3, num_channels=64, num_blocks=16, ratio=4):
        super().__init__(in_channels, num_channels, num_blocks, ratio)
        self.initial = ConvBlockPruned(in_channels, num_channels, kernel_size=9, stride=1, padding=4, use_bn=False)
        self.residuals = nn.Sequential(*[ResidualBlockPruned(num_channels) for _ in range(num_blocks)])
        self.convblock = ConvBlockPruned(num_channels, num_channels, kernel_size=3, stride=1, padding=1, use_act=False)
        self.upsamples = nn.Sequential(*[UpsampleBlockPruned(num_channels, 2) for _ in range(int(log2(ratio)))])

        prune.random_unstructured(self.final, name='weight', amount=PRUNE_AMOUNT)
