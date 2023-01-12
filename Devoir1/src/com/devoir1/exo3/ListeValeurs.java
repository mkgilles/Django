package com.devoir1.exo3;

public class ListeValeurs {
	
	public static void main (String[] args) {

		TableauDeValeurs t1 = new Tableau(0.0, 99.0);
		t1.initialisationList();
		//System.out.println(tableau_De_Valeurs);
	//System.out.println(t1.list.size());

		/** SELECTION ALEATOIRE DES VALEURS DANS LE TABLEAU
		Random rand = new Random();
		int randomIndex = rand.nextInt(tableau_De_Valeurs.size());
		Double nombreAleatoire = tableau_De_Valeurs.get(randomIndex);
		// Affichage de la valeur aleatoire 

		System.out.println("Valeur aleatoire : "+ nombreAleatoire);
		
		tableau_De_Valeurs.ec*/
		//t1.affichageListe();
		Tableau t2 = new Tableau(0.0, 199.0);
		t2.initialisationList();
		
		//t2.affichageListe();
		//System.out.println(t2.echantReg(10));
		//t2.echantReg(10);
		t2.selectionAleatoire(10);
		System.out.println(t2.selectionReguliere(10));
		

	}

}
