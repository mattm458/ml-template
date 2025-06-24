# Machine Learning Template Repository

This repository contains a template for all of my ML projects. The template includes the following components:

- Basic project structure, including directories for models, dataloaders, tests, etc.
- A basic pyproject.toml file, including imports I use in most projects.
- An argument parser set up with CLI arguments I usually use.

Once you make your own project from this repository, create a virtual environment, enter it, then run:
```pip install -e .```

The repository is designed to take advantage of PyTorch Lightning and the [Lightning CLI](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.cli.LightningCLI.html) toolset. Please use the `config/` directory to manage different model configurations.

Once you have customized the repository, start training with:

```
<executable name> fit --config <configuration file>
```