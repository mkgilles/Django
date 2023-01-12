package com.devoir1.exo1;

public class QCM extends Examen{
	private String [] questions;
	private int points;
	private int duree;
	
	public QCM(String[] q, int p, int d) {
		super();
		this.questions = q;
		this.points = p;
		this.duree = d;
		
	}	

	@Override
	public int getPoints() {
		int c = this.questions.length;
		points = this.points*c;
		return points;
	}

	@Override
	public int getDuree() {
		// TODO Auto-generated method stub
		return duree;
	}

}
