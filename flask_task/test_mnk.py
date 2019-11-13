import unittest
import numpy
import mnk as mnk
import reader as reader


class CalcTest(unittest.TestCase):
    def test_lin_mnk(self):
        "Test linear regression"
        self.assertAlmostEqual(mnk.lin_mnk([1,2,3,4,5],[1,1.2,3,7,7])[0], -1.5)
        self.assertAlmostEqual(mnk.lin_mnk([1,2,3,4,5],[1,1.2,3,7,7])[1], 1.78)
    
    def test_lin_dif(self):
        self.assertAlmostEqual(mnk.lin_mnk([1,2,3,4,5],[1,1.2,3,7,7, 9])[0], -1.5)
        self.assertAlmostEqual(mnk.lin_mnk([1,2,3,4,5],[1,1.2,3,7,7,9])[1], 1.78)
    
    def test_sum_s(self):
        self.assertAlmostEqual(mnk.sum_s([9,2,4,6,4],5),68905)
        self.assertAlmostEqual(mnk.sum_s([9,2,4,6,4],-1),1.277777778)
    
    def test_sum_xy(self):
        res=mnk.sum_xy([1,2,3],[3,4,5], 2)
        self.assertAlmostEqual(res, 3+16+45)
        self.assertAlmostEqual(mnk.sum_xy([2,4],[1,1],-1), 2)

    def test_mnk(self):

        self.assertTrue(numpy.allclose(mnk.mnk([1,2,3,4,5,6],[3,4,5,6,7,8],1),[2,1]))
        self.assertRaises(AssertionError,numpy.testing.assert_array_equal(mnk.mnk([1,2,3,4,5,6],[3,4,5,6,7,8],1),[2,1]))

    def test_predict(self):
  
        r=mnk.predict([1,2,3,4,5],["2019/11/01", "2019/11/02", "2019/11/03","2019/11/04","2019/11/05"], 1, 0)
        r1=["2019/11/01", "2019/11/02", "2019/11/03","2019/11/04","2019/11/05","2019/11/06"]
        r2=[1,2,3,4,5,6]
        for i in range(len(r)):
            self.assertAlmostEqual(r[1][i],r1[i])
            self.assertAlmostEqual(r[0][i], r2[i])

    def test_db_connect(self):
        self.assertIsNotNone(reader.IOClass.dbConnect('http://localhost:8091'))
        #print(reader.IOClass.dbConnect('http://localhost:8091'))
    
    def test_read_json(self):
        r=reader.IOClass.readJSON('http://localhost:8091')
        exp={
            "2019/10/04": {
                "Aval": {
                    "EUR_buy": "26.60",
                    "EUR_sell": "27.80",
                    "RUB_buy": "0.372",
                    "RUB_sell": "0.375",
                    "USD_buy": "23.50",
                    "USD_sell": "25.35"
                },
                "Oschad": {
                    "EUR_buy": "26.4000",
                    "EUR_sell": "27.8500",
                    "RUB_buy": "0.2300",
                    "RUB_sell": "0.3900",
                    "USD_buy": "24.5000",
                    "USD_sell": "26.5000"
                },
                "Privat": {
                    "EUR_buy": "27.1",
                    "EUR_sell": "28.85",
                    "RUB_buy": "0.353",
                    "RUB_sell": "0.389",
                    "USD_buy": "24.9",
                    "USD_sell": "25.5"
                }
                },
            "2019/11/05": {
                    "Aval": {
                        "EUR_buy": "27.10",
                        "EUR_sell": "27.70",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.395",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.8000",
                        "EUR_sell": "27.8500",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1500"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
                    },
            "2019/11/06":  {
                    "Aval": {
                        "EUR_buy": "27.15",
                        "EUR_sell": "27.55",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.391",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.7000",
                        "EUR_sell": "27.7000",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1000"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
    }
        } 
        self.assertIsNotNone(r)
        self.assertDictEqual(r,exp)

    def test_makeArraysByBankCurr(self):
        exp={
            "2019/10/04": {
                "Aval": {
                    "EUR_buy": "26.60",
                    "EUR_sell": "27.80",
                    "RUB_buy": "0.372",
                    "RUB_sell": "0.375",
                    "USD_buy": "23.50",
                    "USD_sell": "25.35"
                },
                "Oschad": {
                    "EUR_buy": "26.4000",
                    "EUR_sell": "27.8500",
                    "RUB_buy": "0.2300",
                    "RUB_sell": "0.3900",
                    "USD_buy": "24.5000",
                    "USD_sell": "26.5000"
                },
                "Privat": {
                    "EUR_buy": "27.1",
                    "EUR_sell": "28.85",
                    "RUB_buy": "0.353",
                    "RUB_sell": "0.389",
                    "USD_buy": "24.9",
                    "USD_sell": "25.5"
                }
                },
            "2019/11/05": {
                    "Aval": {
                        "EUR_buy": "27.10",
                        "EUR_sell": "27.70",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.395",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.8000",
                        "EUR_sell": "27.8500",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1500"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
                    },
            "2019/11/06":  {
                    "Aval": {
                        "EUR_buy": "27.15",
                        "EUR_sell": "27.55",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.391",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.7000",
                        "EUR_sell": "27.7000",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1000"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
    }}
        r=reader.IOClass.makeArraysByBankCurr(exp,"Privat", "EUR")
        self.assertListEqual(r[0],["2019/10/04","2019/11/05", "2019/11/06"])
        self.assertListEqual(r[1],[27.1,27.1,27.1])
        self.assertListEqual(r[2],[28.85,27.65,27.65])

    def test_makeAll(self):
        exp={
            "2019/10/04": {
                "Aval": {
                    "EUR_buy": "26.60",
                    "EUR_sell": "27.80",
                    "RUB_buy": "0.372",
                    "RUB_sell": "0.375",
                    "USD_buy": "23.50",
                    "USD_sell": "25.35"
                },
                "Oschad": {
                    "EUR_buy": "26.4000",
                    "EUR_sell": "27.8500",
                    "RUB_buy": "0.2300",
                    "RUB_sell": "0.3900",
                    "USD_buy": "24.5000",
                    "USD_sell": "26.5000"
                },
                "Privat": {
                    "EUR_buy": "27.1",
                    "EUR_sell": "28.85",
                    "RUB_buy": "0.353",
                    "RUB_sell": "0.389",
                    "USD_buy": "24.9",
                    "USD_sell": "25.5"
                }
                },
            "2019/11/05": {
                    "Aval": {
                        "EUR_buy": "27.10",
                        "EUR_sell": "27.70",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.395",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.8000",
                        "EUR_sell": "27.8500",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1500"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
                    },
            "2019/11/06":  {
                    "Aval": {
                        "EUR_buy": "27.15",
                        "EUR_sell": "27.55",
                        "RUB_buy": "0.380",
                        "RUB_sell": "0.391",
                        "USD_buy": "24.45",
                        "USD_sell": "24.85"
                    },
                    "Oschad": {
                        "EUR_buy": "26.7000",
                        "EUR_sell": "27.7000",
                        "RUB_buy": "0.2300",
                        "RUB_sell": "0.3950",
                        "USD_buy": "24.5000",
                        "USD_sell": "25.1000"
                    },
                    "Privat": {
                        "EUR_buy": "27.1",
                        "EUR_sell": "27.65",
                        "RUB_buy": "0.355",
                        "RUB_sell": "0.392",
                        "USD_buy": "24.5",
                        "USD_sell": "24.84"
                    }
    }}
        res=(["2019/10/04","2019/11/05", "2019/11/06"],[27.1,27.1,27.1],[28.85,27.65,27.65],"Privat", "EUR")
        r=reader.IOClass.makeAll(exp)[0]
        self.assertTupleEqual(r,res)

if __name__ == '__main__':
    unittest.main()


