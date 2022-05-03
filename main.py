int symbolNewtona(int n, int k) {
  int* tab = new int[n + 1];
  tab[0] = 1;
  tab[1] = 0;
  for (int i = 1; i < n; i++) {
    for (int j = i; j > 0; j--) {
      tab[j] = tab[j] + tab[j - 1];
    }
    tab[i + 1] = 0;
  }
  int wynik = tab[k];
  delete tab;
  return wynik;
}
