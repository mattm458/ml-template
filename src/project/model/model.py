from lightning import pytorch as pl


class MyModel(pl.LightningModule):
    def forward(self):
        return None

    def configure_optimizers(self):
        return None

    def training_step(self, batch, batch_idx: int):
        pass

    def validation_step(self, batch, batch_idx: int):
        pass

    def test_step(self, batch, batch_idx: int):
        pass
