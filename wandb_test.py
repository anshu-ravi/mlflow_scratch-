import wandb

wandb.init(
    project="test", 
    job_type="test")

wandb.log({"whatever": 1})
wandb.finish()
print("Done")
