from reseau import Reseau

res = Reseau()

res.setError(0.05)

res.print_data()
res.setCouche(4)
res.add_all_neurone([32, 20, 12, 4])
res.creer_reseau()
res.print_all()
