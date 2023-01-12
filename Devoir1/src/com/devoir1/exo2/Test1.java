package com.devoir1.exo2;

public class Test1 {

	public static void main(String[] args) {
		// TEST des TASSEAUX
		Produit t2 = new Tasseaux("T.30.33", 30, 33, true);
		Produit t1 = new Tasseaux("T.30.33", 30, 33, false);
		
		// Test du calcul de prix
		System.out.println(t2.calculPrix());
		
		System.out.println("Tasseaux de reference" + t1.reference + " " + t1.calculPrix());
		System.out.println("TEST DES PANNEAUX");

		Produit p1 = new Panneaux("P.60.100_20", 60, 100);
		Produit p2 = new Panneaux("P.60.90_10", 60, 90);
		
		System.out.println(p1.calculPrix());
		System.out.println(p2.calculPrix());
		
		// TEST DU PRIX DU MEUBLE
		
		//Liste de produits
		Produit [] p = {p1, t1};
	
		Produit meuble = new Meuble("Chaise",p,  10);
		System.out.println(meuble.calculPrix());
	}
}
