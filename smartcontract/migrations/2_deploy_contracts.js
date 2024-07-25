const ContratSoumissions = artifacts.require("ContratSoumissions");
const Authentification = artifacts.require("ContractAuth");

module.exports = function(deployer) {
  deployer.deploy(ContratSoumissions).then(function() {
    return deployer.deploy(Authentification);
  });
};