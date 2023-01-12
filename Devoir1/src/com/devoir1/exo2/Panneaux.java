package com.devoir1.exo2;

public class Panneaux extends Produit  {
	private double prix = 0;

	public Panneaux(String reference, double longueur, double largeur) {
		super(reference, largeur);
		// TODO Auto-generated constructor stub
		this.longueur = longueur;
		this.epaisseur = epaisseur;
	}

	@Override
	public double calculPrix() {
		prix = 0.01*longueur*largeur;
		
		return prix;
	}

}
