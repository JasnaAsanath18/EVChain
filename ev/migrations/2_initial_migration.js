const Migrations = artifacts.require("evchain");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
