const SimpleStorage = artifacts.require("SimpleStorage");
const AppelOffres = artifacts.require("AppelOffres");
const Test = artifacts.require("Test");

module.exports = function(deployer) {
  deployer.deploy(SimpleStorage);
};
module.exports = function(deployer) {
  deployer.deploy(AppelOffres);
};
module.exports = function(deployer) {
  deployer.deploy(Test);
};
