import constants as c

def fillMissingData(insuranceDataset):
    insuranceDataset[c.GENDER] = insuranceDataset[c.GENDER].fillna(c.UNKNOWN)
    insuranceDataset[c.MARITAL_STATUS] = insuranceDataset[c.MARITAL_STATUS].fillna(c.UNKNOWN)
    insuranceDataset[c.EDUCATION_LEVEL] = insuranceDataset[c.EDUCATION_LEVEL].fillna(c.UNKNOWN)
    insuranceDataset[c.OCCUPATION] = insuranceDataset[c.OCCUPATION].fillna(c.UNKNOWN)
    insuranceDataset[c.LOCATION] = insuranceDataset[c.LOCATION].fillna(c.UNKNOWN)
    insuranceDataset[c.POLICY_TYPE] = insuranceDataset[c.POLICY_TYPE].fillna(c.UNKNOWN)
    insuranceDataset[c.CUSTOMER_FEEDBACK] = insuranceDataset[c.CUSTOMER_FEEDBACK].fillna(c.UNKNOWN)
    insuranceDataset[c.SMOKING_STATUS] = insuranceDataset[c.SMOKING_STATUS].fillna(c.UNKNOWN)
    insuranceDataset[c.EXERCISE_FREQUENCY] = insuranceDataset[c.EXERCISE_FREQUENCY].fillna(c.UNKNOWN)
    insuranceDataset[c.PROPERTY_TYPE] = insuranceDataset[c.PROPERTY_TYPE].fillna(c.UNKNOWN)
    return insuranceDataset