import phrasedml, os

with open('./model/BIOMD0000000144.xml') as f:
    sbml_str = f.read()

with open('./phrased/Calzone2007-simulation-figure-1B.xml') as f:
    phrased_str = f.read()

phrasedml.setReferencedSBML('../model/BIOMD0000000144.xml', sbml_str)

phrasedml.convertString(phrased_str)

sedml_str = phrasedml.getLastSEDML()

os.makedirs('phrased')
with open('./phrased/Calzone2007-simulation-figure-1B.xml', 'w') as f:
    f.write(sedml_str)
