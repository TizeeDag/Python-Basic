# Python Basic

Solutions for the coding assignments in Campus IL's **self.py** basic Python course.
There are **53 separate exercise files** in Chapters 1–9 and a standalone final
Hangman program in Chapter 10. Each exercise file can be run independently with
Python 3. No external packages are required.

```bash
python chapter_5/exercise_5_3_6.py
python chapter_10/hangman.py
```

When Hangman asks for a file path, enter `chapter_10/words.txt` if you launched
it from the repository root. Enter `5` as the index to choose `cat` from the
included sample file. Word indexes start at 1 and wrap around at the end of
the file. Invalid or repeated letter guesses do not consume a failed attempt.

| Chapter | Topic | Coding files |
| --- | --- | ---: |
| 1 | Introduction and Hangman artwork | 3 |
| 2 | Variables and input | 3 |
| 3 | Strings | 6 |
| 4 | Conditions | 4 |
| 5 | Functions | 6 |
| 6 | Lists | 7 |
| 7 | Loops | 9 |
| 8 | Tuples and dictionaries | 8 |
| 9 | Files | 7 |
| 10 | Complete Hangman game | 1 |

`exercise_index.json` maps every numbered coding assignment to its file and
original course page. Quiz-only exercises are omitted. Existing Campus IL
answers were not changed, and no files were submitted to Campus IL.

Function exercises expose the exact function names requested by the course.
They also contain a `main()` example or input prompts for direct execution.
File-writing exercises modify the destination specified by the caller;
exercise 9.2.3 writes `found.txt` in the current working directory.

Validation: all 54 course Python files compile. Every exercise was checked
using course examples or representative input; checks also cover list mutation,
file reads and writes, short playlists, circular word selection, invalid and
repeated guesses, and complete Hangman win/loss paths. There were 135 equality
checks plus output and syntax-restriction checks.

Course example note: exercise 8.2.3 shows two different pair orders. The
solution returns each pair immediately followed by its reverse, matching the
first example; the second example contains the same pairs in a different order.
