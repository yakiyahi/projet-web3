// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ContratSoumissions {
    // Structure pour stocker les informations de soumission
    
    struct Soumission {
        uint numeroSoumission;
        address soumissionaire; // Adresse de la personne ayant soumis la soumission
        uint256 numeroContrat; // Numéro du contrat associé à la soumission
        string nom;
        string coutTotal;
        string delaiRealisation;
        string references;
    }
    
    // Tableau pour stocker toutes les soumissions
    Soumission[] public soumissions;
    uint public offreCount;
    
    // Fonction pour ajouter une nouvelle soumission
    function ajouterSoumission(
        address _soumissionaire,
        uint256 _numeroContrat,
        string memory _nom,
        string memory _coutTotal,
        string memory _delaiRealisation,
        string memory _references
    ) public  {
        offreCount++;
        // Créer une nouvelle instance de la structure Soumission
        Soumission memory nouvelleSoumission = Soumission({
            numeroSoumission: offreCount,
            soumissionaire: _soumissionaire,
            numeroContrat: _numeroContrat,
            nom: _nom,
            coutTotal: _coutTotal,
            delaiRealisation: _delaiRealisation,
            references: _references
        });
        
        // Ajouter la nouvelle soumission au tableau
        soumissions.push(nouvelleSoumission);
    }

    // Fonction pour obtenir le nombre total de soumissions
    function nombreSoumissions() public view returns (uint256) {
        return soumissions.length;
    }

    // Fonction pour obtenir les informations d'une soumission par son index
    function obtenirSoumissionParIndex(uint256 index) public view returns (
        uint numeroSoumission,
        address soumissionaire,
        uint256 numeroContrat,
        string memory nom,
        string memory coutTotal,
        string memory delaiRealisation,
        string memory references
    ) {
        require(index < soumissions.length, "L'index est en dehors de la plage");
        Soumission memory soumission = soumissions[index];
        return (
             soumission.numeroSoumission,
            soumission.soumissionaire,
            soumission.numeroContrat,
            soumission.nom,
            soumission.coutTotal,
            soumission.delaiRealisation,
            soumission.references
        );
    }

    // Fonction pour obtenir la liste de toutes les soumissions
    function listeToutesSoumissions() public view returns (Soumission[] memory) {
        return soumissions;
    }
}
