package com.devoir1.exo3;

import java.util.ArrayList;
import java.util.List;

public abstract class TableauDeValeurs {
	
	protected double valeurDebut;
	protected double valeurFin;
	protected List<Double> list;
	
	public TableauDeValeurs(double valeurDebut, double valeurFin) {
		super();
		this.valeurDebut = valeurDebut;
		this.valeurFin = valeurFin;
		this.list = new ArrayList<>();
	}
	
	public abstract void initialisationList();
	public void affichageListe() {
		System.out.println("Liste des elements du tableau : ");
		for (Double d : list) {
			System.out.println(d);
		}
		
	}
	
	
}
