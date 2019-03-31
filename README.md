# searchly
A command​ ​line​ ​driven​ ​text​ ​files search​ ​engine.
Searchly will walk through all text files passed in the command line args, index them to in memory DB, and then prompt a search console enabling searching across these files content.
It also returns the matching score for each document based on the number of words matched in the search query.

# Up & Run:
### Requirement:
The only needed requirements is `python` :D 
*Before starting to run the application, you must make sure that a **folder** exists on the OS holding text files **.txt** .*

To run the application, Simply run the following command from with in the app dir.
```
$ python3 main.py /path/to/dir/ /path/to/another/dir/

```

## TODO
- Write unit tests to each component.
- Add more documentation to each component with examples.
- Enhance the score formula of matching, currently it's very naive.
- Add [Pre-commit](https://github.com/pre-commit/pre-commit) to the application repo to maintain the structure and code style.
- Add a requirements file to hold application dependencies.
- If needed containerizing the application using [Docker](https://docker.com).