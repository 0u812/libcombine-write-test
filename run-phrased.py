import phrasedml, os

with open('./model/BIOMD0000000144.xml') as f:
    sbml_str = f.read()

with open('./experiment/Calzone2007-simulation-figure-1B.xml') as f:
    sedml_in = f.read()

phrasedml.setReferencedSBML('../model/BIOMD0000000144.xml', sbml_str)

phrasedml.convertString(sedml_in)

phrased_str = phrasedml.getLastPhraSEDML()

phrasedml.convertString(phrased_str)

sedml_out = phrasedml.getLastSEDML()

if not os.path.exists('phrased'):
    os.makedirs('phrased')

with open('./phrased/Calzone2007-simulation-figure-1B.xml', 'w') as f:
    f.write(sedml_out)
