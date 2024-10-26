from lightning import pytorch as pl
from torch import Tensor


class ExampleModel(pl.LightningModule):
    def forward(self, x: Tensor) -> Tensor:
        return x

    def configure_optimizers(self):
        return None

    def training_step(self, batch, batch_idx: int):
        pass

    def validation_step(self, batch, batch_idx: int):
        pass

    def test_step(self, batch, batch_idx: int):
        pass
