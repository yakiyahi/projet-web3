const ContratSoumissions = artifacts.require("ContratSoumissions");


module.exports = function(deployer) {
  deployer.deploy(ContratSoumissions);
};
