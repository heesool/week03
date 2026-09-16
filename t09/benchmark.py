import time
import torch
from torch.nn.utils.rnn import pad_sequence


torch.manual_seed(20260907)

NUM_SEQUENCES = 512
MIN_LENGTH = 32
MAX_LENGTH = 256
FEATURE_DIM = 64
REPEAT = 100


lengths = torch.randint(
    MIN_LENGTH,
    MAX_LENGTH + 1,
    (NUM_SEQUENCES,)
)

sequences = [
    torch.randn(length.item(), FEATURE_DIM)
    for length in lengths
]


padded = pad_sequence(
    sequences,
    batch_first=True
)

packed = torch.cat(sequences, dim=0)

max_length = int(lengths.max())
total_valid_length = int(lengths.sum())

padding_positions = NUM_SEQUENCES * max_length
packed_positions = total_valid_length

padding_elements = padding_positions * FEATURE_DIM
packed_elements = packed_positions * FEATURE_DIM

redundancy = (
    (padding_positions - packed_positions)
    / padding_positions
    * 100
)

def benchmark(data):
    start = time.perf_counter()

    for _ in range(REPEAT):
        result = torch.sin(data) + torch.cos(data)

    end = time.perf_counter()

    return (end - start) / REPEAT


padding_time = benchmark(padded)

packing_time = benchmark(packed)

print("Variable Length Sequence Test")
print("-" * 50)

print(f"Number of sequences:      {NUM_SEQUENCES}")
print(f"Maximum sequence length:  {max_length}")
print(f"Total valid length:       {total_valid_length}")

print()
print("Storage Comparison")
print("-" * 50)

print(f"Padding positions:        {padding_positions}")
print(f"Packed positions:         {packed_positions}")

print(f"Padding elements:         {padding_elements}")
print(f"Packed elements:          {packed_elements}")

print(f"Padding redundancy:       {redundancy:.2f}%")

print()
print("Performance Test")
print("-" * 50)

print(f"{'Method':<15}{'Time(s)':<15}")
print(f"{'Padding':<15}{padding_time:.6f}")
print(f"{'Packing':<15}{packing_time:.6f}")
