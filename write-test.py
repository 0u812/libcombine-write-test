from libcombine import CombineArchive, KnownFormats

# Create archive with original SED-ML
archive_sedml = CombineArchive()

# Add SBML
archive_sedml.addFile(
    './model/BIOMD0000000144.xml', # source path
    './model/BIOMD0000000144.xml', # dest path
    KnownFormats.lookupFormat('sbml'),
    False # master attribute
)

# Add SED-ML
archive_sedml.addFile(
    './experiment/Calzone2007-simulation-figure-1B.xml', # source path
    './experiment/Calzone2007-simulation-figure-1B.xml', # dest path
    KnownFormats.lookupFormat('sedml'),
    True # master attribute
)

archive_sedml.writeToFile('out_sedml.omex')

# ************************************************

# Create archive with PhraSEDML-processed SED-ML
archive_phrasedml = CombineArchive()

# Add SBML
archive_phrasedml.addFile(
    './model/BIOMD0000000144.xml', # source path
    './model/BIOMD0000000144.xml', # dest path
    KnownFormats.lookupFormat('sbml'),
    False # master attribute
)

# Add SED-ML processed by phrasedml
archive_phrasedml.addFile(
    './phrased/Calzone2007-simulation-figure-1B.xml', # source path
    './phrased/Calzone2007-simulation-figure-1B.xml', # dest path
    KnownFormats.lookupFormat('sedml'),
    True # master attribute
)

archive_phrasedml.writeToFile('out_phrasedml.omex')
