import unittest
import pandas as pd

def check_type(column, valid_types, column_name):
    return all(isinstance(x, valid_types) for x in column), f"{column_name} is not valid"

class TestData(unittest.TestCase):
    def test_excel_data(self):
        dataframe = pd.read_excel('../data.xlsx')
        self.assertTrue(*check_type(dataframe['open'], (int, float), 'Open'))
        self.assertTrue(*check_type(dataframe['high'], (int, float), 'High'))
        self.assertTrue(*check_type(dataframe['low'], (int, float), 'Low'))
        self.assertTrue(*check_type(dataframe['close'], (int, float), 'Close'))
        self.assertTrue(*check_type(dataframe['volume'], int, 'volume'))
        self.assertTrue(*check_type(dataframe['instrument'], str, 'Instrument'))
        self.assertTrue(*check_type(dataframe['datetime'], pd.Timestamp, 'Datetime'))
    # def test_valid_data(self):
    #     data = {
    #         'open': [100.0, 101.5, 99.8, 102.2],
    #         'high': [102.0, 103.2, 101.0, 104.0],
    #         'low': [98.5, 100.0, 98.0, 99.5],
    #         'close': [101.0, 102.0, 100.5, 103.0],
    #         'Volume': [1000, 1500, 800, 1200],
    #         'instrument': ['HINDALCO', 'HINDALCO', 'HINDALCO', 'HINDALCO'],
    #         'date': [pd.Timestamp('2018-01-01'), pd.Timestamp('2016-01-02'), pd.Timestamp('2017-02-03'), pd.Timestamp('2015-01-04')]
    #     }
        
    #     dataframe = pd.DataFrame(data)
    #     self.assertTrue(*check_type(dataframe['open'], (int, float), 'Open'))
    #     self.assertTrue(*check_type(dataframe['high'], (int, float), 'High'))
    #     self.assertTrue(*check_type(dataframe['low'], (int, float), 'Low'))
    #     self.assertTrue(*check_type(dataframe['close'], (int, float), 'Close'))
    #     # self.assertTrue(*check_type(dataframe['volume'], int, 'Volume'))
    #     self.assertTrue(*check_type(dataframe['instrument'], str, 'Instrument'))
    #     self.assertTrue(*check_type(dataframe['date'], pd.Timestamp, 'Datetime'))
    
    # def test_invalid_data(self):
    #     data = {
    #         'open': [100.0, 'Invalid', 99.8, 102.2],
    #         'high': [102.0, 103.2, 101.0, 104.0],
    #         'low': [98.5, 100.0, 'Invalid', 99.5],
    #         'close': [101.0, 102.0, 100.5, 103.0],
    #         'volume': [1000, 1500, 800, 1200],
    #         'instrument': [100, 'GOOG', 'MSFT', 'TSLA'],
    #         'date': [pd.Timestamp('2023-01-01'), 'Invalid', pd.Timestamp('2023-01-03'), pd.Timestamp('2023-01-04')]
    #     }

    #     dataframe = pd.DataFrame(data)
    #     print(dataframe['volume'])

    #     self.assertTrue(*check_type(dataframe['open'], (int, float), 'Open'))
    #     self.assertTrue(*check_type(dataframe['high'], (int, float), 'High'))
    #     self.assertTrue(*check_type(dataframe['low'], (int, float), 'Low'))
    #     self.assertTrue(*check_type(dataframe['close'], (int, float), 'Close'))
    #     self.assertTrue(*check_type(dataframe['volume'], int, 'Volume'))
    #     self.assertTrue(*check_type(dataframe['instrument'], str, 'Instrument'))
    #     self.assertTrue(*check_type(dataframe['date'], pd.Timestamp, 'Datetime'))

    
        


# if __name__ == '__main__':
#     unittest.main()
