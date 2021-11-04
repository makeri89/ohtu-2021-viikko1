import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_negatiivisen_maaran_lisaaminen_ei_onnistu(self):
        alkuperainen_tila = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), alkuperainen_tila)
        
    def test_liian_suuren_maaran_lisaamine_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
        
    def test_negatiivisen_maaran_ottaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(5)
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, alkuperainen_saldo)
        
    def test_liian_suuren_maaran_ottaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(otto, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_tuloste_on_oikeanlainen(self):
        haluttu_tuloste = 'saldo = 4, vielä tilaa 6'
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(self.varasto.__str__(), haluttu_tuloste)
            
    def test_negatiivinen_tilavuus_nollaantuu(self):
        uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(uusi_varasto.tilavuus, 0)
        
    def test_negatiivinen_alku_saldo_nollaantuu(self):
        uusi_varasto = Varasto(10,-10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)
        
    def test_liian_suuri_alku_saldo(self):
        uusi_varasto = Varasto(5,10)
        self.assertAlmostEqual(uusi_varasto.saldo, uusi_varasto.tilavuus)
        
    
