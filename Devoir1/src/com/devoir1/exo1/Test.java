package com.devoir1.exo1;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Exercice exo1 = new Exercice("Heritage", 10, 22);
		Exercice exo2 = new Exercice("Polymorhisme", 5, 15);
		Examen exo3 = new Exercice("Abstraction", 6, 20);
		Examen exo4 = new Exercice("Surcharge", 15, 35);
		Examen exo5 = new Exercice("Implementation", 7, 10);
		
		//Tableau contenant les differents exercies
		Exercice[] ex = {exo1} ;
		
		
		String[] q = {"Q1", "Q2", "Q3"};
		
		Examen QCM = new QCM(q, 10, 20);
		Devoir D = new Devoir(ex);
		
		System.out.println("Test de verification sur les exercices");
		System.out.println("#######################################");
		
		System.out.println(exo1.getDuree());
		System.out.println(exo2.getDuree());
		System.out.println(exo3.getDuree());
		
		System.out.println("Test de verification sur les QCMs");
		System.out.println("#######################################");
		
		System.out.println("Duree du QCM : " + QCM.getDuree());
		System.out.println("Nombre de points du QCM : " + QCM.getPoints());
		
		System.out.println("Test de verification sur le devoir");
		System.out.println("#######################################");
		
		System.out.println("Nombre de points du Devoir : " + D.getPoints());
		System.out.println("Duree du Devoir : " + D.getDuree());
		System.out.println("Nombre liste des exercices du Devoir : " + D.toString());
		

	}

}
