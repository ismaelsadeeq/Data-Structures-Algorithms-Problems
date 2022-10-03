# Data Structures-Algorithms-Problems Contributing guidelines

Welcome to Data Structures algorithms-Algorithms Before sending your pull requests, make sure that you read the whole guidelines. If you have any doubt on the contributing guide, please feel free to state it clearly in an issue.

### Contributing and 
### Contributor
We are very happy that you consider implementing algorithms and data structures or solving a problems for others!, This repository is referenced and used by learners from around the globe. Being one of our contributors, you agree and confirm that:

Please Any plagiarized work will not be merged.
You did your work - plagiarism is not allowed in any way.
Your work will be distributed under MIT LICENCE your pull request is merged.
Your submitted work must fulfill our styles and standards.
New implementation is welcome! For example, new solutions to a problem, different representations of a graph data structure or algorithm designs with different complexity.

Improving comments or writing proper tests are also highly welcome.

### Contribution
We appreciate any contribution, from fixing grammar mistakes to implementing complex algorithms. Please read this section if you are contributing to your work.

If you submit a pull request that resolves an open issue, please help us to keep our issue list small by adding fixes: #{$ISSUE_NO} to your commit message. the issue will be closed if your PR is merged.

### What is an Algorithm?
An Algorithm is one or more functions (or classes) that:

take one or more inputs.
perform some internal calculations or data manipulations.
return one or more outputs.
have minimal side effects.
Algorithms should be packaged in a way that would make it easy for readers to put them into larger programs.

### Algorithms should:

have intuitive class and function names that make their purpose clear to readers.
use Programming naming conventions, Clean code and intuitive variable names to ease comprehension.
be flexible to take different input values.
### Data Structure
Arrangement of data in other to solve problem.
### Problems
Solution to known list of coding challenges or problems using an Algorithm ,and or a Data-structure

### You can use any programming language to contribute,
### Implementing same Algorithm, Data-Structure, or a problem solution in another programming language is also welcome

#### File Naming Convention
filenames should use the UpperCamelCase (PascalCase) style.
There should be no spaces in filenames.
Example: LinkedList.py is allowed but linkedlist.py,Linkedlist.py,linked-list.py,linkedList.py are not.

### Folder Structure
A folder name is also Upper-Camel-Case with hypen between.
Folder name should be a  Data structure Implementations, Algorithm Implementations, or a Problems name.
E.g  folder Sort, should include all sorting algorithms implementation.
E.g  folder Array should have problems solved with the array data-structure
E.g  folder Two-Pointer should have have problems  solved with the two pointer algorithm
E.g  folder Sliding-Window should have problems  solved with the sliding window algorithm.

If a folder does not exist for the Data-Structure you implemented, Algorithm or problem you solve create a new folder,
Create a folder with the Data-Structure or Algorithm name, In the folder creaate another folder (Programminglanguage-Data-structute) e.g Js-Linked-List
Inside Js-LinkedList create the file LinkedList.js to write your solution.
Add A Readme.md wo write a short problem or algorithm discription, Complexity/Runtime and a link to a blog post Explanation.
Testing
Be confident that your code works. When was the last time you committed a code change, your build failed, and half of your app stopped working? Mine was last week. Writing tests for our Algorithms will help us ensure the implementations are air tight even after multiple fixes and code changes.

It is advised that the algorithm file (module) does not contain any "live" code but rather just exports the function(s) needed to execute the algorithm. Your test code can import those function(s), call them with the appropriate parameters and inspect the outcome. Example: RatInAMaze.test.js.

Please refrain from printing to the console in your implementation AND test code.

You can (and should!) run all tests locally before committing your changes:


Wriiten by @ismaelsadeeq 2022
