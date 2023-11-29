'''Script to update README file'''
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
import re

# Read the content of the version.txt file
with open("version.txt","r",encoding="utf-8") as file:
    version = file.read().strip()

# Read the content of the README.md file
with open("README.md","r",encoding="utf-8") as file:
    readme_content = file.read()

# Use regular expression to find and replace the line containing the \
# old version in the README.md content
updated_readme_content = re.sub(r"last stable version: .+?\n",
                                f"last stable version: {version}\n",
                                readme_content)

# Write the updated README.md content back to the file
with open("README.md","w",encoding="utf-8") as file:
    file.write(updated_readme_content)
