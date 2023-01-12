package com.devoir1.exo4;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class Test3 {

	public static void main(String[] args) {
	List<Double> list = new ArrayList<>();
			for (double i = -10.4; i <= 0.0; i++) {
				list.add(i);
			}
		
		ListValeurs t = new ListValeurs(list);
	
		// Echantillonage regulier
		System.out.println("ECHANTILLONAGE REGULIER");
		System.out.println(t.echantillonageReg(10));
		
		System.out.println("ECHANTILLONAGE ALEATOIRE");
		System.out.println(t.echantillonageAlea(10));
		
		System.out.println("ECHANTILLONAGE CONDITIONNEE");
		Predicate<Double> c = s -> s <= 0;
		System.out.println(t.echantillonContionne(5, c ));
	}

}
