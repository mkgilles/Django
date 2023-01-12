package com.devoir1.exo2;

import java.util.ArrayList;

public class Meuble extends Produit {
	private String ref;
	private int nombreDheure;
	private Produit c;
	private Produit[] produit;
	private double prix = 0;
	public Meuble(String reference, Produit[] p, int nombreDheure) {
		super(reference, nombreDheure);
		this.nombreDheure = nombreDheure;
		this.produit = p;

	}

	@Override
	public double calculPrix() {
		for(Produit c : produit) {
			prix = prix + (c.calculPrix());
		}
		return prix + 10*nombreDheure ;
	}

}
