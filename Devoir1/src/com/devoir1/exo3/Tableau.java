package com.devoir1.exo3;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Tableau extends TableauDeValeurs implements EchantillonageReg, EchantillonageAlea {
	private List<Double> nbreDechantillon;
	private List[] souListe;
	private List<Double> echantillons;

	public Tableau(double valeurDebut, double valeurFin) {
		super(valeurDebut, valeurFin);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void initialisationList() {
		for (double i = valeurDebut; i <= valeurFin; i++) {
			list.add(i);
		}
	}

	@Override
	public List<Double> selectionReguliere(int nbreDechantillon) {
		int plage = list.size()/nbreDechantillon;
		echantillons = new ArrayList<>();
		for (int i = 0; i< list.size(); i+= plage) {
			echantillons.add(list.get(i));
		}
		return echantillons;

	}

	@Override
	public List<Double> selectionAleatoire(int nbreDechantillon) {
		Random random = new Random();
		echantillons = new ArrayList<>();
		for(int i = 0; i < nbreDechantillon; i++) {
			int randomIndex = random.nextInt(list.size());
			echantillons.add(list.get(randomIndex));
		}
		return echantillons;
	}
}
