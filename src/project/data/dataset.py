from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, dataset_dir: str):
        self.dataset_dir = dataset_dir

    def __len__(self) -> int:
        return 0

    def __getitem__(self, i: int):
        return None
