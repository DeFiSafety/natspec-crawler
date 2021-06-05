# Natspec-crawler
## By: Carl Farterson ([@carlfarterson](https://github.com/carlfarterson))

### Description
Script to parse through smart contract directories to return a rating of the [natspec documentation](https://docs.soliditylang.org/en/develop/natspec-format.html)

### Requirements
* Each contract should have `@title`, `@author`
* All functions & contracts should have `@notice`
* One `@param` per parameters in a function
* One `@return` per return argument in a function

### To-do
* [ ] Effectively score usage of `@inheritdoc` (currently inheritance checks return N/A)
* [ ] Interfaces - determine scoring
* [ ] Add `@dev` into scoring 