# Natspec-crawler
## By: Carl Farterson ([@carlfarterson](https://github.com/carlfarterson))

### Description
Script to parse through smart contract directories to return a rating of the [natspec documentation](https://docs.soliditylang.org/en/develop/natspec-format.html)

### Requirements
* Each contract should have `@title`, `@author`
* All functions & contracts should have `@notice`
* One `@param` per parameters in a function
* One `@return` per return argument in a function

### Directions
1. Python 3.5+ and pip required
2. Clone directory to your local computer
3. `cd natspec-crawler`
4. `pip install -r Requirements.txt`
5. `python main.py {contracts directory path}`
    * For example, `python3 main.py /home/carl/Documents/some-repo/contracts`


### To-do
* [ ] Effectively score usage of `@inheritdoc` (currently inheritance checks return N/A)
* [ ] Interfaces - determine scoring
* [ ] Add `@dev` into scoring 
* [ ] Properly score .sol file with multiple contracts/interfaces 
