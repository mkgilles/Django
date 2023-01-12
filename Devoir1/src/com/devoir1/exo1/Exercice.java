package com.devoir1.exo1;

public class Exercice extends Examen {
	
	private String sujet;
	private int points;
	private int duree;
	

	public Exercice(String sujet, int points, int duree) {
		super();
		this.sujet = sujet;
		this.points = points;
		this.duree = duree;
	}

	@Override
	public int getPoints() {
		// TODO Auto-generated method stub
		return points;
	}

	@Override
	public int getDuree() {
		// TODO Auto-generated method stub
		return duree;
	}

	public String getSujet() {
		return sujet;
	}
	
	

}
