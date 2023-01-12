package com.devoir1.exo2;

public abstract class Produit {
	protected String reference;
	protected double largeur;
	protected double epaisseur;
	protected double longueur;
	protected boolean essence; // TRUE pour le chêne et FALSE pour les autres
	
	public Produit(String reference, double largeur) {
		this.longueur = longueur;
		this.reference = reference;
		this.epaisseur = epaisseur;
		this.largeur = largeur;
		this.essence = essence;		
	}
	
	public abstract double calculPrix();

}
