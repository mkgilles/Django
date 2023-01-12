package com.devoir1.exo1;

public class Devoir extends Examen {

	private Examen [] exos;
	private int points;
	private int  duree;

	public Devoir(Examen [] e) {
		super();
		this.exos = e;
		this.points = 0;
		this.duree = 0;
	}

	@Override
	public int getPoints() {
		
		for(Examen e: exos) {
			points = points + e.getPoints();
			
		}
		return points;
	}

	@Override
	public int getDuree() {
		for(Examen e: exos) {
			points = points + e.getDuree();
			
		}
		return points;
	}

}
