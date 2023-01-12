package com.devoir1.exo4;

import java.util.List;
import java.util.function.Predicate;

public interface TypeCondtionne {
	public List<Double> echantillonContionne(int nbrEchantillons, Predicate<Double> condition);

}
