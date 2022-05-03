# animation-sequences
Python function printing animation sequences in a given directory.

This repository includes:
* Analysis of the function (down below in the current file)
* File ```animation_sequences.py``` containing the function
* Test cases using unittest from Python: ```/tests/test_animation_sequences.py```
	* use command ```python -m unittest``` from the root of the project
___
## Analysis
### Task summary
We want a function that finds all animation sequences in a given directory.
The format for an animated sequence is 'name.####.ext'.

* **Input:** directory path
* **Output:** printed frame range in specific format
	* e.g. 'name: 1001, 1003-1500, 1600-2000'


### Use case assumptions:
Assumptions are made to keep the function as robust and simple as possible.
In a real world situation, each assumption would need to be validated with
the appropriate people: we don't want to miss out important edge cases, and
we don't want to spend time developing unnecessary features.

**1. path may not exist**

	Suggested outcome:
		exception raised


**2. path may contain more than one set of animated sequences**
 
	e.g. name1.[0000-0010].jpeg,
	     name2.[0000-0010].jpeg,
	     name3.[0000-0010].png

	Suggested output:
         'name1: 0-10'
         'name2: 0-10'
         'name3: 0-10'

**3. path may contain files with unknown format**
   
	e.g. name1.[0000-0010].jpeg,
         name2.000a.jpeg,
         name3.000.jpeg,
         name4.[0000-0010],
         name5.jpeg,
         name6,
         name7.0020.jpeg

	Suggested output:
         'name1: 0-10'
         'name7: 20'

**4. path contains one file extension per name**

The following example will not be supported to keep the function simple:

	e.g. name1.[0000-0010].jpeg,
         name1.[0011-0020].png,
         name2.[0000-0010].jpeg

	With the current output format, the output may be...
        'name1: 0-10'
        'name1: 11-20'
        'name2: 0-10'

        or

        'name1: 0-20'
        'name2: 0-10'

	...depending on the implementation. In both cases, the displayed
	information is not satisfying (i.e. unclear or wrong).
	
	In a real world situation, if we realize the function must support more than one extension per name, 
	one solution is to add more information to the output when necessary:

        'name1 (jpeg): 0-10'
        'name1 (png): 11-20'
        'name2: 0-10'

**5. filenames should include a-z, A-Z, 0-9, dashes, underscores and spaces only**

Also, the name should not contain leading spaces.

### Implementation
It's a matter of organizing filenames (string) in a given directory:

 	If path exists
     	For each string filtered to match format 'name.####.ext'
            	store K,V in dictionary, where K=name, V=list of number

    To output, iterate over dictionary. 
    The list needs to be organized in order to ouput desired range format:
	1. sort list
	2. As we iterate each number, retain the first and last value of each range.
	3. When the previous number visited is no longer a difference of 1, we know there's a gap detected: 
	   generate an interval if the first and last are different, otherwise generate the first (or last) number only
       
