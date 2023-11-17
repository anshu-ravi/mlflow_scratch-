import argparse 
import wandb

def step1_func(text):
    print(f'Ouput from step1_func: {text}') 
    return text


def main(args):
    step1_func(args.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide parameters for step 1")
    parser.add_argument('--text', type=str, default='Hello World!')
    args = parser.parse_args()

    main(args)
