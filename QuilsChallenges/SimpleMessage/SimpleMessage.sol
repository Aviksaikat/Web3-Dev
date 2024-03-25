// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/*
Challenge:
Write a Solidity contract that allows users to create and store their own simple messages on the blockchain. Each message should be associated with the user's Ethereum address, and users should be able to update their messages at any time. The contract should also allow anyone to view the stored messages for a given Ethereum address.

Instructions:

Create a new Solidity contract with a function for storing and updating messages associated with Ethereum addresses.
The function should take in a string message and store it alongside the Ethereum address of the user who submitted it.
The contract should also have a function that allows anyone to view the stored messages for a given Ethereum address.
Test the contract by deploying it to a testnet and interacting with it using a web3 interface like Remix.
Hints:

You can use a mapping to associate Ethereum addresses with their stored messages.
To allow users to update their messages, you may need to add a check to ensure that the Ethereum address associated with the message is the same as the address of the caller.
Consider using an event to emit the stored message and the Ethereum address of the user who submitted it.
Expected Output:
The contract should allow users to store and update their messages, and anyone should be able to view the messages associated with a given Ethereum address. When a new message is stored, the contract should emit an event containing the message and the Ethereum address of the user who submitted it.
*/


contract SimpleMessage {
    mapping(address => string) private messages;

    
    modifier checkOwner() {
        require(msg.sender == getUserAddr(), "Opps stick to your own msg!!");
        _;
    }
    
    // https://ethereum.stackexchange.com/questions/8658/what-does-the-indexed-keyword-do
    // The indexed parameters for logged events will allow you to search for these events using the indexed parameters as filters.
    event MessgeStored(address indexed user, string message);


    function getUserAddr() public view returns(address){
        return msg.sender;
    }

    //https://medium.com/coinmonks/solidity-storage-vs-memory-vs-calldata-8c7e8c38bce
    //Calldata is an immutable, temporary location where function arguments are stored, and behaves mostly like memory.
    function storeMsg(string calldata message) public {
        messages[msg.sender] = message;
        emit MessgeStored(msg.sender, message);
    }

    function updateMsg(string calldata message) public checkOwner {
        messages[msg.sender] = message;
        emit MessgeStored(msg.sender, message);
    }

    //Return a String with function giving an error 
    //https://ethereum.stackexchange.com/questions/71339/return-a-string-with-function-giving-an-error-in-solidity-0-5-1
    function viewMsg(address msgOwner) public view returns(string memory) {
        return messages[msgOwner];
    }

}