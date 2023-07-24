from typing import Optional
import fire
from llama import Llama
import os

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.1,
    top_p: float = 1,
    max_seq_len: int = 4096,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    
    def get_user_input():
        return input("You: ")
    
    while True:    
        dialogs = [
            [
                {"role": "system", "content": "You are a helpful asisstant."},
                {"role": "user", "content": get_user_input()}
            ],
        ]
            
        # results = generator.chat_completion(
        #     dialogs,  # type: ignore
        #     max_gen_len=max_gen_len,
        #     temperature=temperature,
        #     top_p=top_p,
        # )

        # for dialog, result in zip(dialogs, results):
        #     for msg in dialog:
        #         print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        #     print(
        #         f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        #     )
        #     print("\n==================================\n")
            

        results = generator.chat_completion(
            dialogs,  # type: ignore
            max_gen_len=max_seq_len,
            temperature=temperature,
            top_p=top_p,
        )
        
        print(str(results[0]["generation"]["content"]))
        
        # Check if the user wants to clear terminal history
        clr_terminal = input("Do you want to clear ur terminal? (yes/no): ")
        if clr_terminal.lower() == "yes":
            os.system('cls')

        # Check if the user wants to continue chatting or exit the loop
        # user_response = input("Do you want to continue chatting? (yes/no): ")
        # if user_response.lower() != "yes":
        #     break

fire.Fire(main)
    
# if __name__ == "__main__":
#     fire.Fire(main)
