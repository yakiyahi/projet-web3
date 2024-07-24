// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract AppelOffres {

    // Structure pour stocker les détails de l'appel d'offres
    struct Offre {
        uint numero;
        string titre;
        string description;
        string societe;
        uint datePublication;
        uint dateCloture;
    }

    // Tableau des offres
    mapping(uint =>Offre) offres;
    uint public offreCount;

    event OffreCree(uint numero, string titre, string description, string societe,
     uint datePublication, uint dateCloture);

    function getOffreCount() public view returns(uint) {
        return offreCount;
    }

    // Fonction pour créer un nouvel appel d'offres
    function creerOffre(
        string memory _titre,
        string memory _description,
        string memory _societe,
        uint _datePublication,
        uint _dateCloture
    ) public {
        offreCount++;

        offres[offreCount] = Offre(offreCount, _titre, _description, _societe,
         _datePublication, _dateCloture);
        emit OffreCree(offreCount, _titre, _description, _societe, _datePublication, 
        _dateCloture);
    }

    // Fonction pour récupérer toutes les offres
    function getAllOffres() public view returns(Offre[] memory) {
        Offre[] memory result = new Offre[](offreCount);
        for(uint i = 1; i <= offreCount; i++){
            result[i - 1] = offres[i];
        }
        return result;
    }

    // Fonction pour obtenir les détails d'une offre
    function getOffre(uint _numero) public view returns (Offre memory) {
        require(_numero <= offreCount && _numero > 0, "Offre non trouvee");
        return offres[_numero];
    }


    // Fonction pour obtenir la description d'une offre
    function getDescriptionOffre(uint _numero) public view returns(string memory){
        require(_numero <= offreCount && _numero > 0, "Offre non trouvee");
        return offres[_numero].description;
    }
}
