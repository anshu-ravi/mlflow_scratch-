import os
import hydra 
from omegaconf import DictConfig
import mlflow


@hydra.main(config_name="config")
def main(cfg: DictConfig):
    root_path = hydra.utils.get_original_cwd()
    _ = mlflow.run(
        os.path.join(root_path, "step_1"),
        "main",
        parameters={
            "text": cfg['step_1_params']['text'],
        },
    )

if __name__ == "__main__":
    main()