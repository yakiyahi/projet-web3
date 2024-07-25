// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ContractAuth {
   struct User {
        string username;
        bytes32 passwordHash;
        bool registered;
    }

    mapping(address => User) private users;

    event UserRegistered(address userAddress, string username);
    event UserAuthenticated(address userAddress, string username);

    modifier userExists(address userAddress) {
        require(users[userAddress].registered, "User does not exist");
        _;
    }

    modifier userDoesNotExist(address userAddress) {
        require(!users[userAddress].registered, "User already exists");
        _;
    }

    function register(string memory username, string memory password) public userDoesNotExist(msg.sender) {
        bytes32 passwordHash = keccak256(abi.encodePacked(password));
        users[msg.sender] = User(username, passwordHash, true);
        emit UserRegistered(msg.sender, username);
    }

    function authenticate(string memory username, string memory password) public userExists(msg.sender) returns (bool) {
        User memory user = users[msg.sender];
        require(keccak256(abi.encodePacked(username)) == keccak256(abi.encodePacked(user.username)), "Username does not match");
        require(keccak256(abi.encodePacked(password)) == user.passwordHash, "Password does not match");
        emit UserAuthenticated(msg.sender, username);
        return true;
    }

    function getUsername() public view userExists(msg.sender) returns (string memory) {
        return users[msg.sender].username;
    }
}
