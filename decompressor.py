from huffman import Huffman
import sys

path = 'images\\sample.bmp'
h = Huffman(path)
output_path ="images\sample.bin"
decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)