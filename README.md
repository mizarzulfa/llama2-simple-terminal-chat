# Llama 2 simple chat

## Demo Llama2 simple chat
![Demo](/media/llama2-demo.gif)

This animated GIF demonstrates how Llama 2 looks in action within a terminal environment.


# Prerequisite

Before proceeding, ensure you have completed the following steps:

1. **Download the [Llama2](https://github.com/facebookresearch/llama) project code and models.**
2. **Please follow all the instructions provided in the main repository carefully.**
3. **Place the 'Llama-chat.py' file in the 'llama' directory, at the same level as the 'download.sh' file.**

> **Please make sure to follow these prerequisites to set up the Llama2 project correctly before proceeding with any further steps.**


**Different models require different model-parallel (MP) values:**

|  Model | MP |
|--------|----|
| 7B     | 1  |
| 13B    | 2  |
| 70B    | 8  |

## Model Token Limit and Cache Pre-allocation

This documentation outlines important information regarding the token limits and cache pre-allocation for the models in this repository.

### Token Limit

All models in this repository support a sequence length of up to 4096 tokens. This means that any input text longer than 4096 tokens will need to be truncated or processed in parts to fit within this limit.

### Cache Pre-allocation

The cache is pre-allocated based on the `max_seq_len` and `max_batch_size` values. It is essential to set these parameters according to your hardware specifications and requirements.

- `max_seq_len`: This value should be set to the maximum sequence length that your hardware can handle efficiently. Make sure not to exceed the token limit of 4096 tokens to avoid issues with processing longer sequences.

- `max_batch_size`: This parameter determines the maximum batch size that can be processed in one iteration. Setting an appropriate value for this parameter ensures optimal memory usage and model performance.

Please adjust these settings based on your hardware capabilities to achieve the best performance and avoid any memory-related problems.

### Running the Chatbot

Use the `torchrun` command with the appropriate arguments to run the Llama-chat.py script:

```bash
torchrun --nproc_per_node 1 Llama-chat.py --ckpt_dir llama-2-7b-chat/ --tokenizer_path tokenizer.model
```

#### Optional Arguments

You can also pass some optional arguments to customize the chatbot's behavior:

- `--max_seq_len`: Set the maximum sequence length (default is 512).
- `--max_batch_size`: Set the maximum batch size (default is 4).

These optional arguments allow you to control the length and batch size of the input text for the chatbot.

### Notes

- Ensure you have the model and tokenizer available in the specified directories (`--ckpt_dir` and `--tokenizer_path`).
- model `--nproc_per_node [value]` needs to be set to the MP value.

Feel free to modify the arguments as needed to suit your specific use case.

For more information and usage examples, please refer to the official [Llama2](https://github.com/facebookresearch/llama) documentation and code repository on GitHub.

## Checking CUDA Availability on Windows

To check whether CUDA is available or installed on your Windows system, you can run the `CUDA_Check.py` script.
This code checks whether CUDA is available for use with PyTorch. The output will be either "`CUDA is available!`" or "`CUDA is not available. Using CPU instead.`" depending on whether CUDA is available on the system.