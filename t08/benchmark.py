import time
import torch
from torch.utils.data import Dataset, DataLoader


class TestDataset(Dataset):
    def __init__(self, size=10000):
        self.data = torch.randn(size, 100)
        self.labels = torch.randn(size, 1)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data[index]
        x = torch.sin(x) + torch.cos(x)
        return x, self.labels[index]


def benchmark(dataset, batch_size, num_workers,
              persistent_workers=False, epochs=3):

    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        persistent_workers=persistent_workers
    )

    start = time.perf_counter()

    for _ in range(epochs):
        for x, y in loader:
            _ = x + 1

    end = time.perf_counter()

    return (end - start) / epochs


def main():
    torch.manual_seed(20260907)

    dataset = TestDataset(10000)

    batch_sizes = [32, 64, 128]
    worker_counts = [0, 2, 4]

    print("DataLoader Performance Test")
    print("-" * 65)
    print(
        f"{'batch_size':<12}"
        f"{'workers':<10}"
        f"{'persistent':<15}"
        f"{'time(s)':<10}"
    )

    for batch_size in batch_sizes:
        for workers in worker_counts:

            avg_time = benchmark(
                dataset,
                batch_size,
                workers,
                False
            )

            print(
                f"{batch_size:<12}"
                f"{workers:<10}"
                f"{'False':<15}"
                f"{avg_time:.6f}"
            )

    print("\nPersistent Workers Test")
    print("-" * 65)

    for workers in [2, 4]:
        for persistent in [False, True]:

            avg_time = benchmark(
                dataset,
                64,
                workers,
                persistent
            )

            print(
                f"{64:<12}"
                f"{workers:<10}"
                f"{str(persistent):<15}"
                f"{avg_time:.6f}"
            )


if __name__ == "__main__":
    main()
