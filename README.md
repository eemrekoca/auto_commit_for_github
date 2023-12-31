﻿# Documentation for Automatic Git Commit Script

## Overview:
This script is designed to automatically append the current date and time to a file __(date.txt)__ in a specific Git repository and then commit and push the change to the repository.

## Prerequisites:
- The __gitpython__ library should be installed. You can install it using pip:
```
bash
-

pip install gitpython
```
- The script assumes that the given path is already a git repository, and it's configured with the required remote origin.

## How to Use:
Update the __`REPO_PATH`__ variable with the absolute path to your git repository.

Run the script:
```
bash
- 
python your_script_name.py
```


## Code Breakdown:
### 1. Import required modules:

 - __`os`__: For handling file paths.
 - __`datetime`__: For getting the current date and time.
 - __`Repo`__ from __`git`__: For Git operations.
2. ### Set variables:

- __`REPO_PATH`__: Path to your Git repository.
- __`FILE_PATH`__: Path to the file (date.txt) inside the repository.
- __`COMMIT_MESSAGE`__: Commit message template.
3. ### Append current date and time to the file:
Using Python's file I/O operations, the current date and time is appended to the file __`(date.txt)`__.

4. ### Git operations:

- Initialize the Git repository using the provided path.
- Add the modified file to staging.
- Commit the staged changes with the provided commit message.
- Push the committed changes to the remote repository on the main branch (or change this to your desired branch).

### Confirmation message:

The script prints "Commit successful!" after successfully committing and pushing the changes.

