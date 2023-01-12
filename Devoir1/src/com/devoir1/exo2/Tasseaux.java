package com.devoir1.exo2;

public class Tasseaux extends Produit{
	
	private double prix = 0;
	
	public Tasseaux(String reference, double largeur, double epaisseur, boolean essence) {
		super(reference, largeur);
		this.epaisseur = epaisseur;
		this.longueur = 240;
		this.essence = essence;
	}

	@Override
	public double calculPrix() {
		// TODO Auto-generated method stub
		if(this.essence) {
			prix = 0.012*largeur*epaisseur;
		}
		else {
			prix = 0.015*largeur*epaisseur;
		}
		return prix;
	}

	



	

}
