package com.devoir1.exo4;

import java.util.List;

public abstract class TabDeValeurs {
	
	protected List<Double> valeurs;
	private double valeurDebut;
	private double valeurFin;
	public TabDeValeurs(List<Double> valeurs) {
		this.valeurs = valeurs;
	}
	
}
