# DramaX
 Password and text cracking tools in Python
> ### I am currently rebuilding Dramax from scratch. There might be some issues while working with repository

<br/>

![Main Menu](./docs/images/MainMenu.png "Main Menu")


## Introduction
`DramaX` is a tool to help you crack passwords and encypted text easier. It supports different Hash types ([full list](#Types)), many Ciphers ([full list](#List)). You can also make dictionaries with different options.

<br />

# Modules

## Hash Actions
A set of actions are provided related to hashes like `Decrypting` or `Identifying`. 

#### List of supported hashes:
  - md5
  - sha1
  - sha2 (224,256,384,512)
  - sha3 (224,256,384,512)

<br />

### Hash-Decrypter

You can decrypt hashed text with this tool. For supported hashes see [here](#List)
  - Step 1:
    - First you need to enter your hashed text
  - Step 2:
    - Select the hash method you text is encrypted (if you do not know about the hash type, check [here](#Hash-Identifiers) section)
  - Step 3:
    - Now you need to pass `path` of your dictionary files (absolute path is prefered incase you are not sure where is your current working directory)
    - Keep entering you dictionaries. when you are done, enter `end` to go to next stage
    - Now DramaX starts searching for your word 

<!-- <br /> -->

### Hash-Generator
This is a very simple tool. Only thing you need to do is to enter the text you want to hash and it will generate the hashed text for all [supported](#List) hashes.

<!-- <br /> -->

### Hash-Identifiers
If you are not sure about the method your text has been hashed, this module is useful. Currently there are 3 hash-identifiers in the repository. Pick the one that you prefer and then enter your hashed text to see the predictions about it.

Link to original repositories of these hash identifiers:
  - [psypanda/hashID](https://github.com/psypanda/hashID)
  - [blackploit/hash-identifier](https://github.com/blackploit/hash-identifier)
  - [AnimeshShaw/Hash-Algorithm-Identifier](https://github.com/AnimeshShaw/Hash-Algorithm-Identifier)
