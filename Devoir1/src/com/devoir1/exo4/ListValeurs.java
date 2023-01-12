package com.devoir1.exo4;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.function.Predicate;

public class ListValeurs extends TabDeValeurs implements TypeRegulier, TypeAleatoire, TypeCondtionne{
	List<Double> echantillons = new ArrayList<>();
	public ListValeurs(List<Double> valeurs) {
		super(valeurs);
		// TODO Auto-generated constructor stub
	}

	@Override
	public List<Double> echantillonageReg(int nbrEchantillons) {
		
		for(int i = 0; i < valeurs.size(); i+= valeurs.size()/nbrEchantillons) {
			echantillons.add(valeurs.get(i));
		}
		return echantillons;
	}

	@Override
	public List<Double> echantillonageAlea(int nbrEchantillons) {
		Random alea = new Random();
		
		for(int i = 0; i < nbrEchantillons; i+= valeurs.size()/nbrEchantillons) {
			int index =  alea.nextInt(valeurs.size());
			echantillons.add(valeurs.get(index));
		}
		
		return echantillons;
	}

	@Override
	public List<Double> echantillonContionne(int nbrEchantillons, Predicate<Double> condition) {
		for(Double valeur: valeurs) {
			if(condition.test(valeur)) {
				echantillons.add(valeur);
				if(echantillons.size()== nbrEchantillons) {
					break;
				}
			}
		}
		
		return echantillons;
	}

}
