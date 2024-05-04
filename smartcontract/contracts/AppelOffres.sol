// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract AppelOffres {

    // Structure pour stocker les détails de l'appel d'offres
    struct Offre {
        uint numero;
        string titre;
        string description;
        uint datePublication;
        uint dateCloture;
    }

    // Tableau des offres
    mapping(uint =>Offre) offres;
    uint public offreCount;

    function getOffreCount() public view returns(uint) {
        return offreCount;
    }

    // Fonction pour créer un nouvel appel d'offres
    function creerOffre( string memory _titre,string memory _description,uint _datePublication,uint _dateCloture
    ) public{
        uint num = offreCount +1;

        offres[offreCount] = Offre(num, _titre, _description,_datePublication,_dateCloture);
        offreCount++;
    
    }

    //recuperations de tous les offres
    function getAllOffres() public view returns(Offre[] memory){
        Offre[] memory result = new Offre[](offreCount);
        for(uint i=0;i<offreCount;i++){
            result[i] = offres[i];
        }
        return result;
    }

    // Fonction pour obtenir les détails d'une offre
    function getOffre(uint _index) public view returns (Offre memory) {
        return offres[_index];
    }

    // Fonction pour soumettre une offre (implémentation en attente)
    function soumettreOffre(uint _indexOffre, string memory _soumission) public {
        // TODO: Implémenter la logique de soumission d'offre
    }

    // Fonction pour évaluer les offres (implémentation en attente)
    function evaluerOffres() public {
        // TODO: Implémenter la logique d'évaluation des offres
    }

    // Fonction pour obtenir l'offre gagnante (implémentation en attente)
    function getOffreGagnante() public pure returns (Offre memory) {
        // TODO: Implémenter la logique pour déterminer l'offre gagnante
        return Offre(0,"", "", 0, 0);
    }

    function getDescriptionOffre(uint _numero) public view returns(string memory){
        require(_numero <= offreCount && _numero > 0 ,"offre Non trouve");

        return offres[_numero-1].description;
    }
}
