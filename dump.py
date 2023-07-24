import textwrap

# Your text to be wrapped
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae augue odio. Phasellus non venenatis neque. Maecenas ut luctus nisi, id rhoncus lectus. In ac erat at quam luctus finibus eget sit amet purus."

# Get the terminal width (you may need to install the 'shutil' module for this)
import shutil
terminal_width = shutil.get_terminal_size().columns

# Wrap the text to fit within the terminal width
wrapped_text = textwrap.fill(text, width=terminal_width)

# Print the wrapped text
print(wrapped_text)
