# Example 3: Unit testing a feature transformation

"""
An example of how you might incorporate unit tests into a ML workflow. Here we're using the titanic dataset as an example.
We're performing some preprocessing and want to make tests to verify that all of our operations are valid. Very useful to test to make sure your inputs are always as expected!
"""
import pandas as pd
import numpy as np
import unittest

def preprocessing_age(df):
    # a function to take in the age and replace nulls and max ages
    df["Age"] = np.where(
        (df["Age"] < 18) | (df["Age"] > 100), df["Age"].clip(18, 100), df["Age"]
    )  # replace max age with 100 and min age with 18
    df["Age"].fillna(df["Age"].median(), inplace=True)  # replace nans with the median
    return df


class FeatureTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            [
                [
                    1,
                    2,
                    "Mrs. Leopold (Mathilde Francoise Pede) Weisz",
                    "female",
                    10.0,
                    1,
                    0,
                    26.0,
                ],
                [0, 3, "Mr. Leo Zimmerman", "male", 102.0, 0, 0, 7.875],
                [0, 3, "Mr. Albert Augustsson", "male", 23.0, 0, 0, 7.8542],
                [0, 3, "Mr. Karl Alfred Backstrom", "male", 32.0, 1, 0, 15.85],
                [0, 3, "Mr. Michael Connaghton", "male", np.nan, 0, 0, 7.75],
            ],
            columns=[
                "Survived",
                "Pclass",
                "Name",
                "Sex",
                "Age",
                "Siblings/Spouses Aboard",
                "Parents/Children Aboard",
                "Fare",
            ],
        )

    def testAgePreprocess(self):
        preprocessed_df = preprocessing_age(self.df)
        self.assertEqual(all(preprocessed_df["Age"] >= 18), True)
        self.assertEqual(all(preprocessed_df["Age"] <= 100), True)
        self.assertEqual(preprocessed_df["Age"].isna().sum(), 0)

    def tearDown(self):
        del self.df


# Bonus Example: deep learning unit test example. Very challenging to implement, so enjoy the reading instead: https://medium.com/@keeper6928/how-to-unit-test-machine-learning-code-57cf6fd81765
