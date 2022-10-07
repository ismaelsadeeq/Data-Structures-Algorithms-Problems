# Data Structures-Algorithms-Problems Contributing guidelines

Welcome to Data-Structures-Algorithms-Problems. Please make sure you have read the entire guideline before sending in your pull requests. If you have any doubts about the contributing guide, please don't hesitate to make it known in an issue.

### Contributing and 
### Contributor
We are thrilled that you are considering implementing Algorithms, Data-Structures, or solving problems for others!
This repository is referenced and used by learners from around the globe. As one of our contributors, you agree and confirm that:

Please Any plagiarized work will not be merged. You did your work - plagiarism is not allowed in any way. Your work will be distributed under MIT LICENCE once your pull request is merged. Your submitted work must fulfill our styles and standards. We welcome new implementation. For example, new approaches to a problem, different graph data structure representation, or algorithm designs of different degrees of complexity.

Improving comments or writing proper tests are also highly welcome.

### Contribution
We appreciate any contribution, from fixing grammar mistakes to implementing complex algorithms. Please read this section if you are contributing to this repository.

If you submit a pull request (PR) that resolves an open issue, please add fixes: #{$ISSUE_NO} in your commit message to help us keep our issue list short. If your PR is merged, the issue will be resolved.

### What is an Algorithm?
An Algorithm is one or more functions (or classes) that:

- take one or more inputs
- perform some internal calculations or data manipulations
- return one or more outputs
- have minimal side effects

Algorithms should be packaged in a way that would make it easy for readers to put them into larger programs.

### Algorithms should:

- have intuitive class and function names that make their purpose clear to readers
- use programming naming conventions, clean code and intuitive variable names to ease comprehension.
- be flexible to take different input values.

### Data Structure
Arrangement of data in order to solve a problem.

### Problems
Solution to known list of coding challenges or problems using an Algorithm,and or a Data-structure

### You can use any programming language to contribute.
### Implementing same Algorithm, Data-Structure, or a problem solution in another programming language is also welcome

#### File Naming Convention
filenames should use the UpperCamelCase (PascalCase) style.
There should be no spaces in filenames.
Example: <span style="color:green">LinkedList.py</span> is allowed but <span style="color:red">linkedlist.py,Linkedlist.py,linked-list.py,linkedList.py</span> are not.

### Folder Structure
A folder name is also Upper-Camel-Case with hypen between.
Folder name should be a  Data structure Implementation, Algorithm Implementation, or a Problem name.
E.g  folder Sort, should include all sorting algorithms implementation.
E.g  folder Array should have problems solved with the array data-structure
E.g  folder Two-Pointer should have have problems  solved with the two pointer algorithm
E.g  folder Sliding-Window should have problems solved with the sliding window algorithm.

Create a new folder if one doesn't already exist for the Data-Structure, Algorithm, or problem you solved. Make a folder with the name of the Data-Structure or Algorithm. In the folder if their is no folder for the programming language create another folder with the programming language name. e.g Python then inside it create another folder for the Data-Structure e.g LinkedList, 
inside LinkedList create source file for the Data-Structute e.g Js-Linked-List.js to write your solution.
Add a ReadMe.md file with a brief description of the problem or algorithm, its complexity and runtime, and a link to an explanation blog post.

### Testing
Be confident that your code works. When was the last time you committed a code change, your build failed and half of your app stopped working? Mine was last week. Writing tests for our Algorithms will help us ensure the implementations are air tight even after multiple fixes and code changes.

It is advised that the algorithm file (module) does not contain any "live" code but rather just exports the function(s) needed to execute the algorithm.

Please refrain from printing to the console in your implementation AND test code.


Written by @ismaelsadeeq 2022
Edited by @SulaimanAminuBarkindo 2022
