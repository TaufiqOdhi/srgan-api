# import numpy as np
# import torch
import argparse
# from PIL import Image
# from ai.compress import compress_binary, recovery_srgan, recovery_binary
# from ai.model import Generator
# from ai.config import DEVICE


# read argument from command line
parser = argparse.ArgumentParser(description='Pytorch SRGAN Script')
parser.add_argument("-n", "--name", help = "filename for image result", default='result')
parser.add_argument("-f", "--file", help="input image file")
args = parser.parse_args()

if __name__ == '__main__':
    CKPT_PTH = '/mnt/Windows/Users/taufi/MyFile/Projects/image-compression-restoration/04_1_binaryCompression_srganRecovery_layerWisePruning/checkpoints/no_prune/gen.pth.tar'

    print(args.name)
    print(args.file)

    # gen = Generator()
    # gen.load_state_dict(torch.load(CKPT_PTH)["state_dict"])
    # gen.eval().to(DEVICE)

    # input_image = np.asarray(Image.open(image.file))
    # input_image = compress_binary(input_image)
    # input_image = recovery_binary(input_image)
    # input_image = recovery_srgan(img=input_image, gen=gen)
    # Image.fromarray(input_image).save(file_path)
